import cv2
import pytesseract
import numpy as np
import textwrap
import pyttsx3
# Initialize webcam
url = "C:\\Users\\Sivaranjani\\OneDrive\\Desktop\\SVAG\\Untitled video - Made with Clipchamp (5).mp4"
cap = cv2.VideoCapture(url)
text_speech=pyttsx3.init()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     # Preprocess image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + 
                          cv2.THRESH_OTSU)[1]
    # Use pytesseract to detect and extract text
    text = pytesseract.image_to_string(thresh)
    if len(text)!=0:
        print(text)#extracted text
    # Save the final result to a text file
    with open("C:\\Users\\Sivaranjani\\OneDrive\\Desktop\\SVAG\\text_detection.txt", "w+")as f:
        f.write(text)
        
    # Draw a border around the text and display the extracted text
    imgH, imgW,_ = frame.shape
    x1,y1,w1,h1=0,0,imgH,imgW  
    imgbox = pytesseract.image_to_boxes(thresh)
    
    for boxes in imgbox.splitlines():
        boxes=boxes.split(' ')
        x,y,w,h=int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
       # print(x,y,w,h)
        cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,225,0),2)  
        
    #wrap and display the extracted text in window
    wrapped_text = textwrap.wrap(text, width=50)
    x, y = x1,y1
    font_size = 0.8
    font_thickness = 2
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

        gap = textsize[1] + 10

        y = int((frame.shape[0] + textsize[1])/2 ) + i * gap
        x = int((frame.shape[1] - textsize[0])/2 )

        cv2.putText(frame, line, (x, y),cv2.FONT_HERSHEY_SIMPLEX ,
                    font_size, 
                    (0,0,225), 
                    font_thickness, 
                    lineType = cv2.LINE_AA)
        font = cv2.FONT_HERSHEY_SIMPLEX

    # Show the frame in a window
    cv2.imshow("Webcam", frame)
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# Release webcam and close the window
cap.release() 
cv2.destroyAllWindows()
f = open("C:\\Users\\Sivaranjani\\OneDrive\\Desktop\\SVAG\\text_detection.txt", "r")
text=f.read()
print(text)

text_speech.say(text)
text_speech.runAndWait()
