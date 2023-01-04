# OpenCV-Techniques

## Table of Contents

- IMPORT LIBRARIES
- THRESHOLDING
- BLURRING AND SMOOTHING
- COLOR FILTERING
- EDGE DETECTION
- RGB IMAGE AND RESIZING
- GRAYSCALE IMAGE
- IMAGE DENOISING
- IMAGE THRESHOLDING
- IMAGE GRADIENTS
- EDGE DETECTION FOURIER TRANSFORM ON IMAGE
- LINE TRANSFORM
- CORNER DETECTION
- MORPHOLOGICAL TRANSFORMATION OF IMAGE
- GEOMETRIC TRANSFORMATION OF IMAGE
- CONTOURS
- IMAGE PYRAMIDS
- COLORSPACE CONVERSION AND OBJECT TRACKING
- INTERACTIVE FOREGROUND EXTRACTION
- IMAGE SEGMENTATION
- IMAGE INPAINTING
- TEMPLATE MATCHING
- FACE AND EYE DETECTION
- CROPPING AN IMAGE


### IMPORT LIBRARIES 
*Import all the required libraries using the below commands:*

```Python
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline
```


## Thresholding

Thresholding is a basic concept in computer vision. It is widely used in image processing.

Thresholding is used to simplify visual data for further analysis. In image processing, we need to pre-process the image data and get the important details. This technique is important to separate background image and foreground image.

The function used for the threshold is given below:

*cv2.threshold(img , 125, 255, cv2.THRESH_BINARY)*

The first parameter is the image data, the second one is the threshold value, the third is the maximum value (generally 255) and the fourth one is the threshold technique. Let’s implement this in our code and observe how different techniques affect the image.

![alt text](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/Thresholding/threshold.png "threshold")

## Blurring and Smoothing


Images may contain lots of noise. There are few techniques through which we can reduce the amount of noise by blurring them. The blurring technique is used as a preprocessing step in various other algorithms. With blurring, we can hide the details when necessary. For example – the police use the blurring technique to hide the face of the criminal. Later on, when learning about edge detection in the image, we will see how blurring the image improves our edge detection experience.

There are different computer vision algorithms available to us which will blur the image using a kernel size. There is no right kernel size, according to our need, we have to try the trial and error method to see what works better in our case.

**There are four different types of functions available for blurring:**

**cv2.blur()** – This function takes average of all the pixels surrounding the filter. It is a simple and fast blurring technique.<br>
**cv2.GaussianBlur()** – Gaussian function is used as a filter to remove noise and reduce detail. It is used in graphics software and also as a preprocessing step in machine learning and deep learning models.<br>
**cv2.medianBlur()** – This function uses median of the neighbouring pixels. Widely used in digital image processing as under certain conditions, it can preserve some edges while removing noise.<br>
**cv2.bilateralFilter()** – In this method, sharp edges are preserved while the weak ones are discarded.<br>

![alt text](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/Blurring%20and%20Smoothing/blurring.png "blurring")


## Color Filtering

When you need information about a specific color, you can take out the color you want.

This process is called **color filtering**. We can define a range of color which we want to focus at. For example – if you want to track a tennis ball in an image, we can filter out only green color from the image. This computer vision technique works better when the color that needs to be extracted is different from the background. 

![alt text](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/Color%20Filtering/color_filter.png "colorfiltering")


*How to implement color filtering in your application.*

**Step 1: Convert the color image into HSV which is Hue Saturation Value**

**HSV** is also another way of representing a color. It is easier to specify a color range in HSV format that is why OpenCV expects us to specify the range in this format. Hue is for color (0- 179), Saturation is for the strength of color (0-255) and Value is for the different lighting conditions from low to high (0-255).

**Step 2: Create the mask**

OpenCV provides us with cv2.inRange() function. The first parameter contains the HSV image, the second parameter has a numpy array with lower bound of the color we want to extract and the third parameter contains the upper bound of the color.

**Note**: The upper and lower bound of color should be in HSV value. The mask contains only the 0 and 1 values representing black and white respective.

**Step 3: Perform bitwise ‘and’ operation**

At last, we perform bitwise ‘and’ operation on the original image and the mask image to get only the color we want.

## Edge Detection

Edges are a sudden change in the brightness of the image. The significant transitions in the brightness of the image are used to calculate the edges in an image. Edge detection is used for various image processing purposes. One of them is to sharpen the images. Sharpening of images is done to make the images more clear. Edge detection is used to enhance the images and image recognition becomes easier.

