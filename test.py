import sys
from tensorflow.keras.models import load_model
import cv2
model = load_model(sys.argv[2])
RESULT = ['NEGATIVE', 'POSITIVE']
FILENAME = ''
def load(img):
    IMG_SIZE = 224
    img_array = cv2.imread(img)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE),3)
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)
pred = model.predict(load(sys.argv[1]))
print(RESULT[int(pred[0,0])])
