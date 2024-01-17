import cv2 as cv
from features import ExtractBloodVessels, ExtractExudates
import argparse
import os


parser = argparse.ArgumentParser(description='Feature Extraction.')
parser.add_argument('-e', '--exudates', help='Extract Exudates')
parser.add_argument('-v', '--vessels', help='Extract Blood Vessels')
args = parser.parse_args()


if(args.vessels and os.path.isfile(args.vessels)):
    imageName = args.vessels

    # Extraction of Blood vessels
    vessels = ExtractBloodVessels()

    image = cv.imread(imageName, 1)
    # convert image to numpy array
    convNp = vessels.readImage(image)

    # extract green component
    gComponent = vessels.greenComp(convNp)

    # perform Histogram Equalization
    histEqualize = vessels.histEqualize(gComponent)

    # apply Kirsch filter
    kirschFilter = vessels.kirschFilter(histEqualize)

    # apply inverse binary threshold
    thresh = vessels.threshold(kirschFilter)

    # apply median filter
    vesselsImage = vessels.clearSmallObjects(thresh)

    result = imageName.rsplit('.', maxsplit=1)
    cv.imwrite(str(result[0]) + 'Vessels.' + str(result[1]), vesselsImage)
    print("Blood Vessels Extraction Done!")
elif(args.vessels and not os.path.isfile(args.vessels)):
    print("Blood Vessels Extraction Failed! - Image doesn't exist")


if(args.exudates and os.path.isfile(args.exudates)):
    imageName = args.exudates

    # Extraction of exudates
    exudates = ExtractExudates()

    image = cv.imread(imageName, 1)
    # convert image to numpy array
    convNp = exudates.readImage(image)

    # extract green component
    gComponent = exudates.greenComp(convNp)

    # apply Contrast Limited Adaptive Histogram Equalization
    clahe = exudates.CLAHE(gComponent)

    # perform dilation
    dilate = exudates.dilation(clahe)

    # apply inverse binary threshold
    thresh = exudates.threshold(dilate)

    # apply median filter
    exudatesImage = exudates.medianFilter(thresh)

    result = imageName.rsplit('.', maxsplit=1)
    cv.imwrite(str(result[0]) + 'Exudates.' + str(result[1]), exudatesImage)
    print("Exudates Extraction Done!")
elif(args.exudates and not os.path.isfile(args.exudates)):
    print("Exudates Extraction Failed! - Image doesn't exist")
