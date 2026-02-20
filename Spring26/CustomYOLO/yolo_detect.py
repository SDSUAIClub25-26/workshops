from ultralytics import YOLO
import cv2
import argparse

def run_inference_image(model_path, image_path):
    """Run inference on a single image"""

    model = YOLO(model_path, task='detect')
    results = model(image_path)

    for result in results:
        img_with_boxes = result.plot()
        cv2.imshow('Detection results', img_with_boxes)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

def run_inference_video(model_path, video_path):
    """Run inference on a video file"""
    model = YOLO(model_path, task='detect')
    cap = cv2.VideoCapture(video_path)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Run inference
        results = model(frame)
        
        # Display results
        annotated_frame = results[0].plot()
        cv2.imshow('Video Detection', annotated_frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def run_inference_webcam(model_path):
    """Run inference on webcam feed"""
    model = YOLO(model_path, task='detect')
    cap = cv2.VideoCapture(0)  # 0 is default webcam
    
    print("Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Run inference
        results = model(frame, verbose=False)  # verbose=False reduces console output
        
        # Display results
        annotated_frame = results[0].plot()
        cv2.imshow('Webcam Detection', annotated_frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YOLO inference on different sources')
    parser.add_argument('--model', type=str, required=True, help='Path')
    parser.add_argument('--source', type=str, required=True, 
                       help='Source type: "webcam", "image", or "video"')
    parser.add_argument('--path', type=str, default=None, 
                       help='Path to image or video file (not needed for webcam)')

    args = parser.parse_args()

    if args.source == 'webcam':
        run_inference_webcam(args.model)
    elif args.source == 'image':
        if not args.path:
            print('Error: --path required for image inference')
        else:
            run_inference_image(args.model, args.path)
    elif args.source == 'video':
        if not args.path:
            print('Error: --path required for video inference')
        else:
            run_inference_video(args.model, args.path)
    else:
        print("Invalid source. Choose 'webcam', 'image', or 'video'")

    