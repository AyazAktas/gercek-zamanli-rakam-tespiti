import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
import pickle


path="myData"

myList=os.listdir(path)
noOfClasses=len(myList)

print("Label sayisi: ",noOfClasses)

images=[]
classNo=[]

for i in range(noOfClasses):
    myImageList=os.listdir(path+"\\"+str(i)) # myData ya giriş
    for j in myImageList:
        img=cv2.imread(path+"\\"+str(i)+"\\"+j)#içerdekilere giriş
        img=cv2.resize(img,(32,32))
        images.append(img)
        classNo.append(i)

print(len(images))
print(len(classNo))

images=np.array(images)
classNo=np.array(classNo)

x_train,x_test,y_train,y_test=train_test_split(images,classNo,test_size=0.5,random_state=42)
x_train,x_validation,y_train,y_validation=train_test_split(x_train,y_train,test_size=0.2,random_state=42)


#fig, axes = plt.subplots(3, figsize=(7, 7))
#fig.subplots_adjust(hspace=0.5)
#sns.countplot(y_train,ax=axes[0])
#axes[0].set_title("y_Train")
#plt.show()
#sns.countplot(y_train,ax=axes[1])
#axes[1].set_title("y_test")
#plt.show()
#sns.countplot(y_train,ax=axes[2])
#axes[2].set_title("y_validation")

#plt.show()



def preProcess(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.equalizeHist(img)

    img=img/255

    return img


x_train=np.array(list(map(preProcess,x_train)))
x_test=np.array(list(map(preProcess,x_test)))
x_validation=np.array(list(map(preProcess,x_validation)))

x_train=x_train.reshape(-1,32,32,1)

x_test=x_test.reshape(-1,32,32,1)
x_validation=x_validation.reshape(-1,32,32,1)


dataGen=ImageDataGenerator(width_shift_range=0.1,height_shift_range=0.1,zoom_range=0.1,rotation_range=10)

dataGen.fit(x_train)
y_train=to_categorical(y_train,noOfClasses)
y_test=to_categorical(y_test,noOfClasses)
y_validation=to_categorical(y_validation,noOfClasses)

model=Sequential()
model.add(Conv2D(input_shape=(32,32,1),filters=8,kernel_size=(5,5),activation="relu",padding="same"))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Conv2D(filters=16,kernel_size=(3,3),activation="relu",padding="same"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(units=256,activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(units=noOfClasses,activation="softmax"))


model.compile(loss="categorical_crossentropy",optimizer="Adam",metrics=["accuracy"])
batch_size=250
hist=model.fit_generator(dataGen.flow(x_train,y_train,batch_size=batch_size),validation_data=(x_validation,y_validation),epochs=70,steps_per_epoch=x_train.shape[0]/batch_size,shuffle=1)
pickle_out=open("model_trained_new.p","wb")
pickle.dump(model,pickle_out)
pickle_out.close()