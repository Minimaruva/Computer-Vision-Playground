"""
Exercise Goal:
Build a reusable image filtering module that applies multiple filter variants to the same frame.

Builds Toward:
A photo/video preprocessing service for a larger real-time vision pipeline (tracking, detection, OCR).

ASSETS NEEDED:
- One sample image file, for example: assets/images/city_street.jpg
"""

from pathlib import Path

import cv2
import numpy as np


def load_image(image_path: str) -> np.ndarray:
    """Load an image and fail fast if the path is invalid."""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")
    return image


def build_filter_bank() -> dict[str, callable]:
    """Return named filter functions that each map BGR image -> BGR image."""
    # TODO(student): Add 2-3 more filters (for example bilateral, sharpen, emboss).
    # Hint: Keep signatures consistent so each filter can be called in a loop.
    return {
        "original": lambda img: img,
        "gaussian_blur": lambda img: cv2.GaussianBlur(img, (7, 7), 1.5),
        "median_blur": lambda img: cv2.medianBlur(img, 5),
        "clahe_luma": apply_clahe_on_luma,
    }


def apply_clahe_on_luma(image_bgr: np.ndarray) -> np.ndarray:
    """Enhance local contrast while preserving color balance."""
    lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # TODO(student): Tune clipLimit and tileGridSize for your chosen dataset.
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l_enhanced = clahe.apply(l)

    merged = cv2.merge([l_enhanced, a, b])
    return cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)


def render_filter_grid(image_bgr: np.ndarray, filters: dict[str, callable]) -> np.ndarray:
    """Apply all filters and compose a labeled 2-column preview grid."""
    previews: list[np.ndarray] = []

    for name, filter_fn in filters.items():
        # TODO(student): Add error handling that skips failed filters but logs why.
        filtered = filter_fn(image_bgr)
        labeled = filtered.copy()
        cv2.putText(
            labeled,
            name,
            (12, 28),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )
        previews.append(labeled)

    # Hint: Keep output dimensions uniform before stacking.
    target_h, target_w = 360, 640
    resized = [cv2.resize(p, (target_w, target_h)) for p in previews]

    rows = []
    for i in range(0, len(resized), 2):
        left = resized[i]
        right = resized[i + 1] if i + 1 < len(resized) else np.zeros_like(left)
        rows.append(np.hstack([left, right]))

    return np.vstack(rows)


def main() -> None:
    default_image = Path("assets/images/city_street.jpg")
    image = load_image(str(default_image))

    filter_bank = build_filter_bank()
    grid = render_filter_grid(image, filter_bank)

    cv2.imshow("Intermediate: Image Filter Bank", grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
