"""
Exercise Goal:
Implement a centroid-based multi-object tracker with ID persistence across frames.

Builds Toward:
A real-time people/vehicle analytics pipeline where tracked IDs feed counting and behavior modules.

ASSETS NEEDED:
- Detection source video with moving objects: assets/videos/pedestrians.mp4
- Optional detection file for offline testing: assets/annotations/pedestrians_detections.json
"""

from dataclasses import dataclass, field

import cv2
import numpy as np


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
        self.objects[self.next_id] = TrackedObject(
            object_id=self.next_id,
            centroid=centroid,
            missing_frames=0,
            trail=[centroid],
        )
        self.next_id += 1

    def _deregister_missing(self) -> None:
        to_remove = [oid for oid, obj in self.objects.items() if obj.missing_frames > self.max_missing]
        for oid in to_remove:
            del self.objects[oid]

    def update(self, detections_xyxy: list[tuple[int, int, int, int]]) -> dict[int, TrackedObject]:
        centroids = [((x1 + x2) // 2, (y1 + y2) // 2) for x1, y1, x2, y2 in detections_xyxy]

        if len(self.objects) == 0:
            for c in centroids:
                self._register(c)
            return self.objects

        if len(centroids) == 0:
            for obj in self.objects.values():
                obj.missing_frames += 1
            self._deregister_missing()
            return self.objects

        # TODO(student): Implement matching between existing objects and new centroids.
        # Hint 1: Build a distance matrix between object centroids and detections.
        # Hint 2: Greedily match smallest distances under max_distance.
        # Hint 3: Unmatched detections should register new IDs.
        # Hint 4: Unmatched existing tracks should increment missing_frames.

        return self.objects


def fake_detector(frame_idx: int) -> list[tuple[int, int, int, int]]:
    # Simple synthetic detections to help test tracker logic before using a real detector.
    base_x = 40 + frame_idx * 4
    return [
        (base_x, 80, base_x + 40, 150),
        (280 - frame_idx * 2, 180, 320 - frame_idx * 2, 250),
    ]


def draw_tracks(frame: np.ndarray, tracks: dict[int, TrackedObject]) -> np.ndarray:
    for obj in tracks.values():
        cx, cy = obj.centroid
        cv2.circle(frame, (cx, cy), 6, (0, 255, 0), -1)
        cv2.putText(
            frame,
            f"ID {obj.object_id}",
            (cx + 8, cy - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        # Draw motion trail.
        for i in range(1, len(obj.trail)):
            cv2.line(frame, obj.trail[i - 1], obj.trail[i], (0, 180, 255), 2)

    return frame


def main() -> None:
    tracker = CentroidTracker(max_missing=8, max_distance=70.0)

    canvas_h, canvas_w = 360, 480
    for frame_idx in range(60):
        frame = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)
        detections = fake_detector(frame_idx)
        tracks = tracker.update(detections)

        # TODO(student): After matching logic is done, update each track trail here.

        for (x1, y1, x2, y2) in detections:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (100, 100, 255), 2)

        frame = draw_tracks(frame, tracks)
        cv2.imshow("Intermediate: Centroid Tracker", frame)
        if cv2.waitKey(40) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
