# XRAY-IMAGING
Analyzing X-Ray Imaging of potential covid-patient using deep learning


## Disclaimer
**The dataset was quite small (180 images each). I do not claim any diagonstic performance of the model this is simply an experiment**

## Requirements
* Tensorflow 2.0
* Keras
* Numpy 
* CV2

## Datasets
The datasets are from [HERE](https://github.com/ieee8023/covid-chestxray-dataset/blob/master/README.md) and [Kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

## Example

<code>python3 test.py sample.jpeg models/100accuracy</code>

The command above should print "Negative"

## Model

I was able to get a 100% accuracy on validation data, however it's likely due to a small dataset
I did a 80/20 split for the dataset
Layer (type) | Output Shape | Param 
-------|----|-------
Conv2D | 32 | 896
Conv2D | 64 | 18496
MaxPooling2D | 64 | 0
Dropout 0.25 | 64 | 0
Conv2D | 64 | 36928
MaxPooling2D | 64 | 0
Dropout 0.25 | 64 | 0
Conv2D | 128 | 73856
MaxPooling2D | 128 | 0
Dropout 0.25 | 64 | 0
Flatten | | 0
Dense | 64 | 5537856
Dropout 0.5| 64 | 0
Dense | 1 | 65

