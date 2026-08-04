# 4-Minute Video Walkthrough Script — PS3: Advanced Object Tracking and Detection

Group: _<fill in>_ · File to submit: `CV_assignment2_10_3.ipynb` (already in `notebooks/`)
Target length: **4:00** total, split across **5 speakers** (~40–50s each). Read the notebook
section named in "[Show]" while speaking that part — no need to scroll ahead, the sections
are in the same top-to-bottom order as the script.

Once recorded, add the video link to the group's row in the shared Google Sheet (see the
assignment PDF) — that's a manual step, not something this file does for you.

---

## Speaker 1 — Introduction & Problem Statement (0:00–0:35, ~35s)

**[Show: notebook title cell / Section intro]**

> "Hi, we're presenting Problem Statement 3: Advanced Object Tracking and Detection in
> Video Streams. The goal is to detect and track multiple objects across a video with
> stable identities, even as they move, overlap, or get occluded. We built this using a
> Faster R-CNN detector fine-tuned for pedestrian detection, combined with a SORT-style
> tracker that adds a temporal consistency check and adaptive motion-based tracking. We
> evaluated it on a real MOT17 sequence — a busy street scene with 83 pedestrians across
> over a thousand frames."

*(~75 words)*

---

## Speaker 2 — Data Preprocessing (0:35–1:15, ~40s)

**[Show: Section 1. Data Preprocessing — frame loading + augmented sample image]**

> "For data, we work with the MOT17-04 sequence: a static-camera street scene with ground
> truth bounding boxes and identities for every pedestrian in every frame. We extract
> frames, normalize them to match what Faster R-CNN expects, and — for the training
> split only — apply augmentation: random horizontal flips and color jittering, so the
> detector generalizes better instead of memorizing the exact lighting and positions in
> the training frames. You can see here an augmented training sample with its ground
> truth boxes drawn on top."

*(~85 words)*

---

## Speaker 3 — Model Development: Detection (1:15–2:00, ~45s)

**[Show: Section 2.1 — build_model / training loss plot / detector sample output]**

> "For detection, we start from a Faster R-CNN with a ResNet-50 backbone and Feature
> Pyramid Network, pretrained on COCO, and replace its classification head so it fine-tunes
> for our single 'pedestrian' class. We trained for 5 epochs — you can see the loss drops
> steadily from about 0.48 down to 0.20, and it's still trending down at the end, meaning
> more epochs would likely help further. This gave us a mean Average Precision of 0.81 at
> an IoU threshold of 0.5 — here's the detector correctly picking out pedestrians across a
> busy, crowded frame."

*(~100 words)*

---

## Speaker 4 — Model Development: Tracking (2:00–2:50, ~50s)

**[Show: Section 2.2 — tracker code briefly, then run the tracking loop / sample tracked frames]**

> "Detections alone don't give you identities across frames, so on top of that we run a
> SORT-style tracker. Each track has its own Kalman filter that predicts where the object
> should be next frame based on its motion, and we match new detections to existing tracks
> using the Hungarian algorithm on IoU overlap. Two additions make this more robust: a
> temporal consistency check, which only confirms a new identity once it's been matched for
> three consecutive frames — so a single flickering false detection doesn't create a fake
> identity — and adaptive gating, which loosens the matching threshold for faster-moving
> objects, since their predicted position is naturally less certain. Let's run it live —
> here you can see consistent IDs being tracked across the sequence, frame 1 through
> frame 1050."

*(~135 words — trim if running long; the live run itself can absorb a few seconds)*

---

## Speaker 5 — Evaluation & Conclusion (2:50–3:40, ~50s)

**[Show: Section 3 — MOTA/IDF1 output, baseline comparison table, FPS cell, then Conclusion]**

> "For evaluation, we used standard multi-object tracking metrics via the motmetrics
> library: MOTA of 0.805 and IDF1 of 0.823. To actually prove our additions helped, we
> compared against a naive baseline tracker with no Kalman filter and no temporal
> consistency check — same detections, same MOTA, but 291 identity switches versus just 52
> for our tracker. That's an 82% reduction in identity switches, which is exactly what
> temporal consistency and motion prediction are supposed to buy you. The detector alone
> runs at about 7.4 frames per second on a Colab GPU — not real-time yet, but a solid
> baseline. Our main takeaway: detection recall in dense, occluded crowds is the biggest
> remaining bottleneck, more than the tracking algorithm itself. Thanks for watching."

*(~130 words)*

---

## Timing check

| Speaker | Section | Target |
|---|---|---|
| 1 | Intro & Problem Statement | 0:00–0:35 |
| 2 | Data Preprocessing | 0:35–1:15 |
| 3 | Detection (Faster R-CNN) | 1:15–2:00 |
| 4 | Tracking (SORT/Kalman) + live run | 2:00–2:50 |
| 5 | Evaluation & Conclusion | 2:50–3:40 |

Leaves ~20s of buffer under the 4:00 cap for transitions between speakers — practice once
with a timer and trim speaker 4/5 first if you're running over, since those have the most
words.
