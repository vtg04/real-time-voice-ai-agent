import torch
import numpy as np

# Load Silero VAD from torch hub
model, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-vad',
    model='silero_vad',
    force_reload=False
)

(get_speech_timestamps, _, _, _, _) = utils

def is_speech(audio_np, sample_rate=16000):
    ts = get_speech_timestamps(audio_np, model, sampling_rate=sample_rate)
    return len(ts) > 0
