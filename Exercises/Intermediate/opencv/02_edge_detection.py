"""
Exercise Goal:
Implement a modular edge detection pipeline with configurable preprocessing and thresholding.

Builds Toward:
A lane/contour extraction block that can be plugged into robotics and inspection systems.

ASSETS NEEDED:
- One road or industrial image, for example: assets/images/road_scene.jpg
"""

from dataclasses import dataclass

import numpy as np


@dataclass
class EdgeConfig:
    blur_kernel: int = 5
    sigma: float = 0.33


class EdgeDetectionPipeline:
    def __init__(self, config: EdgeConfig) -> None:
        self.config = config

    def preprocess(self, image_bgr: np.ndarray) -> np.ndarray:
        # TODO(student): Convert BGR to grayscale and apply denoising/blur.
        # Hint: Ensure blur kernel is odd; validate config values.
        raise NotImplementedError("Implement preprocessing")

    def auto_canny(self, gray_blurred: np.ndarray) -> np.ndarray:
        # TODO(student): Compute dynamic Canny thresholds.
        # Hint: Use median-based thresholding controlled by sigma.
        raise NotImplementedError("Implement Canny thresholding")

    def postprocess(self, edges: np.ndarray) -> np.ndarray:
        # TODO(student): Add morphology to reduce noise and bridge broken edges.
        raise NotImplementedError("Implement edge cleanup")

    def run(self, image_bgr: np.ndarray) -> dict[str, np.ndarray]:
        # TODO(student): Execute pipeline stages and build overlay visualization.
        # Hint: Return keys: smooth, edges, cleaned, overlay
        raise NotImplementedError("Implement pipeline execution")


def load_image(image_path: str) -> np.ndarray:
    # TODO(student): Load image via OpenCV and validate result.
    raise NotImplementedError("Implement image loader")


def main() -> None:
    # TODO(student):
    # 1) Load assets/images/road_scene.jpg
    # 2) Instantiate config + pipeline
    # 3) Run pipeline and show all result windows
    # 4) Wait for key press and close windows
    raise NotImplementedError("Implement exercise runner")


if __name__ == "__main__":
    main()