The canny edge detection algorithm is mostly used to detect the edges in an image.

OpenCV contains the function cv2.Canny() for edge detection.

cv2.Canny(img, 50, 150)

First parameter is the image data, the second parameter is the lower threshold value and the third parameter is the upper threshold value. You need to try different values for tuning the edge detection algorithm.

![alt text](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/Edge%20DEtection/Edge-Detection.png "edgedetection")


### RGB IMAGE AND RESIZING 

==> An RGB image where RGB indicates Red, Green, and Blue respectively can be considered as three images stacked on top of each other. It also has a nickname called ‘True Color Image’ as it represents a real-life image as close as possible and is based on human perception of colours.

==> The RGB colour model is used to display images on cameras, televisions, and computers.

==> Resizing all images to a particular height and width will ensure uniformity and thus makes processing them easier since images are naturally available in different sizes.

==> If the size is reduced, though the processing is faster, data might be lost in the image. If the size is increased, the image may appear fuzzy or pixelated. Additional information is usually filled in using interpolation.

```Python
height = 224
width = 224
font_size = 20
plt.figure(figsize=(15, 8))
for i, path in enumerate(paths):
name = os.path.split(path)[-1]
img = cv2.imread(path, cv2.IMREAD_COLOR)
resized_img = cv2.resize(img, (height, width))
plt.subplot(1, 2, i+1).set_title(name[ : -4], fontsize = font_size); plt.axis('off')
plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
plt.show()
```

![RGB image resizing](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/rgbimageresizing.png)

### GRAYSCALE IMAGE 

==> Grayscale images are images that are shades of grey. It represents the degree of luminosity and carries the intensity information of pixels in the image. Black is the weakest intensity and white is the strongest intensity.

==> Grayscale images are efficient as they are simpler and faster than colour images during image processing.

```Python
plt.figure(figsize=(15, 8))
for i, path in enumerate(paths):
name = os.path.split(path)[-1]
img = cv2.imread(path, 0)
resized_img = cv2.resize(img, (height, width))
plt.subplot(1, 2, i + 1).set_title(f'Grayscale {name[ : -4]} Image', fontsize = font_size); plt.axis('off')
plt.imshow(resized_img, cmap='gray')
plt.show()
``` 

![Grayscale images](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/greyscaleimage.png)

### IMAGE DENOISING

==> Image denoising removes noise from the image. It is also known as ‘Image Smoothing’. The image is convolved with a low pass filter kernel which gets rid of high-frequency content like edges of an image

```Python
for i, path in enumerate(paths):
name = os.path.split(path)[-1]
img = cv2.imread(path, cv2.IMREAD_COLOR)
resized_img = cv2.resize(img, (height, width))
denoised_img = cv2.medianBlur(resized_img, 5)
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title(f'Original {name[ : -4]} Image', fontsize = font_size); plt.axis('off')
plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2).set_title(f'After Median Filtering of {name[ : -4]} Image', fontsize = font_size); plt.axis('off')
plt.imshow(cv2.cvtColor(denoised_img, cv2.COLOR_BGR2RGB))
plt.show()
```
![Image denoising](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/imagedenoising.png)

### IMAGE THRESHOLDING

==> Image Thresholding is self-explanatory. If the pixel value in an image is above a certain threshold, a particular value is assigned and if it is below the threshold, another particular value is assigned.

==> Adaptive Thresholding does not have global threshold values. Instead, a threshold is set for a small region of the image. Hence, there are different thresholds for the entire image and they produce greater outcomes for dissimilar illumination. There are different Adaptive Thresholding methods

```Python
for i, path in enumerate(paths):
name = os.path.split(path)[-1]
img = cv2.imread(path, 0)
resized_img = cv2.resize(img, (height, width))
denoised_img = cv2.medianBlur(resized_img, 5)
th = cv2.adaptiveThreshold(denoised_img, maxValue = 255, adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType = cv2.THRESH_BINARY, blockSize = 11, C = 2)
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title(f'Grayscale {name[ : -4]} Image', fontsize = font_size); plt.axis('off')
plt.imshow(resized_img, cmap = 'gray')
plt.subplot(1, 2, 2).set_title(f'After Adapative Thresholding of {name[ : -4]} Image', fontsize = font_size); plt.axis('off')
plt.imshow(cv2.cvtColor(th, cv2.COLOR_BGR2RGB))
plt.show()
```
![image thresholding](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/imagethresholding.png)

