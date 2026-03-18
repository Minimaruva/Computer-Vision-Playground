"""
Exercise Goal:
Build a reusable image filtering module that applies multiple filter variants to one input image.

Builds Toward:
A preprocessing stage that can plug into tracking, OCR, and detection pipelines.

Module Architecture:
1) load_image() handles file I/O and validation.
2) build_filter_bank() defines a registry of filter functions.
3) apply_clahe_on_luma() implements one advanced contrast module.
4) render_filter_grid() visualizes outputs in a consistent layout.
5) main() orchestrates pipeline execution.

Standard Practices:
- Keep each filter stateless and pure (input frame -> output frame).
- Preserve color space assumptions explicitly (BGR, LAB, grayscale).
- Validate image load paths early with clear errors.
- Keep visualization separate from algorithmic transformation logic.

ASSETS NEEDED:
- One sample image file, for example: assets/images/city_street.jpg
"""

from typing import Callable

import numpy as np


def load_image(image_path: str) -> np.ndarray:
    """Load an image from disk and validate it exists."""
    # TODO(student): Use cv2.imread and raise FileNotFoundError on failure.
    raise NotImplementedError("Implement image loading")


def build_filter_bank() -> dict[str, Callable[[np.ndarray], np.ndarray]]:
    """Create a dictionary of named filters."""
    # TODO(student): Add at least 4 filters.
    # Hint: Include original/pass-through, blur, denoise, and contrast enhancement.
    raise NotImplementedError("Implement filter bank")


def apply_clahe_on_luma(image_bgr: np.ndarray) -> np.ndarray:
    """Apply CLAHE on the luminance channel while preserving color."""
    # TODO(student): Convert BGR -> LAB, apply CLAHE on L channel, merge back.
    # Hint: Expose clip limit and tile size as tunable values.
    raise NotImplementedError("Implement CLAHE filter")


def render_filter_grid(
    image_bgr: np.ndarray,
    filters: dict[str, Callable[[np.ndarray], np.ndarray]],
) -> np.ndarray:
    """Apply all filters and compose a labeled preview grid."""
    # TODO(student): Apply each filter safely and label each panel with the filter name.
    # Hint: Resize each preview to a fixed shape before stacking.
    raise NotImplementedError("Implement filter grid rendering")


def main() -> None:
    # TODO(student):
    # 1) Load assets/images/city_street.jpg
    # 2) Build your filter bank
    # 3) Render and show filter grid
    # 4) Wait for key press and close windows
    raise NotImplementedError("Implement exercise runner")


if __name__ == "__main__":
    main()
