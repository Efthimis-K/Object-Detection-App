# Object Detection App

A Python application that uses YOLOv5 for object detection in static images.

## Features

- **Static Image Detection**: Analyze objects in saved image files
- **YOLOv5 Model**: Uses the pre-trained YOLOv5s model for accurate object detection
- **Visual Output**: Displays bounding boxes and class labels for detected objects

## Requirements

- Python 3.7+
- PyTorch
- OpenCV (cv2)
- NumPy

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd object-detection-app
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

Alternatively, install manually:
```bash
pip install torch torchvision
pip install opencv-python
pip install numpy
```

3. The YOLOv5 model will be automatically downloaded on first run.

## Usage

Run the main script:
```bash
python object-detection.py
```

The application will prompt you to enter the path to your image file.

## File Structure

```
object-detection-app/
├── object-detection.py   # Main application script
├── requirements.txt      # Python dependencies
├── yolov5s.pt           # Pre-trained YOLOv5 model (auto-downloaded, excluded from git)
├── test.jpg             # Sample test image
├── test_image.jpg       # Another sample image
├── README.md            # This file
└── .gitignore           # Git ignore file
```

## Git Repository Notes

- The `yolov5/` folder is excluded from version control via `.gitignore`
- Large model files (`*.pt`, `*.pth`) are also excluded to keep repository size manageable
- The YOLOv5 model will be automatically downloaded when the application is first run

## Model Information

This application uses the YOLOv5s (small) model, which can detect 80 different object classes including:
- Person, car, truck, bus, motorcycle
- Animals: dog, cat, horse, cow, sheep
- Objects: chair, table, laptop, phone, bottle
- And many more...

## Notes

- The YOLOv5 model is automatically downloaded from PyTorch Hub on first run
- For image detection, provide the relative path to the image file
- The application sets `KMP_DUPLICATE_LIB_OK='TRUE'` to handle potential library conflicts

## Troubleshooting

- For image detection, ensure the image file exists in the correct path
- If you experience performance issues, try closing other applications that might be using the GPU
