"""Unit tests for EmotionDetection package."""

import unittest
from unittest.mock import patch

from EmotionDetection import emotion_detector


class MockResponse:
    """Simple response object for mocked requests."""

    def __init__(self, status_code=200, emotion=None):
        self.status_code = status_code
        self._emotion = emotion

    def json(self):
        """Return payload matching Watson API schema."""
        return {"emotionPredictions": [{"emotion": self._emotion}]}


def mocked_requests_post(_url, json, headers=None, timeout=30):
    """Return deterministic emotions based on known test phrases."""
    text = (json["raw_document"]["text"] or "").strip()
    if not text:
        return MockResponse(status_code=400)

    labels = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear",
    }
    dominant = labels[text]
    emotion = {
        "anger": 0.01,
        "disgust": 0.01,
        "fear": 0.01,
        "joy": 0.01,
        "sadness": 0.01,
    }
    emotion[dominant] = 0.95
    return MockResponse(status_code=200, emotion=emotion)


class TestEmotionDetector(unittest.TestCase):
    """Validate dominant emotions for known sample statements."""

    def test_emotion_detector(self):
        """Check expected dominant emotion labels."""
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }

        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            side_effect=mocked_requests_post,
        ):
            for statement, expected_emotion in test_cases.items():
                result = emotion_detector(statement)
                self.assertEqual(result["dominant_emotion"], expected_emotion)


if __name__ == "__main__":
    unittest.main()
