# SIFT Feature Extraction
This repository contains Python code for extracting Scale-Invariant Feature Transform (SIFT) features from a pair of images using OpenCV. SIFT features are useful for various computer vision tasks, such as image matching and object recognition.

### Instructions:
Follow the steps below to use the SIFT feature extraction code:

### Clone the Repository:
git clone https://github.com/Skanda-sap/sift_feature_extraction.git

### Provide Images:
Ensure that you have a pair of images for feature extraction. Update the file paths of img1 and img2 variables in the sift_feature_extraction.py file to point to your images.

### Run the Code:
Execute the code using the following command:

### Copy code:
python3 sift_feature_extraction.py
The code will extract SIFT features from the provided images and generate a new image (matchedImage.jpg) displaying the matched features.

### Review Results:
Open the generated matchedImage.jpg file to visualize the matched SIFT features between the two input images.

### Notes:
The code uses the Brute-Force Matcher for matching descriptors.
The first 50 matches are drawn on the matchedImage.jpg, but you can adjust this number according to your preference.
Experiment with different pairs of images and explore the possibilities of using SIFT features in your computer vision projects.
