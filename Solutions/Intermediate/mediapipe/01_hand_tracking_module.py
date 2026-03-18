"""
Exercise Goal:
Build a reusable hand-tracking module that outputs landmarks and handedness per frame.

Builds Toward:
A gesture-driven UI controller that can plug into games, robot controls, or touchless dashboards.

ASSETS NEEDED:
- Optional test video file: assets/videos/hand_gestures.mp4
- If no video is provided, use a webcam.
"""

from dataclasses import dataclass
from typing import Any

import cv2
import mediapipe as mp


@dataclass
class HandTrackingConfig:
    max_num_hands: int = 2
    min_detection_confidence: float = 0.65
    min_tracking_confidence: float = 0.60


class HandTrackingModule:
    def __init__(self, config: HandTrackingConfig) -> None:
        self.config = config
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=config.max_num_hands,
            min_detection_confidence=config.min_detection_confidence,
            min_tracking_confidence=config.min_tracking_confidence,
        )

    def process_frame(self, frame_bgr: Any) -> dict[str, Any]:
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        result = self.hands.process(frame_rgb)

        # TODO(student): Return a richer structure with per-hand pixel coordinates,
        # handedness label, and confidence score.
        return {
            "raw_result": result,
            "num_hands": 0 if result.multi_hand_landmarks is None else len(result.multi_hand_landmarks),
        }

    def draw_landmarks(self, frame_bgr: Any, result: Any) -> Any:
        if result.multi_hand_landmarks is None:
            return frame_bgr

        for hand_landmarks in result.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                frame_bgr,
                hand_landmarks,
                self.mp_hands.HAND_CONNECTIONS,
            )

        return frame_bgr


def open_capture(path: str | None = None) -> cv2.VideoCapture:
    if path:
        return cv2.VideoCapture(path)
    return cv2.VideoCapture(0)


def main() -> None:
    # TODO(student): Try both webcam and file-based testing.
    cap = open_capture(path=None)
    tracker = HandTrackingModule(config=HandTrackingConfig())

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        output = tracker.process_frame(frame)
        visual = tracker.draw_landmarks(frame, output["raw_result"])

        cv2.putText(
            visual,
            f"Hands: {output['num_hands']}",
            (12, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

        cv2.imshow("Intermediate: Hand Tracking Module", visual)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
