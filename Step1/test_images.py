from ultralytics import YOLO
import os

model = YOLO("./models/yolo11n.pt")

folder = "test_images"

for filename in os.listdir(folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(folder, filename)

        print(f"\nTesting: {filename}")

        results = model.predict(
            source=image_path,
            conf=0.25,
            save=True
        )

        for result in results:
            if len(result.boxes) == 0:
                print("No object detected")
            else:
                for box in result.boxes:
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    label = model.names[class_id]

                    print(
                        f"Detected: {label}, confidence: {confidence:.2f}"
                    )