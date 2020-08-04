from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
import time

'''

Make changes in NAME / MODEL_FOLDER accordingly


'''
##########################################
#             MODIFICATION               #
##########################################
NAME = 'COVID-IMAGING-CNN-{}'.format(time.time())
MODEL_FOLDER = "/home/usr/workspace/pycharm-workspace/XRAY-IMAGING/models/"


tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))




train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
    '/home/usr/workspace/pycharm-workspace/XRAY-IMAGING/post-processed',
    target_size=(224,224),
    batch_size=32,
    class_mode='binary',
    subset='training'
)
validation_generator = train_datagen.flow_from_directory(
    '/home/usr/workspace/pycharm-workspace/XRAY-IMAGING/post-processed',
    target_size=(224,224),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

model = Sequential(
    [
        layers.Conv2D(32, (3,3), input_shape=(224,224,3), activation='relu'),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2,2)),
        layers.Dropout(0.25),


        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.25),

        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.25),

        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid'),

    ]
)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit_generator(
    train_generator,
    steps_per_epoch= 8,
    validation_data = validation_generator,
    validation_steps= 2,
    epochs= 10,
    callbacks=[tensorboard],
)
PATH_TO_SAVE = MODEL_FOLDER + NAME
model.save(PATH_TO_SAVE)
model.evaluate(validation_generator)