### IMAGE GRADIENTS

==> Gradients are the slope of the tangent of the graph of the function. Image gradients find the edges of a grayscale image in the x and y-direction. This can be done by calculating derivates in both directions using Sobel x and Sobel y operations.

```Python
for i, path in enumerate(paths):
name = os.path.split(path)[-1]
img = cv2.imread(path, 0)
resized_img = cv2.resize(img, (height, width))
laplacian = cv2.Laplacian(resized_img, cv2.CV_64F)
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title(f'Grayscale {name[ : -4]} Image', fontsize = font_size); plt.axis('off')
plt.imshow(resized_img, cmap = 'gray')
plt.subplot(1, 2, 2).set_title(f'After finding Laplacian Derivatives of {name[ : -4]} Image', fontsize = font_size); plt.axis('off')
plt.imshow(cv2.cvtColor(laplacian.astype('float32'), cv2.COLOR_BGR2RGB))
plt.show()
```

![Image gradients](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/imagegradients.png)

### EDGE DETECTION
Edge Detection is performed using Canny Edge Detection which is a multi-stage algorithm. The stages to achieve edge detection are as follows. Noise Reduction – Smoothen image using Gaussian filter
Find Intensity Gradient – Using the Sobel kernel, find the first derivative in the horizontal (Gx) and vertical (Gy) directions.

```Python
for i, path in enumerate(paths):
name = os.path.split(path)[-1]
img = cv2.imread(path, 0)
resized_img = cv2.resize(img, (height, width))
edges = cv2.Canny(resized_img, threshold1 = 100, threshold2 = 200)
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title(f'Grayscale {name[ : -4]} Image', fontsize = font_size); plt.axis('off')
plt.imshow(resized_img, cmap = 'gray')
plt.subplot(1, 2, 2).set_title(f'After Canny Edge Detection of {name[ : -4]} Image', fontsize = font_size); plt.axis('off')
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
```

![Edge detection](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/edgedetection.png)

### FOURIER TRANSFORM ON IMAGE 

==> Fourier Transform analyzes the frequency characteristics of an image. Discrete Fourier Transform is used to find the frequency domain.

==> Fast Fourier Transform (FFT) calculates the Discrete Fourier Transform. Frequency is higher usually at the edges or wherever noise is present. When FFT is applied to the image, the high frequency is mostly in the corners of the image. To bring that to the centre of the image, it is shifted by N/2 in both horizontal and vertical directions.

==> Finally, the magnitude spectrum of the outcome is achieved. Fourier Transform is helpful in object detection as each object has a distinct magnitude spectrum

```Python
for i, path in enumerate(paths):
name = os.path.split(path)[-1]
img = cv2.imread(path, 0)
resized_img = cv2.resize(img, (height, width))
freq = np.fft.fft2(resized_img)
freq_shift = np.fft.fftshift(freq)
magnitude_spectrum = 20 * np.log(np.abs(freq_shift))
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title(f'Grayscale {name[ : -4]} Image', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2).set_title(f'Magnitude Spectrum of {name[ : -4]} Image', fontsize = font_size); plt.axis('off')   
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.show()
```
![magnitude spectrum](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/foruriertransformonimage.png)

### LINE TRANSFORM 

==> Hough Transform can detect any shape even if it is distorted when presented in mathematical form. A line in the cartesian coordinate system y = mx + c can be put in its polar coordinate system as rho = xcosθ + ysinθ. rho is the perpendicular distance from the origin to the line and θ is the angle formed by the horizontal axis and the perpendicular line in the clockwise direction.

==> So, the line is represented in these two terms (rho, θ). An array is created for these two terms where rho forms the rows and θ forms the columns. This is called the accumulator. rho is the distance resolution of the accumulator in pixels and θ is the angle resolution of the accumulator in radians.

==> For every line, its (x, y) values can be put into (rho, θ) values. For every (rho, θ) pair, the accumulator is incremented. This is repeated for every point on the line. A particular (rho, θ) cell is voted for the presence of a line.

==> This way the cell with the maximum votes implies a presence of a line at rho distance from the origin and at angle θ degrees.

