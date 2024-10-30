import numpy as np
import librosa

def detect_pitch(audio_file):
    y, sr = librosa.load(audio_file)
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    # Extract the highest magnitude pitch
    pitch = pitches[magnitudes.argmax()]
    return pitch
