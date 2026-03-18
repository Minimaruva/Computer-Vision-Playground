"""
Exercise Goal:
Implement a centroid-based multi-object tracker with ID persistence across frames.

Builds Toward:
A real-time people/vehicle analytics pipeline where tracked IDs feed counting and behavior modules.

Module Architecture:
1) TrackedObject stores per-object state (id, centroid, age/missing, trail).
2) CentroidTracker manages lifecycle (register, match, deregister).
3) fake_detector() enables quick logic testing without a detector model.
4) draw_tracks() handles visualization only.
5) main() coordinates frame loop and tracker updates.

API-Level Notes:
- update(detections_xyxy) should be the only public tracking API.
- Input format should stay stable: list of (x1, y1, x2, y2) boxes.
- Output should be deterministic mapping from object_id to TrackedObject.

Standard Practices:
- Keep matching threshold explicit (max_distance).
- Separate data association from drawing.
- Increment missing counts for unmatched tracks and remove stale tracks.
- Prefer predictable, testable update rules over hidden side effects.

ASSETS NEEDED:
- Detection source video with moving objects: assets/videos/pedestrians.mp4
- Optional detection file for offline testing: assets/annotations/pedestrians_detections.json
"""

from dataclasses import dataclass, field

@dataclass
class TrackedObject:
    object_id: int
    centroid: tuple[int, int]
    missing_frames: int = 0
    trail: list[tuple[int, int]] = field(default_factory=list)


class CentroidTracker:
    def __init__(self, max_missing: int = 10, max_distance: float = 80.0) -> None:
        self.max_missing = max_missing
        self.max_distance = max_distance
        self.next_id = 1
        self.objects: dict[int, TrackedObject] = {}

    def _register(self, centroid: tuple[int, int]) -> None:
        # TODO(student): Create a TrackedObject and insert into self.objects.
        # Hint: Initialize trail with first centroid.
        raise NotImplementedError("Implement track registration")

    def _deregister_missing(self) -> None:
        # TODO(student): Remove tracks that exceed max_missing frames.
        raise NotImplementedError("Implement track cleanup")

    def update(self, detections_xyxy: list[tuple[int, int, int, int]]) -> dict[int, TrackedObject]:
        # TODO(student):
        # 1) Convert detection boxes to centroids.
        # 2) Handle empty tracker / empty detections cases.
        # TODO(student): Implement matching between existing objects and new centroids.
        # Hint 1: Build a distance matrix between object centroids and detections.
        # Hint 2: Greedily match smallest distances under max_distance.
        # Hint 3: Unmatched detections should register new IDs.
        # Hint 4: Unmatched existing tracks should increment missing_frames.
        raise NotImplementedError("Implement tracker update")


def fake_detector(frame_idx: int) -> list[tuple[int, int, int, int]]:
    # TODO(student): Generate synthetic detections for early testing.
    # Hint: Move boxes over time so matching behavior is visible.
    raise NotImplementedError("Implement synthetic detector")


def draw_tracks(frame, tracks: dict[int, TrackedObject]):
    # TODO(student): Draw centroid, ID label, and motion trail for each active track.
    raise NotImplementedError("Implement track visualization")


def main() -> None:
    # TODO(student):
    # 1) Create tracker instance.
    # 2) Build frame loop using synthetic detections first, then real detector/video.
    # 3) Update tracks each frame and append centroid history.
    # 4) Draw detections + tracks and display output.
    # 5) Exit loop on key press and clean up windows/resources.
    raise NotImplementedError("Implement exercise runner")


if __name__ == "__main__":
    main()
