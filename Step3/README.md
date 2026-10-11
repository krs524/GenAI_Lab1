# Step 3: Zero-Shot Object Detection with YOLOE

## Overview

In Step 3, I studied YOLOE's architecture and workflow and explored its open-vocabulary object detection capabilities. Unlike standard object detectors(YOLO) that recognize a predefined set of classes, YOLOE can detect objects specified through text prompts or visual examples without additional fine-tuning.

I used a pretrained YOLOE model to experiment with both prompting methods on images and videos, observing their detection performance and limitations.

## Model and Experimental Setup

The experiments were conducted in Google Colab using a pretrained YOLOE model.

| Setting | Value |
|---|---|
| Model | `yoloe-v8l-seg.pt` |
| Framework | YOLOE / Ultralytics |
| Prompt types | Text and visual |
| Input types | Images and videos |
| Text-prompt confidence threshold | 0.1 |

Although the model supports segmentation, these experiments focused on object detection, with predictions displayed using bounding boxes and class labels.

## How to Run

1. Open `zero_shot_object_detection_and_segmentation_with_yoloe.ipynb` in Google Colab and enable a GPU runtime.
2. Configure `HF_TOKEN` in **Colab Secrets** as instructed in the notebook for accessing the pretrained model weights.
3. Run the setup cells to install dependencies and download the pretrained YOLOE weights and example images and videos.
4. **Text prompts on images:** Run the prediction cells using text labels such as `dog`, `eye`, `tongue`, `nose`, and `ear`.
5. **Visual prompts on images:** Select bounding boxes for `cap`, `sunglasses`, and `dog` in `dog-3.jpeg`, then use these examples to detect corresponding objects in `dog-8.jpeg`.
6. **Text prompts on video:** Process `suitcases-1280x720.mp4` using the text prompt `suitcase` and save the annotated video.
7. **Visual prompts on video:** Select a croissant using a bounding box in the first frame of `croissant-1280x720.mp4`, then use this visual prompt to detect similar objects in subsequent frames.

Run the notebook cells in order because later sections depend on variables and files created in earlier cells. The example inputs can be replaced by updating the corresponding image or video paths.

## Results

The following observations were recorded across the four experiments:

| Experiment | Input and prompt | Observations |
|---|---|---|
| Text prompt on image | `dog.jpeg` - dog and facial features | Detected the dog, eye, tongue, and nose, but missed the ear |
| Visual prompt on image | `dog-3.jpeg` to `dog-8.jpeg` - cap, sunglasses, dog | Successfully detected the cap and dog in the target image |
| Text prompt on video | Suitcase video - `suitcase` | Detected suitcases across frames, but also misidentified some ordinary boxes as suitcases |
| Visual prompt on video | Croissant video - selected croissant | Detected similar croissants across subsequent video frames |

An additional text-prompt experiment using `dogs tail` was also performed in the notebook.

The annotated video outputs are available in the `results/` folder:

- [Suitcase Detection Result](results/suitcases-1280x720-result.mp4)
- [Croissant Detection Result](results/croissant-1280x720-result.mp4)

Image predictions and sampled video frames can be viewed directly in the notebook.

## Observations and Limitations

YOLOE demonstrated the ability to recognize objects using text and visual prompts without additional training. Text prompting successfully identified several features of the dog, although the ear was missed. Visual prompting also allowed the model to recognize selected objects in a different image.

In the video experiments, the model detected prompted objects across multiple frames. However, some ordinary boxes were incorrectly labeled as suitcases, showing that visually similar objects can still cause false detections.

These experiments represents the flexibility of open-vocabulary detection and the importance of prompt selection and visual context. The evaluation was qualitative, so no quantitative accuracy or inference-speed comparison was performed.

**Note:** The notebook uses temporary Colab storage. Generated outputs should be saved before the runtime resets. The two annotated video results are included in the repository.

## Security

The Hugging Face access token should be stored securely in Colab Secrets as `HF_TOKEN`, rather than written directly into notebook code or committed to GitHub.
