import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
import torch
import cv2
import numpy as np

# load yolov5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# detect from webcam
def detect_from_webcam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        results = model(frame)
        rendered_img = np.array(results.render()[0])
        cv2.imshow('frame', rendered_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# detect objects
def detect_objects(frame):
    image = cv2.imread(frame)
    results = model(image)
    results.show()

choice = input("Choose detection method (webcam/image): ")
if choice == "webcam":
    detect_from_webcam()
elif choice == "image":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image = input("Enter image path: ")
    detect_objects(os.path.join(base_dir, image))
else:
    print("Invalid choice")