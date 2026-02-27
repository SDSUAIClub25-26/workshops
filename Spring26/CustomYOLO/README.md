## Spring '26 Computer Vision Workshop - Training YOLO26 on a Custom Dataset!

### Objectives

This will be our 2nd workshop of the semester, this time focusing on Computer Vision models! Many of you may have heard of YOLO (You Only Look Once), which is a state-of-the-art real-time object detection model. Today, we will be trying out their latest model, YOLO26, which was released about a month ago and fine-tuning it on our own dataset to detect school supplies. We will be training it in Google Colab and then deploying it locally and testing out inference with our cameras.

### Prerequisites:
- Google Colab
- Google Drive
- Roboflow School Supplies Dataset (in `datasets` repo)
- VS Code & Python (live demo)

### Python Dependencies (for running locally):
- Ultralytics
- python-opencv
- [torch / torchvision](https://pytorch.org/get-started/locally/)

### Setup

1. Clone the workshops repo

`git clone https://github.com/SDSUAIClub25-26/workshops.git`

2. Go to the workshop folder

`cd Spring26/CustomYOLO`

3. Create a virtual environment

`python -m venv <your-name>` 

`<your-name>\Scripts\Activate.ps1` (Windows) or `source <your-name>/bin/activate` (MacOS/Linux)

4. Install dependencies

`pip install -r requirements.txt`

5. Run inference!

- Image Input:
`python yolo_detect.py --model my_model.pt --source image --path <path to img>`

- Video Input:
`python yolo_detect.py --model my_model.pt --source video --path <path to video>`

- Webcam:
`python yolo_detect.py --model my_model.pt --source webcam`

Tip: Make sure your model files are imported into your environment (best.pt in Colab). You can also add the .onnx file which is specifically meant for faster inference.