```Python
min_line_length = 100
max_line_gap = 10
img = cv2.imread('../input/cv-images/hough-min.png')
resized_img = cv2.resize(img, (height, width))
img_copy = resized_img.copy()
edges = cv2.Canny(resized_img, threshold1 = 50, threshold2 = 150)
lines = cv2.HoughLinesP(edges, rho = 1, theta = np.pi / 180, threshold = 100, minLineLength = min_line_length, maxLineGap = max_line_gap)
for line in lines:
    for x1, y1, x2, y2 in line:
hough_lines_img = cv2.line(resized_img ,(x1,y1),(x2,y2),color = (0,255,0), thickness = 2)
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title('Original Image', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2).set_title('After Hough Line Transformation', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(hough_lines_img, cv2.COLOR_BGR2RGB))
plt.show()
```

![Line transform](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/line%20transform.png)

### CORNER DETECTION
==> Harris Corner finds the difference in intensity for a displacement in all directions to detect a corner.

```Python
img = cv2.imread('../input/cv-images/corners-min.jpg')
resized_img = cv2.resize(img, (height, width))
img_copy = resized_img.copy()
gray = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.cornerHarris(gray, blockSize = 2, ksize = 3, k = 0.04)
corners = cv2.dilate(corners, None)
resized_img[corners > 0.0001 * corners.max()] = [0, 0, 255]
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title('Original Image', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2).set_title('After Harris Corner Detection', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
plt.show()
```

![corner detection](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/cornerdetection.png)

### MORPHOLOGICAL TRANSFORMATION OF IMAGE 
==> Morphological Transformation is usually applied on binary images where it takes an image and a kernel which is a structuring element as inputs. Binary images may contain imperfections like texture and noise.

==> These transformations help in correcting these imperfections by accounting for the form of the image

```Python
kernel = np.ones((5,5), np.uint8)
plt.figure(figsize=(15, 8))
img = cv2.imread('../input/cv-images/morph-min.jpg', cv2.IMREAD_COLOR)
resized_img = cv2.resize(img, (height, width))
morph_open = cv2.morphologyEx(resized_img, cv2.MORPH_OPEN, kernel)
morph_close = cv2.morphologyEx(morph_open, cv2.MORPH_CLOSE, kernel)
plt.subplot(1,2,1).set_title('Original Digit - 7 Image', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2).set_title('After Morphological Opening and Closing of Digit - 7 Image', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(morph_close, cv2.COLOR_BGR2RGB))
plt.show()
```

![Morphologiacal transformation](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/morphologicaltransformationofimage.png)

### GEOMETRIC TRANSFORMATION OF IMAGE 
==> Geometric Transformation of images is achieved by two transformation functions namely cv2.warpAffine and cv2.warpPerspective that receive a 2×3 and 3×3 transformation matrix respectively.

```Python
pts1 = np.float32([[1550, 1170],[2850, 1370],[50, 2600],[1850, 3450]])
pts2 = np.float32([[0,0],[4160,0],[0,3120],[4160,3120]])
img = cv2.imread('../input/cv-images/book-min.jpg', cv2.IMREAD_COLOR)
transformation_matrix = cv2.getPerspectiveTransform(pts1, pts2)
final_img = cv2.warpPerspective(img, M = transformation_matrix, dsize = (4160, 3120))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (256, 256))
final_img = cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB)
final_img = cv2.resize(final_img, (256, 256))
plt.figure(figsize=(15, 8))    
plt.subplot(1,2,1).set_title('Original Book Image', fontsize = font_size); plt.axis('off')   
plt.imshow(img)
plt.subplot(1,2,2).set_title('After Perspective Transformation of Book Image', fontsize = font_size); plt.axis('off')   
plt.imshow(final_img)
plt.show()
```

![geomatric transformation](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/geometric%20transformation%20of%20image.png)

### CONTOURS 
==> Contours are outlines representing the shape or form of objects in an image. They are useful in object detection and recognition. Binary images produce better contours. There are separate functions for finding and drawing contours.

```Python
plt.figure(figsize=(15, 8))
img = cv2.imread('contours-min.jpg', cv2.IMREAD_COLOR)
resized_img = cv2.resize(img, (height, width))
contours_img = resized_img.copy()
img_gray = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img_gray, thresh = 127, maxval = 255, type = cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_NONE)
cv2.drawContours(contours_img, contours, contourIdx = -1, color = (0, 255, 0), thickness = 2)
plt.subplot(1,2,1).set_title('Original Image', fontsize = font_size); plt.axis('off')   
plt.imshow(resized_img)
plt.subplot(1,2,2).set_title('After Finding Contours', fontsize = font_size); plt.axis('off')   
plt.imshow(contours_img)
plt.show()
```

![countours](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/contours.png)

