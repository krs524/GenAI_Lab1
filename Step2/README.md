# Step 2: YOLO11 Fine-Tuning on a Custom Dataset

## Overview

In Step 1, the pretrained YOLO11n model identified a hanger as *scissors*. In Step 2, I fine-tuned YOLO11s on a custom hanger dataset to see whether training on labeled examples would improve detection. I then evaluated the model and tested it on the original Step 1 hanger Image.

## Dataset and Training

I prepared **50 hanger images** in Roboflow (`lab1-dataset`, version 2), with bounding-box annotations for the `hanger` class.

| Split | Images |
|---|---:|
| Training | 30 |
| Validation | 10 |
| Test | 10 |

| Setting | Value |
|---|---|
| Starting model | `yolo11s.pt` (pretrained) |
| Epochs | 10 |
| Image size | 640 |
| Prediction confidence threshold | 0.25 |
| Environment | Google Colab with GPU |

## How to Run

Step 2 includes two notebooks:

- **Main fine-tuning notebook:** `train_yolo11_object_detection_on_custom_dataset.ipynb` trains YOLO11s and generates the fine-tuned weights and evaluation outputs.
- **Saved-model evaluation notebook:** `Object_detection_with_saved_train_yolo11_on_custom_dataset .ipynb` downloads the saved weights from GitHub and evaluates the trained model without repeating training.

**Main fine-tuning workflow**

1. Open the main fine-tuning notebook in Google Colab and enable a GPU runtime.
2. In **Colab Secrets**, configure `ROBOFLOW_API_KEY` (with access to the dataset) and `GITHUB_TOKEN` (for GitHub downloads).
3. Run the setup and dataset-download cells. Check that `data.yaml` lists the `hanger` class.
4. Run the training, validation, and test-prediction cells. Outputs are saved under `runs/detect/`.
5. To compare the results before and after fine-tuning, use the notebook's GitHub download code to retrieve `Step1/test_images/Hanger.jpg`. Run the final prediction cell to test the fine-tuned model on the same image and compare it with the YOLO11n result from Step 1. No manual image upload is required.

**Saved-model evaluation workflow**

Open Saved-model evaluation notebook in Colab, configure the same two secrets, and run its cells in order. It downloads the Roboflow dataset and `Step2/models/best.pt` from GitHub, validates the saved model, predicts on the test images, and tests the original hanger image all without retraining.

**Run directory:** Training results normally appear under `runs/detect/train/` in a fresh runtime; later runs may use `train2`, `train3`, etc. Ensure validation and prediction cells reference the correct `weights/best.pt` file. The optional Roboflow deployment section is not required for this experiment.

## Results

The saved fine-tuned model produced the following results on 10 validation images containing 12 annotated hangers:

| Metric | Result |
|---|---:|
| Precision | 0.944 |
| Recall | 0.500 |
| mAP@50 | 0.674 |
| mAP@50–95 | 0.455 |

On the 10 held-out test images, the model detected at least one hanger in **7 images**; the other **3** produced no detections. This is an image-level observation, not an overall accuracy score.

| Model | Prediction on original hanger image | Confidence |
|---|---|---:|
| Pretrained YOLO11n | Scissors | 0.38 |
| Fine-tuned YOLO11s | Hanger | ~0.35 |

## Observations and Limitations

Fine-tuning improved hanger recognition in the original test photograph. However, the recall of 0.500 and missed detections in several test images indicated that performance was still limited.

With only 30 training images, the model had relatively few examples covering different hanger shapes, positions, lighting conditions, and backgrounds. This highlighted the importance of training-data quantity, quality, variety, and accurate annotations.

The baseline experiment used YOLO11n, whereas fine-tuning used YOLO11s. Therefore, the before-and-after comparison does not isolate the effect of fine-tuning alone.

**Note:** The notebooks use temporary Colab storage. Saved model weights (`best.pt`) and important outputs, including `results.png`, `confusion_matrix.png`, and prediction images, should be preserved outside the runtime.

## Security

The Roboflow API key and GitHub personal access token must be stored in Colab Secrets as `ROBOFLOW_API_KEY` and `GITHUB_TOKEN`, respectively. Neither should be written directly into notebook code or committed to GitHub.
