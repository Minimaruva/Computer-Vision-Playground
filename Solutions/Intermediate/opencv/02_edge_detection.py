"""
Exercise Goal:
Implement a modular edge detection pipeline with configurable preprocessing and thresholding.

Builds Toward:
A lane/contour extraction block that can be plugged into robotics and inspection systems.

ASSETS NEEDED:
- One road or industrial image, for example: assets/images/road_scene.jpg
"""

from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np


@dataclass
class EdgeConfig:
    blur_kernel: int = 5
    sigma: float = 0.33


class EdgeDetectionPipeline:
    def __init__(self, config: EdgeConfig) -> None:
        self.config = config

    def preprocess(self, image_bgr: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        return cv2.GaussianBlur(gray, (self.config.blur_kernel, self.config.blur_kernel), 0)

    def auto_canny(self, gray_blurred: np.ndarray) -> np.ndarray:
        # TODO(student): Replace this with your own threshold strategy.
        # Hint: Try median intensity +- sigma scaling.
        v = float(np.median(gray_blurred))
        lower = int(max(0, (1.0 - self.config.sigma) * v))
        upper = int(min(255, (1.0 + self.config.sigma) * v))
        return cv2.Canny(gray_blurred, lower, upper)

    def postprocess(self, edges: np.ndarray) -> np.ndarray:
        # TODO(student): Add morphology (open/close) to suppress noise speckles.
        return edges

    def run(self, image_bgr: np.ndarray) -> dict[str, np.ndarray]:
        smooth = self.preprocess(image_bgr)
        edges = self.auto_canny(smooth)
        cleaned = self.postprocess(edges)

        overlay = image_bgr.copy()
        overlay[cleaned > 0] = (0, 255, 255)

        return {
            "smooth": smooth,
            "edges": edges,
            "cleaned": cleaned,
            "overlay": overlay,
        }


def load_image(image_path: str) -> np.ndarray:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")
    return image


def main() -> None:
    image = load_image(str(Path("assets/images/road_scene.jpg")))
    pipeline = EdgeDetectionPipeline(config=EdgeConfig())
    result = pipeline.run(image)

    cv2.imshow("Smooth", result["smooth"])
    cv2.imshow("Edges", result["edges"])
    cv2.imshow("Cleaned", result["cleaned"])
    cv2.imshow("Overlay", result["overlay"])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