### IMAGE PYRAMIDS 
==> Images have a resolution which is the measure of the information in the image. In certain scenarios of image processing like Image Blending, working with images of different resolutions is necessary to make the blend look more realistic.

==> In OpenCV, images of high resolution can be converted to low resolution and vice-versa. By converting a higher-level image to a lower-level image, the lower-level image becomes 1/4th the area of the higher-level image.

==> When this is done for a number of iterations and the resultant images are placed next to each other in order, it looks like it is forming a pyramid and hence its name ‘Image Pyramid’

```Python
R = cv2.imread('GR-min.jpg', cv2.IMREAD_COLOR)
R = cv2.resize(R, (224, 224))
H = cv2.imread('../input/cv-images/H-min.jpg', cv2.IMREAD_COLOR)
H = cv2.resize(H, (224, 224))
G = R.copy()
guassian_pyramid_c = [G]
for i in range(6):
G = cv2.pyrDown(G)
guassian_pyramid_c.append(G)
G = H.copy()
guassian_pyramid_d = [G]
for i in range(6):
G = cv2.pyrDown(G)
guassian_pyramid_d.append(G)
laplacian_pyramid_c = [guassian_pyramid_c[5]]
for i in range(5, 0, -1):
GE = cv2.pyrUp(guassian_pyramid_c[i])
L = cv2.subtract(guassian_pyramid_c[i-1], GE)
laplacian_pyramid_c.append(L)
laplacian_pyramid_d = [guassian_pyramid_d[5]]
for i in range(5,0,-1):
guassian_expanded = cv2.pyrUp(guassian_pyramid_d[i])
L = cv2.subtract(guassian_pyramid_d[i-1], guassian_expanded)
laplacian_pyramid_d.append(L)
laplacian_joined = []
for lc,ld in zip(laplacian_pyramid_c, laplacian_pyramid_d):
r, c, d = lc.shape
lj = np.hstack((lc[:, 0 : int(c / 2)], ld[:, int(c / 2) :]))
laplacian_joined.append(lj)
laplacian_reconstructed = laplacian_joined[0]
for i in range(1,6):
laplacian_reconstructed = cv2.pyrUp(laplacian_reconstructed)
laplacian_reconstructed = cv2.add(laplacian_reconstructed, laplacian_joined[i])
direct = np.hstack((R[ : , : int(c / 2)], H[ : , int(c / 2) : ]))
plt.figure(figsize=(30, 20))
plt.subplot(2,2,1).set_title('Golden Retriever', fontsize = 35); plt.axis('off')   
plt.imshow(cv2.cvtColor(R, cv2.COLOR_BGR2RGB))
plt.subplot(2,2,2).set_title('Husky', fontsize = 35); plt.axis('off')   
plt.imshow(cv2.cvtColor(H, cv2.COLOR_BGR2RGB))
plt.subplot(2,2,3).set_title('Direct Joining', fontsize = 35); plt.axis('off')   
plt.imshow(cv2.cvtColor(direct, cv2.COLOR_BGR2RGB))
plt.subplot(2,2,4).set_title('Pyramid Blending', fontsize = 35); plt.axis('off')   
plt.imshow(cv2.cvtColor(laplacian_reconstructed, cv2.COLOR_BGR2RGB))
plt.show()
```

![Image pyramids](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/imagepyramids.png)

### COLORSPACE CONVERSION AND OBJECT TRACKING 

==> Colourspace Conversion, BGR↔Gray, BGR↔HSV conversions are possible. The BGR↔Gray conversion was previously seen. HSV stands for Hue, Saturation, and Value respectively.

==> Since HSV describes images in terms of their hue, saturation, and value instead of RGB where R, G, B are all co-related to colour luminance, object discrimination is much easier with HSV images than RGB images.

```Python
lower_white = np.array([0, 0, 150])
upper_white = np.array([255, 255, 255])
img = cv2.imread('../input/cv-images/color_space_cat.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (height, width))
background = cv2.imread("../input/cv-images/galaxy.jpg", cv2.IMREAD_COLOR)
background = cv2.resize(background, (height, width))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_img, lowerb = lower_white, upperb = upper_white)
final_img = cv2.bitwise_and(img, img, mask = mask)
final_img = np.where(final_img == 0, background, final_img)
plt.figure(figsize=(15, 8))
plt.subplot(1,2,1).set_title('Original Cat Image', fontsize = font_size); plt.axis('off')   
plt.imshow(img)
plt.subplot(1,2,2).set_title('After Object Tracking using Color-space Conversion of Cat Image', fontsize = font_size); plt.axis('off')   
plt.imshow(final_img)
plt.show()
```

