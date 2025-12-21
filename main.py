# ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦
# ✦ Author  : Sobaha
# ✦ Created : 2025-12-15 12:31:27
# ✦ Life Is a Series of Events
# ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦
import torch
import numpy as np
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from scipy.signal import resample
import wave
import base64
import time
from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel
from typing import List
import io

from datetime import datetime
from loguru import logger

from asr_output_fixing import fix_transcription_output

# logger configuration
logger.add(
    "log_folder/{time:YYYY-MM-DD}.log",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
)

app = FastAPI()

# Constants
RATE = 16000  # Target sampling rate
SAVE_DIR = "EC_ASR_AUDIO"
AUTO_CORRECTION = True

import os

# Check if the directory exists
if not os.path.exists(SAVE_DIR):
    # Create the directory
    os.makedirs(SAVE_DIR)
    print(f"Directory '{SAVE_DIR}' was created.")
else:
    print(f"Directory '{SAVE_DIR}' already exists.")

# Initialize the Wav2Vec2 model and processor (this is the same model as bengali ai 2nd we used for the live cc just dir name is different)
model_name = "bangla_wav2vec2_live_asr_model"  # Replace with your model name
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

# Use GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Pydantic models to mirror the Java request/response structure
class Language(BaseModel):
    sourceLanguage: str

class Config(BaseModel):
    language: Language

class AudioContent(BaseModel):
    audioContent: str  # Base64 encoded audio

class AsrRequest(BaseModel):
    config: Config
    audio: List[AudioContent]

class Output(BaseModel):
    source: str

class AsrResponse(BaseModel):
    taskType: str
    output: List[Output]
    time_taken: float

def normalize_audio(audio_data, target_level=-20.0):
    """Normalize audio to the target RMS level in dBFS."""
    rms = np.sqrt(np.mean(audio_data**2))  # Calculate the RMS
    scalar = 10**(target_level / 20.0) / (rms + 1e-6)  # Calculate normalization scalar
    normalized_audio = audio_data * scalar  # Apply normalization
    return np.clip(normalized_audio, -1.0, 1.0)  # Clip to [-1.0, 1.0] range to avoid clipping distortion

def save_audio(audio_data, filename='default'):
    if filename=='default':
        # filename = 'EC_AUDIO_DATA_wav2vec2_'+str(time.time())+'.wav'
        filename = f'{SAVE_DIR}/EC_AUDIO_DATA_wav2vec2_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.wav'
    """Save the audio data to a WAV file."""
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)   # 2 bytes for int16
        wav_file.setframerate(RATE)
        wav_file.writeframes((audio_data * 32768).astype(np.int16).tobytes())

# Function to load and resample audio data
def load_audio_from_base64(audio_content: str, target_rate=RATE):
    """Convert base64 encoded audio to waveform and resample it if necessary."""
    audio_data = base64.b64decode(audio_content)

    
    # Use BytesIO to create a file-like object from the audio data
    with io.BytesIO(audio_data) as wav_file:
        with wave.open(wav_file, 'rb') as wav_file:
            framerate = wav_file.getframerate()
            num_frames = wav_file.getnframes()
            logger.info(f"Audio framerate: {framerate} Hz")
            
            # Read audio data and normalize it
            audio_data = np.frombuffer(wav_file.readframes(num_frames), dtype=np.int16).astype(np.float32) / 32768.0

            # audio_data = normalize_audio(audio_data=audio_data)

            # Resample audio if the sample rate is not the target rate (16kHz)
            # if framerate != target_rate:
            #     num_samples = round(len(audio_data) * target_rate / framerate)
            #     audio_data = resample(audio_data, num_samples)
            if framerate != target_rate:
                audio_data = librosa.resample(audio_data, orig_sr=framerate, target_sr=target_rate)
                logger.info(f"Audio resampled to {target_rate} Hz")

            return audio_data

def transcribe_audio(audio_data):

    """Transcribe single audio data using Wav2Vec2 model."""
    # Process the audio data with the processor
    input_values = processor(audio_data, return_tensors="pt", sampling_rate=RATE).input_values.to(device)

    # Inference with half precision if on GPU
    with torch.no_grad():
        logits = model(input_values).logits

    # Decode predicted tokens to text
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]

    # hardcoded transcription fixing 
    if AUTO_CORRECTION:
        transcription = fix_transcription_output(transcription)

    return transcription

@app.post("/asr", response_model=AsrResponse)
async def process_asr(request: AsrRequest):
    start_time = time.time()
    
    # Check if audio is present
    if not request.audio or len(request.audio) == 0:
        raise HTTPException(status_code=400, detail="No audio content provided")
    


    # Decode and process the audio content
    try:
    
        # -----------------------------
        audio_data = load_audio_from_base64(request.audio[0].audioContent)
        transcription = transcribe_audio(audio_data)

        # in prouction this line must be commented now this is just saving audio for better testing purpose
        save_audio(audio_data)

        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing audio: " + str(e))

    # Calculate time taken
    time_taken = time.time() - start_time

    # Create response
    response = AsrResponse(
        taskType="ASR",
        output=[Output(source=transcription)],
        time_taken=time_taken
    )

    # print(response)
    logger.info(response)

    return response
