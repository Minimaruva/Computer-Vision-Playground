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

import cv2
import numpy as np


MIN_MATCHES = 15


def load_gray(path: str) -> np.ndarray:
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {path}")
    return image


def get_orb_matches(
    query: np.ndarray, scene: np.ndarray
) -> tuple[list[cv2.KeyPoint], list[cv2.KeyPoint], list[cv2.DMatch]]:
    orb = cv2.ORB_create(nfeatures=1500)
    kp_q, desc_q = orb.detectAndCompute(query, None)
    kp_s, desc_s = orb.detectAndCompute(scene, None)

    if desc_q is None or desc_s is None:
        return kp_q or [], kp_s or [], []

    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(desc_q, desc_s, k=2)

    good: list[cv2.DMatch] = []
    for pair in matches:
        if len(pair) == 2 and pair[0].distance < 0.75 * pair[1].distance:
            good.append(pair[0])

    return kp_q, kp_s, good


def estimate_homography(
    kp_query: list[cv2.KeyPoint],
    kp_scene: list[cv2.KeyPoint],
    matches: list[cv2.DMatch],
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if len(matches) < MIN_MATCHES:
        return None, None

    # TODO(student): Try RANSAC reprojection thresholds (2.0, 3.0, 5.0).
    src_pts = np.float32([kp_query[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp_scene[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    return cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)


def draw_localization(
    query_gray: np.ndarray,
    scene_gray: np.ndarray,
    homography: np.ndarray,
) -> np.ndarray:
    scene_bgr = cv2.cvtColor(scene_gray, cv2.COLOR_GRAY2BGR)
    h, w = query_gray.shape

    corners = np.float32([[0, 0], [w, 0], [w, h], [0, h]]).reshape(-1, 1, 2)
    projected = cv2.perspectiveTransform(corners, homography)

    cv2.polylines(scene_bgr, [np.int32(projected)], True, (0, 255, 0), 3, cv2.LINE_AA)
    return scene_bgr


def main() -> None:
    query = load_gray(str(Path("assets/images/poster_query.jpg")))
    scene = load_gray(str(Path("assets/images/poster_scene.jpg")))

    kp_q, kp_s, good = get_orb_matches(query, scene)
    homography, mask = estimate_homography(kp_q, kp_s, good)

    if homography is None:
        print(f"Not enough matches ({len(good)}). Need at least {MIN_MATCHES}.")
        return

    localized = draw_localization(query, scene, homography)

    inliers = int(mask.sum()) if mask is not None else 0
    cv2.putText(
        localized,
        f"Inliers: {inliers}/{len(good)}",
        (16, 32),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

    cv2.imshow("Homography Localization", localized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