![colorspace conversion](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/colorspace.png)

### INTERACTIVE FOREGROUND EXTRACTION 

*The foreground of the image is extracted using user input and the Gaussian Mixture Model (GMM).*

```Python
img = cv2.imread('Cat.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (height, width))
img_copy = img.copy()
mask = np.zeros(img.shape[ : 2], np.uint8)
background_model = np.zeros((1,65),np.float64)
foreground_model = np.zeros((1,65),np.float64)
rect = (10, 10, 224, 224)
cv2.grabCut(img, mask = mask, rect = rect, bgdModel = background_model, fgdModel = foreground_model, iterCount = 5, mode = cv2.GC_INIT_WITH_RECT)
new_mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * new_mask[:, :, np.newaxis]
plt.figure(figsize=(15, 8))
plt.subplot(1,2,1).set_title('Original Cat Image', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2).set_title('After Interactive Foreground Extraction of Cat Image', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
```

![foreground extraction](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/interactive%20foregroundextraction.png)

### IMAGE SEGMENTATION

==>Image Segmentation is done using the Watershed Algorithm. This algorithm treats the grayscale image as hills and valleys representing high and low-intensity regions respectively. If these valleys are filled with coloured water and as the water rises, depending on the peaks, different valleys with different coloured water will start to merge.

==> To avoid this, barriers can be built which gives the segmentation result. This is the concept of the Watershed algorithm. This is an interactive algorithm as one can specify which pixels belong to an object or background. The pixels that one is unsure about can be marked as 0. Then the watershed algorithm is applied on this where it updates the labels given and all the boundaries are marked as -1

```Python
img = cv2.imread('lymphocytes-min.jpg', cv2.IMREAD_COLOR)
resized_img = cv2.resize(img, (height, width))
img_copy = resized_img.copy()
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, thresh = 0, maxval = 255, type = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
opening = cv2.morphologyEx(thresh, op = cv2.MORPH_OPEN, kernel = kernel, iterations = 2)
background = cv2.dilate(opening, kernel = kernel, iterations = 5)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, foreground = cv2.threshold(dist_transform, thresh = 0.2  * dist_transform.max(), maxval = 255, type = cv2.THRESH_BINARY)
foreground = np.uint8(foreground)
unknown = cv2.subtract(background, foreground)
ret, markers = cv2.connectedComponents(foreground)
markers = markers + 1
markers[unknown == 255] = 0
markers = cv2.watershed(resized_img, markers)
resized_img[markers == -1] = [0, 0, 255]
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title('Lymphocytes Image', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2).set_title('After Watershed Algorithm', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
plt.show()
```
![imagesegmentation](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/imagesegmentation.png)
### IMAGE INPAINTING 
- Images may be damaged and require fixing. **For example,** *an image may have no pixel information in certain portions.* 
- Image Inpainting will fill all the missing information with the help of the surrounding pixels.

```Python
mask = cv2.imread('mask.png',0)
mask = cv2.resize(mask, (height, width))
for i, path in enumerate(paths):
name = os.path.split(path)[-1]
img = cv2.imread(path, cv2.IMREAD_COLOR)
resized_img = cv2.resize(img, (height, width))
ret, th = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
inverted_mask = cv2.bitwise_not(th)
damaged_img = cv2.bitwise_and(resized_img, resized_img, mask = inverted_mask)
result = cv2.inpaint(resized_img, mask, inpaintRadius = 3, flags = cv2.INPAINT_TELEA)
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title(f'Damaged Image of {name[ : -4]}', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(damaged_img, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2).set_title(f'After Image Inpainting of {name[ : -4]}', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()
```

![imageinpainting](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/imageinpainting.png)

### TEMPLATE MATCHING 
- Template Matching matches the template provided to the image in which the template must be found. 
- The template is compared to each patch of the input image. This is similar to a 2D convolution operation. 
- It results in a grayscale image where each pixel denotes the similarity of the neighbourhood pixels to that of the template.

==> From this output, the maximum/minimum value is determined. This can be regarded as the top-left corner coordinates of the rectangle. By also considering the width and height of the template, the resultant rectangle is the region of the template in the image.

