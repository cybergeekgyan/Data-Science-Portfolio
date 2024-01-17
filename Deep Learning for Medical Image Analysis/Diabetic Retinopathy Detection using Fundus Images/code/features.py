import numpy as np
import cv2 as cv
from skimage import morphology


class ExtractBloodVessels:
    image = 0

    def readImage(self, img):
        self.image = np.array(img)
        return self.image

    def greenComp(self, image):
        gcImg = self.image[:, :, 1]
        self.image = gcImg
        return self.image

    def histEqualize(self, image):
        histEqImg = cv.equalizeHist(self.image)
        self.image = histEqImg
        return self.image

    def kirschFilter(self, image):
        gray = self.image
        if gray.ndim > 2:
            raise Exception("illegal argument: input must be a single channel image (gray)")
        kernelG1 = np.array([[5, 5, 5],
                             [-3, 0, -3],
                             [-3, -3, -3]], dtype=np.float32)
        kernelG2 = np.array([[5, 5, -3],
                             [5, 0, -3],
                             [-3, -3, -3]], dtype=np.float32)
        kernelG3 = np.array([[5, -3, -3],
                             [5, 0, -3],
                             [5, -3, -3]], dtype=np.float32)
        kernelG4 = np.array([[-3, -3, -3],
                             [5, 0, -3],
                             [5, 5, -3]], dtype=np.float32)
        kernelG5 = np.array([[-3, -3, -3],
                             [-3, 0, -3],
                             [5, 5, 5]], dtype=np.float32)
        kernelG6 = np.array([[-3, -3, -3],
                             [-3, 0, 5],
                             [-3, 5, 5]], dtype=np.float32)
        kernelG7 = np.array([[-3, -3, 5],
                             [-3, 0, 5],
                             [-3, -3, 5]], dtype=np.float32)
        kernelG8 = np.array([[-3, 5, 5],
                             [-3, 0, 5],
                             [-3, -3, -3]], dtype=np.float32)

        g1 = cv.normalize(cv.filter2D(gray, cv.CV_32F, kernelG1), None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)
        g2 = cv.normalize(cv.filter2D(gray, cv.CV_32F, kernelG2), None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)
        g3 = cv.normalize(cv.filter2D(gray, cv.CV_32F, kernelG3), None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)
        g4 = cv.normalize(cv.filter2D(gray, cv.CV_32F, kernelG4), None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)
        g5 = cv.normalize(cv.filter2D(gray, cv.CV_32F, kernelG5), None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)
        g6 = cv.normalize(cv.filter2D(gray, cv.CV_32F, kernelG6), None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)
        g7 = cv.normalize(cv.filter2D(gray, cv.CV_32F, kernelG7), None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)
        g8 = cv.normalize(cv.filter2D(gray, cv.CV_32F, kernelG8), None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)
        magn = cv.max(g1, cv.max(g2, cv.max(g3, cv.max(g4, cv.max(g5, cv.max(g6, cv.max(g7, g8)))))))
        self.image = magn
        return self.image

    def threshold(self, image):
        ret, threshImg = cv.threshold(self.image, 160, 180, cv.THRESH_BINARY_INV)
        self.image = threshImg
        return self.image

    def clearSmallObjects(self, image):
        cleanImg = morphology.remove_small_objects(self.image, min_size=130, connectivity=100)
        self.image = cleanImg
        return self.image



class ExtractExudates:
    image = 0

    def readImage(self, img):
        self.image = np.array(img)
        return self.image

    def greenComp(self, image):
        gcImg = image[:, :, 1]
        image = gcImg
        return image

    def CLAHE(self, image):
        clahe = cv.createCLAHE()
        clImg = clahe.apply(image)
        image = clImg
        return image

    def dilation(self, image):
        strEl = cv.getStructuringElement(cv.MORPH_ELLIPSE, (6, 6))
        dilateImg = cv.dilate(image, strEl)
        image = dilateImg
        return image

    def threshold(self, image):
        retValue, threshImg = cv.threshold(image, 220, 220, cv.THRESH_BINARY)
        image = threshImg
        return image

    def medianFilter(self, image):
        medianImg = cv.medianBlur(image, 5)
        image = medianImg
        return image
