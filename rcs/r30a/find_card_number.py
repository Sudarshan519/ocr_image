import cv2
import numpy as np
import pytesseract

def preprocess_and_ocr(image_path):
    # Load image
    image = cv2.imread(image_path)
    
    # Define crop region and crop
    crop_length = 980
    crop_height = 80 
    cropped_region = image[0:crop_height, 640:crop_length]
    
    # Convert cropped region to grayscale
    gray = cv2.cvtColor(cropped_region, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray, (10, 10), 0)
    
    # Apply binary thresholding
    _, thresh_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Find contours
    contours, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on the grayscale image
    cv2.drawContours(gray, contours, -1, (0, 255, 0), 2)  # -1 means draw all contours, thickness is 2
    mask = np.zeros_like(gray)
    masked_image = cv2.bitwise_and(gray, mask)
    # Display the preprocessed image with contours
    cv2.imshow('Preprocessed Image', blurred_image)
    
    # Perform OCR on the preprocessed image
    data = pytesseract.image_to_string(blurred_image, config='--oem 3 --psm 6', lang='jpn')
    
    # Print the extracted text
    print("Extracted Card Number:", data)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return data

# Example usage:
image_path = 'zOCR/rcs/r19a.jpg'
extracted_text = preprocess_and_ocr(image_path)
