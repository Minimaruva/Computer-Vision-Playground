"""
Exercise Goal:
Create a reusable ORB-based feature matcher with robust filtering of false matches.

Builds Toward:
A visual localization module for panorama stitching or object retrieval systems.

ASSETS NEEDED:
- Query image: assets/images/book_cover.jpg
- Scene image: assets/images/bookshelf_scene.jpg
"""

from pathlib import Path

import cv2
import numpy as np


def load_grayscale(path: str) -> np.ndarray:
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {path}")
    return image


def detect_and_describe(image_gray: np.ndarray) -> tuple[list[cv2.KeyPoint], np.ndarray]:
    # TODO(student): Tune nfeatures and scaleFactor for your dataset.
    orb = cv2.ORB_create(nfeatures=1200, scaleFactor=1.2, nlevels=8)
    keypoints, descriptors = orb.detectAndCompute(image_gray, None)

    if descriptors is None:
        descriptors = np.empty((0, 32), dtype=np.uint8)

    return keypoints, descriptors


def ratio_test_knn(
    desc_a: np.ndarray, desc_b: np.ndarray, ratio: float = 0.75
) -> list[cv2.DMatch]:
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    knn_matches = matcher.knnMatch(desc_a, desc_b, k=2)

    good_matches: list[cv2.DMatch] = []
    for pair in knn_matches:
        # TODO(student): Guard against malformed match pairs.
        if len(pair) == 2:
            m, n = pair
            if m.distance < ratio * n.distance:
                good_matches.append(m)

    return good_matches


def draw_matches(
    image_a: np.ndarray,
    kp_a: list[cv2.KeyPoint],
    image_b: np.ndarray,
    kp_b: list[cv2.KeyPoint],
    matches: list[cv2.DMatch],
) -> np.ndarray:
    return cv2.drawMatches(
        image_a,
        kp_a,
        image_b,
        kp_b,
        matches,
        None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
    )


def main() -> None:
    query = load_grayscale(str(Path("assets/images/book_cover.jpg")))
    scene = load_grayscale(str(Path("assets/images/bookshelf_scene.jpg")))

    kp_q, desc_q = detect_and_describe(query)
    kp_s, desc_s = detect_and_describe(scene)

    good = ratio_test_knn(desc_q, desc_s, ratio=0.72)
    matched = draw_matches(query, kp_q, scene, kp_s, good)

    cv2.putText(
        matched,
        f"Good matches: {len(good)}",
        (16, 32),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

    cv2.imshow("ORB Feature Matching", matched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
