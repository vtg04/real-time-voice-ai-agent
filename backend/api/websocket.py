from fastapi import APIRouter, WebSocket
import tempfile, os
import numpy as np
import soundfile as sf

from voice.asr import transcribe
from voice.vad import is_speech
from core.llm_client import call_llm
from voice.tts import synthesize

router = APIRouter()

@router.websocket("/ws/voice")
async def voice_ws(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            audio_bytes = await ws.receive_bytes()

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
                f.write(audio_bytes)
                audio_path = f.name

            audio_np, sr = sf.read(audio_path)
            if not is_speech(audio_np, sr):
                os.remove(audio_path)
                continue

            text = transcribe(audio_path)
            await ws.send_text(f"PARTIAL_TRANSCRIPT:{text}")

            reply = call_llm(text)
            tts_audio = synthesize(reply)

            with open(tts_audio, "rb") as f:
                await ws.send_bytes(f.read())

            os.remove(audio_path)
            os.remove(tts_audio)

    except Exception:
        await ws.close()
