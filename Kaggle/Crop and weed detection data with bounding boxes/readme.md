# Crop and Weed Detection with Bounding Boxes 

## About Dataset
Content : 
- This dataset contains 1300 images of sesame crops and different types of weeds with each image labels.
- Each image is a 512 X 512 color image. Labels for images are in YOLO format.

*For Pascal-voc format check this [notebook](https://www.kaggle.com/code/ravirajsinh45/convert-yolo-labels-to-pascalvoc-format/notebook)*

## Problem
Weed is an unwanted thing in agriculture. Weed use the nutrients, water, land and many more things that might have gone to crops. Which results in less production of the required crop. The farmer often uses pesticides to remove weed which is also effective but some pesticides may stick with crop and may causes problems for humans.

## Aim
We aim to develop a system that only sprays pesticides on weed and not on the crop Which will reduce the mixing problem with crops and also reduce the waste of pesticides.

## Data Preparation

STEPS:

1. First of we have to collect dataset for it.For that we have to capture photos of weeds and crops.we collected total 589 images
2. After collection of photos we have to clean the dataset.This step is very important because if any bed photo is remain in dataset it causs worse effect in detection model.after cleaning we have 546 images.
3. Now time for image processing.Our photo size is 4000X3000 color which is very large and model will take very long time for training so we convert all images to 512X512X3 size.
4. now 546 image is not enogh for training,so we have done some magic to convert 546 image into 1300 images.We used Data Augmetation technique to increase dataset.(Check it out keras ImageDataGenerator on google)
5. This step is very tedious, Manual labeling of image data!! In this step we have to drow bounding boxes on photos whether it weed or crop.

# Some images
### sesame crop
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2Fdd84e10cd56c74516656e1fee2742763%2Ftal_55.jpeg?generation=1589438968788391&alt=media)
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2Fbf8669472ca779a36fbd992c6ee80b9b%2Ftal_44.jpeg?generation=1589438975110310&alt=media)

### weed
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2F223e1ae1bc2b2d976ccf79685bb5ef24%2Fimage_359.jpeg?generation=1589439154681622&alt=media)
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2Fec12dbafbf4b5b6e1b46cc1a47e95147%2Fimage_528.jpeg?generation=1589439166010189&alt=media)
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2Fc4e147d01af2667a293c3ff1caac6a85%2Fimage_21.jpeg?generation=1589439187082625&alt=media)

