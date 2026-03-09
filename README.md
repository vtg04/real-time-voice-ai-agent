# Real-Time Voice AI Agent

A production-style **real-time voice AI system** that enables natural voice conversations with an LLM using streaming speech recognition, voice activity detection, and text-to-speech synthesis.

This project demonstrates how modern voice assistants are built using **CPU-friendly models and streaming architectures**.

---

# Features

• Real-time microphone streaming via WebSockets  
• Voice Activity Detection (Silero VAD) for turn detection  
• Speech-to-Text using Faster-Whisper (CPU optimized)  
• LLM response generation via Groq API  
• Text-to-Speech using Piper TTS  
• Browser-based microphone interface  
• Partial transcript streaming for improved UX  

---

# Tech Stack

### Backend
- FastAPI
- WebSockets
- Python

### Speech Processing
- Faster-Whisper (Speech Recognition)
- Silero VAD (Voice Activity Detection)

### LLM
- Groq API
- LLaMA 3.1 / Mixtral models

### Text-to-Speech
- Piper TTS

### Frontend
- Web Audio API
- Vanilla JavaScript

---

frontend/
└── index.html

requirements.txt
README.md
