import cv2
from yolov8 import YOLOv8
from playsound import playsound
import pyttsx3
A = ["person","bicycle","car","motorcycle","airplane","bus","train","truck",
"boat","traffic light","fire hydrant","street sign","stop sign","parking meter",
"bench,bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe","hat",
"backpack","umbrella","shoe","eye glasses","handbag","tie","suitcase","frisbee","skis",
"snowboard","sports ball","kite","baseball bat","baseball glove","skateboard","surfboard",
"tennis racket","bottle","plate","wine glass","cup","fork","knife","spoon","bowl","banana","apple",
"sandwich","orange","broccoli","carrot","hot dog","pizza","donut","cake","chair","couch","potted plant",
"bed","mirror","dining table","window","desk","toilet","door","tv","laptop","mouse","remote","keyboard",
"cell phone","microwave","oven","toaster","sink","refrigerator","blender","book","clock",
"vase","scissors","teddy bear","hair drier","toothbrush,hair","brush"]
def speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    
cap = cv2.VideoCapture(0)

lables = []
unique_labels = set() 

model_path = "models/yolov8m.onnx"
yolov8_detector = YOLOv8(model_path, conf_thres=0.5, iou_thres=0.5)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    boxes, scores, class_ids = yolov8_detector(frame)

    combined_img = yolov8_detector.draw_detections(frame)
    cv2.imshow("Detected Objects", combined_img)
    
    for class_id in class_ids:
        
        unique_labels.add(A[class_id])
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
print(unique_labels)
    
i=0
new_sentence = []
for label in unique_labels:
    if i==0:
        new_sentence.append(f"I fonnd a {label}, and , ")
    else:
        new_sentence.append(f"a {label}")
        
    i+=1 
speech(" ".join(new_sentence))