```Python
w, h, c = template.shape
method = eval('cv2.TM_CCOEFF')
result = cv2.matchTemplate(img, templ = template, method = method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, color = (255, 0, 0), thickness = 3)
plt.figure(figsize=(30, 20))
plt.subplot(2, 2, 1).set_title('Image of Selena Gomez and Taylor Swift', fontsize = 35); plt.axis('off')
plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
plt.subplot(2, 2, 2).set_title('Face Template of Selena Gomez', fontsize = 35); plt.axis('off')
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.subplot(2, 2, 3).set_title('Matching Result', fontsize = 35); plt.axis('off')
plt.imshow(result, cmap = 'gray')
plt.subplot(2, 2, 4).set_title('Detected Face', fontsize = 35); plt.axis('off')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
```
![templatematching](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/templatematching.png)

### FACE AND EYE DETECTION
*It is done by using Haar Cascades. Check the below code for face and eye detection:*
```Python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
img = cv2.imread('../input/cv-images/elon-min.jpg')
img = cv2.resize(img, (height, width))
img_copy = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5)
for (fx, fy, fw, fh) in faces:
img = cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 2)
roi_gray = gray[fy:fy+fh, fx:fx+fw]
roi_color = img[fy:fy+fh, fx:fx+fw]
eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1).set_title('Elon Musk', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2).set_title('Elon Musk - After Face and Eyes Detections', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
```

![faceandeyedetection](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/images/faceandeyedetection.png)


### CROPPING AN IMAGE

**Importing the cv2 library**
```Python
//Python
//Importing the cv2 library
import cv2 
```
```C++
//C++
#include<opencv2/opencv.hpp>
#include<iostream>

// Namespace nullifies the use of cv::function(); 
using namespace std;
using namespace cv;
```

==> *The above code imports the OpenCV library in Python and C++ respectively.*

**Cropping Using OpenCV**

The image that will be used for cropping in this post.
![croppingimage](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/CroppingImage/croppingimage.png)



=> **Python:**
```Python
img=cv2.imread('test.png')

# Prints Dimensions of the image
print(img.shape) 

# Display the image
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

=> **C++:**
```C++
Mat img = imread("test.jpg");

//Print the height and width of the image
cout << "Width : " << img.size().width << endl;
cout << "Height: " << img.size().height << endl;
cout << "Channels: " << img.channels() << endl;

// Display image
imshow("Image", img);
waitKey(0);
destroyAllWindows();
```

=> - The above code reads and displays an image and its dimensions. 
   - The dimensions include not just the width and height of the 2-D matrix, but the number of channels as well (for example, an RGB image has 3 channels – Red, Green and Blue).

**Let’s try to crop the part of the image that contains the flower.**

//Python
```Python
cropped_image = img[80:280, 150:330] # Slicing to crop the image

