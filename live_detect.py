# import the opencv library
import cv2
img=cv2.imread("boy.jpg")
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Define a video capture object
vid = cv2.VideoCapture(0)

while(True):
   
#  # Capture the video frame by frame
   ret, frame = vid.read()

   gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   faces=face_cascade.detectMultiScale(gray,1.1,5)
   #print(faces)
   for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(90,40,50),2)
        

    # Display the resulting frame
   cv2.imshow("frame", frame)
      
#     # Quit Window by Spacebar Key
   if cv2.waitKey(25) == 32:
         break
  
# # After the loop release the cap object
vid.release()

# # Destroy all the windows
cv2.destroyAllWindows()