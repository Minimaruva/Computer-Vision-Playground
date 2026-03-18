"""
Exercise Goal:
Build a reusable hand-tracking module that outputs landmarks and handedness per frame.

Builds Toward:
A gesture-driven UI controller that can plug into games, robot controls, or touchless dashboards.

Module Architecture:
1) HandTrackingConfig stores tunable runtime parameters.
2) HandTrackingModule owns model lifecycle and frame processing methods.
3) open_capture() abstracts webcam/file input.
4) main() runs the event loop and handles cleanup.

API-Level Notes:
- MediaPipe Hands expects RGB input (not BGR).
- The detector returns normalized landmark coordinates (x, y in [0,1]).
- You should convert normalized values to pixel coordinates before rendering or downstream logic.

Standard Practices:
- Keep model initialization outside the frame loop.
- Separate detection output from rendering code.
- Fail gracefully when frames are missing or camera stream ends.
- Release resources reliably (capture + windows).

ASSETS NEEDED:
- Optional test video file: assets/videos/hand_gestures.mp4
- If no video is provided, use a webcam.
"""

from dataclasses import dataclass
from typing import Any

@dataclass
class HandTrackingConfig:
    max_num_hands: int = 2
    min_detection_confidence: float = 0.65
    min_tracking_confidence: float = 0.60


class HandTrackingModule:
    def __init__(self, config: HandTrackingConfig) -> None:
        self.config = config
        # TODO(student): Initialize MediaPipe Hands resources here.
        # Hint: Keep detector state on self so it can be reused per frame.
        raise NotImplementedError("Implement tracker initialization")

    def process_frame(self, frame_bgr: Any) -> dict[str, Any]:
        # TODO(student):
        # 1) Convert frame to RGB.
        # 2) Run hand inference.
        # 3) Return a structured dictionary with hand landmarks and handedness.
        raise NotImplementedError("Implement frame processing")

    def draw_landmarks(self, frame_bgr: Any, result: Any) -> Any:
        # TODO(student): Draw landmarks and connections for each detected hand.
        # Hint: Display label left/right near wrist landmark.
        raise NotImplementedError("Implement landmark rendering")


def open_capture(path: str | None = None) -> Any:
    # TODO(student): Open file capture when path is provided, else webcam capture.
    raise NotImplementedError("Implement capture opening")


def main() -> None:
    # TODO(student):
    # 1) Create capture source (webcam or assets/videos/hand_gestures.mp4).
    # 2) Initialize HandTrackingModule.
    # 3) Process each frame and draw landmarks + hand count.
    # 4) Exit on 'q' and release resources.
    raise NotImplementedError("Implement exercise runner")


if __name__ == "__main__":
    main()