# Display the cropped image
cv2.imshow("cropped", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
```

//C++
```C++
Mat crop = img(Range(80,280),Range(150,330)); // Slicing to crop the image

// Display the cropped image
imshow("Cropped Image", crop);

waitKey(0);
destroyAllWindows();
return 0;
```

![croppedimage](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/CroppingImage/croppedimageresult.png)


=> - *In **Python,** you crop the image using the same method as NumPy array slicing.*
   - *To slice an array, you need to specify the start and end index of the first as well as the second dimension.* 

        - The first dimension is always the number of rows or the height of the image.
        - The second dimension is the number of columns or the width of the image. 

*It goes with the convention that the first dimension of a 2D array represents the rows of the array (where each row represents the y-coordinate of the image).* 
*How to slice a NumPy array?*

*Check out the syntax in this example:*
```Python
//Python
cropped = img[start_row:end_row, start_col:end_col]
```
=> - *In C++, we use the **Range()** function to crop the image.*

   - Like Python, it also applies slicing. 
   - Here too, the image is read in as a 2D matrix, following the same convention described above. 

*The following is the C++ syntax to crop an image:*
```C++
//C++
img(Range(start_row, end_row), Range(start_col, end_col))
```

**Dividing an Image Into Small Patches Using Cropping**

- *One practical application of cropping in OpenCV can be to divide an image into smaller patches.* 
- *Use loops to crop out a fragment from the image.* 
- *Start by getting the height and width of the required patch from the shape of the image.*

```Python
//Python
img =  cv2.imread("test_cropped.jpg")
image_copy = img.copy() 
imgheight=img.shape[0]
imgwidth=img.shape[1]
```
```C++
//C++
Mat img = imread("test_cropped.jpg");
Mat image_copy = img.clone();
int imgheight = img.rows;
int imgwidth = img.cols;
```

=> - *Load the height and width to specify the range till which the smaller patches need to be cropped out.* 
   - *For this, use the range() function in Python.* 
   - *Now, crop using two for loops:*

       - one for the width range
       - other for the height range 

- *We are using patches with a height and width of 76 pixels and 104 pixels respectively. 
- *The stride (number of pixels we move through the image) for the inner and outer loops is equal to the width and height of the patches that we are considering.*

```Python
//Python
M = 76
N = 104
x1 = 0
y1 = 0

for y in range(0, imgheight, M):
    for x in range(0, imgwidth, N):
        if (imgheight - y) < M or (imgwidth - x) < N:
            break
            
        y1 = y + M
        x1 = x + N

        # check whether the patch width or height exceeds the image width or height
        if x1 >= imgwidth and y1 >= imgheight:
            x1 = imgwidth - 1
            y1 = imgheight - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        elif y1 >= imgheight: # when patch height exceeds the image height
            y1 = imgheight - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        elif x1 >= imgwidth: # when patch width exceeds the image width
            x1 = imgwidth - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        else:
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
```

```C++
//C++
    int M = 76;
    int N = 104;

    int x1 = 0;
    int y1 = 0;
    for (int y = 0; y<imgheight; y=y+M)
    {
        for (int x = 0; x<imgwidth; x=x+N)
        {
            if ((imgheight - y) < M || (imgwidth - x) < N)
            {
                break;
            }
            y1 = y + M;
            x1 = x + N;
            string a = to_string(x);
            string b = to_string(y);

            if (x1 >= imgwidth && y1 >= imgheight)
            {
                x = imgwidth - 1;
                y = imgheight - 1;
                x1 = imgwidth - 1;
                y1 = imgheight - 1;

                // crop the patches of size MxN
                Mat tiles = image_copy(Range(y, imgheight), Range(x, imgwidth));
                //save each patches into file directory
                imwrite("saved_patches/tile" + a + '_' + b + ".jpg", tiles);  
                rectangle(img, Point(x,y), Point(x1,y1), Scalar(0,255,0), 1);    
            }
            else if (y1 >= imgheight)
            {
                y = imgheight - 1;
                y1 = imgheight - 1;

                // crop the patches of size MxN
                Mat tiles = image_copy(Range(y, imgheight), Range(x, x+N));
                //save each patches into file directory
                imwrite("saved_patches/tile" + a + '_' + b + ".jpg", tiles);  
                rectangle(img, Point(x,y), Point(x1,y1), Scalar(0,255,0), 1);    
            }
            else if (x1 >= imgwidth)
            {
                x = imgwidth - 1;   
                x1 = imgwidth - 1;

                // crop the patches of size MxN
                Mat tiles = image_copy(Range(y, y+M), Range(x, imgwidth));
                //save each patches into file directory
                imwrite("saved_patches/tile" + a + '_' + b + ".jpg", tiles);  
                rectangle(img, Point(x,y), Point(x1,y1), Scalar(0,255,0), 1);    
            }
            else
            {
                // crop the patches of size MxN
                Mat tiles = image_copy(Range(y, y+M), Range(x, x+N));
                //save each patches into file directory
                imwrite("saved_patches/tile" + a + '_' + b + ".jpg", tiles);  
                rectangle(img, Point(x,y), Point(x1,y1), Scalar(0,255,0), 1);    
            }
        }
    }
```

=> - *Next, display the image patches, using the **imshow()** function.* 
   - *Save it to the file directory, using the **imwrite()** function.* 
```python
//Python
#Save full image into file directory
cv2.imshow("Patched Image",img)
cv2.imwrite("patched.jpg",img)
 
cv2.waitKey()
cv2.destroyAllWindows()
```

```C++
//C++
    imshow("Patched Image", img);
    imwrite("patched.jpg",img);
    waitKey();
    destroyAllWindows();
```

**The below GIF demonstrates the process of executing the code for dividing the image into patches:**

![divingpatches](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/CroppingImage/dividingtheimageintopatches.gif)

**The final image with the rectangular patches overlayed on it will look something like this:**

![dividingimgpatchesresult](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/CroppingImage/dividingimgpatchesresult.jpg)


**The following image shows the separate image patches that are saved to the disk.**

![final result](https://github.com/gyanprakash0221/OpenCV-Techniques/blob/main/CroppingImage/seperateimagespatchescreated.jpg)


### Some Interesting Applications using Cropping

- You can use cropping to extract a region of interest from an image and discard the other parts you do not need to use.
- You can extract patches from an image to train a patch-based neural network.
