"""
Exercise Goal:
Create a reusable ORB-based feature matcher with robust filtering of false matches.

Builds Toward:
A visual localization module for panorama stitching or object retrieval systems.

What Is ORB:
ORB = Oriented FAST and Rotated BRIEF.
- FAST detects keypoints quickly.
- BRIEF generates compact binary descriptors.
- ORB adds orientation handling and ranking to improve robustness and speed.

How It Works Under API:
1) cv2.ORB_create(...) configures detector/descriptor.
2) detectAndCompute(image, None) returns keypoints + descriptors.
3) BFMatcher(...).knnMatch(desc_a, desc_b, k=2) creates candidate pairs.
4) Lowe ratio test keeps distinctive matches and removes ambiguous ones.
5) drawMatches(...) visualizes correspondences.

Module Architecture:
1) load_grayscale() handles input safety.
2) detect_and_describe() extracts features.
3) ratio_test_knn() filters matches.
4) draw_matches() creates visual output.
5) main() orchestrates complete workflow.

Standard Practices:
- Always handle empty descriptor cases.
- Keep ratio threshold configurable (e.g., 0.70 to 0.80).
- Track both match count and inlier quality for better diagnostics.

ASSETS NEEDED:
- Query image: assets/images/book_cover.jpg
- Scene image: assets/images/bookshelf_scene.jpg
"""

from pathlib import Path

import numpy as np


def load_grayscale(path: str) -> np.ndarray:
    # TODO(student): Load grayscale image and raise FileNotFoundError when invalid.
    raise NotImplementedError("Implement grayscale loader")


def detect_and_describe(image_gray: np.ndarray) -> tuple[list, np.ndarray]:
    # TODO(student):
    # 1) Create ORB detector with tunable parameters.
    # 2) Detect keypoints and compute descriptors.
    # 3) Return empty descriptor array when no features are found.
    raise NotImplementedError("Implement ORB detect+describe")


def ratio_test_knn(
    desc_a: np.ndarray,
    desc_b: np.ndarray,
    ratio: float = 0.75,
) -> list:
    # TODO(student):
    # 1) Run k-NN matching with k=2.
    # 2) Apply Lowe's ratio test to reject ambiguous matches.
    # 3) Handle edge cases where descriptors are empty.
    raise NotImplementedError("Implement ratio-test matching")


def draw_matches(
    image_a: np.ndarray,
    kp_a: list,
    image_b: np.ndarray,
    kp_b: list,
    matches: list,
) -> np.ndarray:
    # TODO(student): Visualize only strong matches.
    # Hint: Try draw flags that hide unmatched keypoints for cleaner output.
    raise NotImplementedError("Implement match visualization")


def main() -> None:
    # TODO(student):
    # 1) Load query and scene grayscale images.
    # 2) Detect and describe features in both images.
    # 3) Match descriptors using ratio test.
    # 4) Draw matches and overlay count text.
    # 5) Display result and close windows correctly.
    query_path = Path("assets/images/book_cover.jpg")
    scene_path = Path("assets/images/bookshelf_scene.jpg")
    _ = (query_path, scene_path)  # Replace after implementation.
    raise NotImplementedError("Implement exercise runner")


if __name__ == "__main__":
    main()
