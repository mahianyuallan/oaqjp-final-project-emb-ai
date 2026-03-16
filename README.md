# Final Project - Emotion Detector

Emotion Detector is a Flask web app that analyzes text emotions with the Watson NLP emotion model and returns a formatted response including the dominant emotion.

## Project Structure

- `EmotionDetection/emotion_detection.py`: Watson NLP integration and response formatting.
- `EmotionDetection/__init__.py`: Package export for `emotion_detector`.
- `test_emotion_detection.py`: Unit tests for dominant-emotion behavior.
- `server.py`: Flask deployment and blank-input handling.

## Run Locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py
```

Then open `http://localhost:5000`.
