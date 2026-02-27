## Spring 26 Computer Vision Workshop - Training YOLO26 on a Custom Dataset!

### Objectives

### Dependencies:
- Ultralytics, python-opencv
- torch / torchvision (from website)

# Setup

python -m venv venv
venv\Scripts\Activate.ps1 # for windows
pip install dependencies

**make sure model files are imported into the running instance (my_model.onnx, my_model.pt)**

python yolo_detect.py --model --source video/image/webcam --path <path to video/img if needed>