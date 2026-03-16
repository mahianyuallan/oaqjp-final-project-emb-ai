"""Unit tests for EmotionDetection package."""

import unittest

from EmotionDetection import emotion_detector


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

        for statement, expected_emotion in test_cases.items():
            result = emotion_detector(statement)
            self.assertEqual(result["dominant_emotion"], expected_emotion)


if __name__ == "__main__":
    unittest.main()
