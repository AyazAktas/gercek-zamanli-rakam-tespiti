import cv2
import pickle
import  numpy as np



#GERÇEK ZAMANLI SINIFLANDIRMA


def preProcess(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.equalizeHist(img)

    img=img/255

    return imgq


cap=cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480)

pickle_in=open("model_trained_new.p","rb")

model=pickle.load(pickle_in)

while True:
    success,frame=cap.read()

    img=np.asarray(frame)
    img=cv2.resize(img,(32,32))
    img=preProcess(img)

    img=img.reshape(1,32,32,1)

    predictions = model.predict(img)
    classIndex = int(np.argmax(predictions))
    probVal = np.max(predictions)

    print(classIndex,probVal)

    if probVal>0.7:
        cv2.putText(frame,str(classIndex)+"  "+str(probVal),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))

    cv2.imshow("Rakam Sınıflandırma",frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):break
