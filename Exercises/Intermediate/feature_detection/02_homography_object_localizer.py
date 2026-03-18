"""
Exercise Goal:
Estimate a homography from feature matches to localize a planar object in a scene.

Builds Toward:
An AR marker/object anchoring component for overlaying graphics on known surfaces.

ASSETS NEEDED:
- Planar object image: assets/images/poster_query.jpg
- Scene image containing that object: assets/images/poster_scene.jpg
"""

from pathlib import Path

import numpy as np


MIN_MATCHES = 15


def load_gray(path: str) -> np.ndarray:
    # TODO(student): Load grayscale image and validate path.
    raise NotImplementedError("Implement grayscale loader")


def get_orb_matches(
    query: np.ndarray, scene: np.ndarray
) -> tuple[list, list, list]:
    # TODO(student):
    # 1) Detect ORB keypoints/descriptors in query and scene.
    # 2) Match descriptors with k-NN.
    # 3) Apply ratio test and return good matches.
    raise NotImplementedError("Implement ORB matching")


def estimate_homography(
    kp_query: list,
    kp_scene: list,
    matches: list,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    # TODO(student):
    # 1) Stop early if matches < MIN_MATCHES.
    # 2) Build source/destination point arrays from matched keypoints.
    # 3) Estimate homography with RANSAC and return (H, mask).
    raise NotImplementedError("Implement homography estimation")


def draw_localization(
    query_gray: np.ndarray,
    scene_gray: np.ndarray,
    homography: np.ndarray,
) -> np.ndarray:
    # TODO(student):
    # 1) Convert scene to BGR for colored drawing.
    # 2) Project query image corners using homography.
    # 3) Draw projected polygon onto scene and return visualization.
    raise NotImplementedError("Implement localization drawing")


def main() -> None:
    # TODO(student):
    # 1) Load query + scene images.
    # 2) Extract matches and estimate homography.
    # 3) Handle "not enough matches" case cleanly.
    # 4) Draw localization polygon and inlier count text.
    # 5) Show final output window and close resources.
    query_path = Path("assets/images/poster_query.jpg")
    scene_path = Path("assets/images/poster_scene.jpg")
    _ = (query_path, scene_path)  # Replace after implementation.
    raise NotImplementedError("Implement exercise runner")


if __name__ == "__main__":
    main()
