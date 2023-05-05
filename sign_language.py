import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

def drawCircles(img, hand_landmark, handNo=0):
    if hand_landmark:
        hand_landmark=hand_landmark[handNo].landmark
        tips=[]
        for tips in finger_tips:
            x,y=int(lm_list[tips].x*w), int(lm_list[tips].y*h)
            cv2.circle(img,(x,y),15,(255,0,0),cv2.FILLED)
            

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS, mp_drawing.DrawingSpec((0,0,255),2,2), mp_drawing.DrawingSpec((0,255,0),4,2))
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

             #Code goes here   



            
            
    

    cv2.imshow("hand tracking", img)
    key=cv2.waitKey(1)
    if key == 32:
        break
cv2.destroyAllWindows()