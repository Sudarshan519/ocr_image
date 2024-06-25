import cv2
import numpy as np

# Path to your image file
image_path = './removed.jpg'


def resizeImg(image):
    def resize_to_fixed_card_size(image_path, card_width_mm=85.60, card_height_mm=53.98, dpi=300):
        card_width_px = int(card_width_mm * dpi / 25.4)  # mm to inches to pixels
        card_height_px = int(card_height_mm * dpi / 25.4)
        
        # Load the image
        # image = cv2.imread(image_path)
        
        # Resize the image to the fixed card size while maintaining aspect ratio
        resized_image = cv2.resize(image, (card_width_px, card_height_px))
        
        # Display the resized image
        # cv2.imshow("Resized Image", resized_image)
        # cv2.imwrite('cropped_card.jpg', card_cropped)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return resized_image

    # Load image
    # Load image
    image = cv2.imread(image_path)
    original_image = image.copy()  # Make a copy for visualization

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables to store largest contour and its bounding box
    largest_contour = None
    max_area = 0
    card_contour = None

    # Loop over the contours
    for contour in contours:
        # Approximate the contour to a polygon
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        
        # Ensure the contour is rectangular and large enough
        if len(approx) == 4:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                largest_contour = approx

    # If a rectangular contour is found, proceed to crop the card
    if largest_contour is not None:
        # Convert the largest contour back to integer coordinates and draw it on the original image
        largest_contour = largest_contour.reshape(-1, 2).astype(np.int32)
        cv2.drawContours(original_image, [largest_contour], -1, (0, 255, 0), 2)
        
        # Get bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Crop the card from the original image
        card_cropped = original_image[y:y+h, x:x+w]

        # Display the original image with the detected card contour and cropped card
        # cv2.imshow('Card Detection and Cropping', original_image)
        # cv2.imshow('Cropped Card', card_cropped)
        # cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save the cropped card image if needed
        cv2.imwrite('cropped_card.jpg', card_cropped)
    else:
        print("No rectangular contour (card) found in the image.")

    image = cv2.imread('./cropped_card.jpg')
    resizedImg=resize_to_fixed_card_size(image)
    return resizedImg