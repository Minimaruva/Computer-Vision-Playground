"""
Exercise Goal:
Implement temporal smoothing for pose landmarks to reduce jitter while preserving motion.

Builds Toward:
A stable human-pose analytics pipeline for fitness coaching and action recognition.

ASSETS NEEDED:
- Video clip with full-body motion: assets/videos/fitness_pose.mp4
"""

from collections import deque
from dataclasses import dataclass
from typing import Any

import cv2
import mediapipe as mp
import numpy as np


@dataclass
class SmootherConfig:
    history_size: int = 5
    alpha: float = 0.4


class LandmarkSmoother:
    def __init__(self, config: SmootherConfig) -> None:
        self.config = config
        self.history: deque[np.ndarray] = deque(maxlen=config.history_size)

    def smooth(self, current_landmarks: np.ndarray) -> np.ndarray:
        # TODO(student): Implement adaptive smoothing where alpha changes based on velocity.
        # Hint: Fast motion -> higher alpha; still frames -> lower alpha.
        if len(self.history) == 0:
            self.history.append(current_landmarks)
            return current_landmarks

        previous = self.history[-1]
        smoothed = self.config.alpha * current_landmarks + (1 - self.config.alpha) * previous
        self.history.append(smoothed)
        return smoothed


class PoseModule:
    def __init__(self) -> None:
        self.pose = mp.solutions.pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6,
        )

    def extract(self, frame_bgr: Any) -> Any:
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        return self.pose.process(frame_rgb)


def landmarks_to_array(results: Any) -> np.ndarray | None:
    if results.pose_landmarks is None:
        return None

    coords = []
    for lm in results.pose_landmarks.landmark:
        coords.append([lm.x, lm.y, lm.z, lm.visibility])
    return np.array(coords, dtype=np.float32)


def main() -> None:
    cap = cv2.VideoCapture("assets/videos/fitness_pose.mp4")
    pose = PoseModule()
    smoother = LandmarkSmoother(config=SmootherConfig())

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        results = pose.extract(frame)
        landmarks = landmarks_to_array(results)

        if landmarks is not None:
            smoothed = smoother.smooth(landmarks)
            # TODO(student): Reproject smoothed normalized coordinates into pixels
            # and draw your own landmark renderer instead of default drawing utils.
            cv2.putText(
                frame,
                f"Smoothed landmarks: {smoothed.shape[0]}",
                (12, 28),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

        cv2.imshow("Intermediate: Pose Landmark Smoother", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
