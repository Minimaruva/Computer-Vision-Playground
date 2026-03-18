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
        # TODO(student): Implement temporal smoothing.
        # Hint: Start with exponential moving average, then make alpha velocity-aware.
        raise NotImplementedError("Implement landmark smoothing")


class PoseModule:
    def __init__(self) -> None:
        # TODO(student): Initialize MediaPipe Pose model.
        raise NotImplementedError("Implement pose module initialization")

    def extract(self, frame_bgr: Any) -> Any:
        # TODO(student): Convert frame to RGB and run pose inference.
        raise NotImplementedError("Implement pose extraction")


def landmarks_to_array(results: Any) -> np.ndarray | None:
    # TODO(student): Convert pose landmarks to NumPy array of shape (N, 4).
    # Hint: Use [x, y, z, visibility] per landmark.
    raise NotImplementedError("Implement landmark conversion")


def main() -> None:
    # TODO(student):
    # 1) Open assets/videos/fitness_pose.mp4.
    # 2) Extract pose landmarks frame-by-frame.
    # 3) Smooth landmarks and render your own visualization.
    # 4) Display output and exit cleanly on 'q'.
    raise NotImplementedError("Implement exercise runner")


if __name__ == "__main__":
    main()
