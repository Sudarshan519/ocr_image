import cv2
import pytesseract

def preprocess_and_ocr(image_path):
    try:
        # Load image
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"Error: Unable to read image at '{image_path}'")
            return None
        
        # Preprocess image (e.g., grayscale conversion, blur, thresholding, etc.)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        # Perform OCR with adjusted Tesseract configuration
        data = pytesseract.image_to_string(thresh_image, config='--oem 3 --psm 6', lang='jpn')
        
        # Print and return extracted text
        print("Extracted Text:", data)
        return data
    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage:
image_path = 'zOCR/rcs/r30a/icropped_card.jpg'
extracted_text = preprocess_and_ocr(image_path)

if extracted_text:
    print("Extracted Text:", extracted_text)
else:
    print("Failed to extract text.")
