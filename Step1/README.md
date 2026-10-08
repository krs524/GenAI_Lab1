# Step 1: Pretrained YOLO11 Object Detection

## Overview

In step 1, I tested a pretrained YOLO11 model on everyday objects using my laptop camera. I used the provided webcam object recognition project and tested the model on few captured images to observe how well it detected different objects.

## Files

- `main.py` - Runs real-time object detection using the laptop webcam.
- `test_images.py` - Runs detection on saved images and prints the predicted labels and confidence scores.
- `models/` - Contains the pretrained YOLO11 model.
- `test_images/` - Contains the original images captured using my laptop camera.
- `results/` - Contains the prediction images with bounding boxes, labels, and confidence scores.

## How to Run

This experiment was performed on a Windows laptop using Python, OpenCV, and Ultralytics.

**1. Install the required libraries**

Open Command Prompt in the `Step1` folder and run:

```bash
python -m pip install ultralytics opencv-python
```

**2. Run live webcam detection**

```bash
python main.py
```

This runs real-time object detection using the laptop webcam with a confidence threshold of `0.50`. Press `q` to close the webcam window.

**3. Run detection on saved images**

```bash
python test_images.py
```

This processes the images in `test_images/` using a confidence threshold of `0.25`. The script prints the predicted labels and confidence scores and saves the annotated images under `runs/detect/`.

The original webcam code uses a threshold of `0.50`, while `0.25` was used for test-image predictions.

## Results

| Test Image | YOLO11 Predictions | Observation |
|---|---|---|
| Teddy.jpg | teddy bear (0.85) | The teddy bear was correctly detected. |
| Hanger.jpg | person (0.78), scissors (0.38) | The hanger was incorrectly labeled as scissors. The visible hand was detected as a person. |
| Ruler.jpg | person (0.67) | The ruler was not recognized. Instead, the model detected the visible hand as a person. |
| Diary.jpg | umbrella (0.85), person (0.42, 0.29) | The diary was incorrectly labeled as an umbrella, along with additional person detections. |
| scissors.jpg | person (0.86) | The scissors were not recognized. The model detected the hand holding them as a person. |
| lamp.jpg | No detections | The model did not detect the lamp or draw any bounding box. |

The original images are available in `test_images/`, and their annotated predictions are available in `results/`.

## Observations

The pretrained YOLO11 model correctly detected the teddy bear but struggled with several other objects. It incorrectly labeled the hanger as scissors and the diary as an umbrella. The ruler and scissors were not recognized, while the lamp received no detections at all.

Some images included visible hands or arms, which may explain the person-related predictions. The lamp was white against a light-colored background, which may have made detection more difficult, although the exact reason for the missed detection is uncertain.

Based on these results, I selected the hanger for further fine-tuning in Step 2.

## Reference

Given GitHub repository in assignment:

https://github.com/valeriouberti/webcam-object-recognition
