# GenAI_Lab1

## Overview

This lab explores object detection using YOLO11 and YOLOE through three experiments: evaluating a pretrained YOLO11 model, fine-tuning YOLO11 on a custom dataset, and exploring YOLOE's open-vocabulary object detection capabilities.

The experiments focus on understanding how these models work, evaluating their detection performance, and exploring the differences between standard object detection, model fine-tuning, and prompt-based detection.

## Experiments

| Experiment | Description | Documentation |
|---|---|---|
| **Step 1: Pretrained YOLO11** | Evaluated YOLO11n using a live webcam feed and six object images captured with laptop's camera to examin detection performance. | [Step 1 README](Step1/README.md) |
| **Step 2: YOLO11 Fine-Tuning** | Fine-tuned YOLO11s on a custom hanger dataset and compared its predictions with those from Step 1. | [Step 2 README](Step2/README.md) |
| **Step 3: YOLOE Open-Vocabulary Detection** | Explored text and visual prompting for zero-shot object detection on images and videos using pretrained YOLOE. | [Step 3 README](Step3/README.md) |

## Repository Structure

```text
GenAI_Lab1/
├── README.md
├── Step1/
│   ├── models/
│   ├── results/
│   ├── test_images/
│   ├── README.md
│   ├── main.py
│   └── test_images.py
├── Step2/
│   ├── models/
│   ├── results/
│   ├── README.md
│   ├── train_yolo11_object_detection_on_custom_dataset.ipynb
│   └── Object_detection_with_saved_train_yolo11_on_custom_dataset .ipynb
└── Step3/
    ├── results/
    ├── README.md
    └── zero_shot_object_detection_and_segmentation_with_yoloe.ipynb
```

Each experiment folder contains its implementation and README, while the `models/`, `test_images/`, and `results/` folders store the relevant weights, input images, and experimental outputs.

## Getting Started

1. Open the folder for the experiment you want to reproduce.
2. Follow its README for the required setup, dependencies, and execution instructions.
3. Run the corresponding scripts or notebooks in the specified environment. Steps 2 and 3 use Google Colab.
4. Configure any required API keys or access tokens securely, as described in the individual experiment READMEs.

## Key Findings

- **Step 1:** The pretrained YOLO11n model successfully detected some objects but misclassified or missed others, highlighting limitations in recognizing certain objects.
- **Step 2:** Fine-tuning enabled YOLO11s to correctly identify the original hanger image, although the validation results and missed test detections showed that performance remained limited.
- **Step 3:** YOLOE detected objects through text and visual prompts without  fine-tuning, demonstrating the flexibility of open-vocabulary detection while also producing some missed detections and false positives.
