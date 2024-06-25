import cv2
import pytesseract

# Example usage
image_path = './cropped_card.jpg'

def getStatus(image):
    crop_length = 320
    crop_height = 300
    cropped_region = image[250:crop_height, 70:crop_length]
    data= pytesseract.image_to_string(cropped_region,       config='--oem 3 --psm 6',
    lang='jpn') 
    # print(data)
    # cv2.imshow("Status", cropped_region)
    return data

def peroid_of_stay(image):
    crop_length = 560
    crop_height = 390
    cropped_region = image[340:crop_height, 200:crop_length]
    data= pytesseract.image_to_string(cropped_region,       config='--oem 3 --psm 6',lang='jpn') 
    # print(data)
    # cv2.imshow("Peroid of Stay", cropped_region)
    return data


def delivery_date(image):
    crop_length = 560
    crop_height = 470
    cropped_region = image[420:crop_height, 100:crop_length]
    data= pytesseract.image_to_string(cropped_region,       config='--oem 3 --psm 6',lang='jpn') 
    # print(data)
    # cv2.imshow("Peroid of Stay", cropped_region)
    return data

def expiry_date(image):
    crop_length = 560
    crop_height = 550
    cropped_region = image[470:crop_height, 100:crop_length]
    data= pytesseract.image_to_string(cropped_region,       config='--oem 3 --psm 6',lang='jpn') 
    # print(data)
    cv2.imshow("Expiry Date", cropped_region)
    return data


def localize_text(image_path): 
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV) 
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    text_boxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text_boxes.append((x, y, x + w, y + h))
    cv2.destroyAllWindows()
    return text_boxes
def getDob(image):
    crop_length = 320
    crop_height = 150 
    cropped_region = image[80:crop_height, 70:crop_length]
    data= pytesseract.image_to_string(cropped_region,       config='--oem 3 --psm 6',lang='jpn')  
    # cv2.imshow("DOB", cropped_region)
    return data
def getAddress(image): 
    crop_length = 480
    crop_height = 230 
    cropped_region = image[165:crop_height, 40:crop_length]
    data= pytesseract.image_to_string(cropped_region,       config='--oem 3 --psm 6',
    lang='jpn')  
    cv2.imshow("ADDRESS", cropped_region)
    return data
def getName(image): 
    crop_length = 480
    crop_height = 100 
    cropped_region = image[50:crop_height, 70:crop_length]
    data= pytesseract.image_to_string(cropped_region,       config='--oem 3 --psm 6',
    lang='jpn')  
    # cv2.imshow("NAME", cropped_region)
    return data


def getCardNumber(image):
    crop_length = 830
    crop_height = 80 
    cropped_region = image[0:crop_height, 540:crop_length]
    data= pytesseract.image_to_string(cropped_region,       config='--oem 3 --psm 6',
    lang='jpn')  
    cv2.imshow("Card Number", cropped_region)
    return data
    # card name
def crop_and_display(): 
    image = cv2.imread(image_path) 
    card_data={}
    card_data['card_number']=getCardNumber(image)
    card_data['name']=getName(image) 
    # print(card_data)
    card_data['address']=getAddress(image)
    card_data['dob']=getDob(image)
    card_data['status']= getStatus(image)
    card_data['peroid_of_stay']=peroid_of_stay(image)   
    card_data['expiry_date']=expiry_date(image)   
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return card_data

# text_boxes = localize_text(image_path)
# # print("Text boxes coordinates:", text_boxes)

# print(crop_and_display(image_path))


# def perform_ocr(image, text_boxes):
#     # Initialize dictionary to store extracted text and positions
#     extracted_text_dict = {}
    
#     # Perform OCR using Tesseract for each text box
#     for idx, (x1, y1, x2, y2) in enumerate(text_boxes):
#         cropped_image = image[y1:y2, x1:x2]  # Crop the region of interest
#         text = pytesseract.image_to_string(cropped_image,       config='--oem 3 --psm 6',
# lang='jpn')
#         extracted_text_dict[idx] = {
#             'text': text,
#             'bounding_box': (x1, y1, x2, y2)
#         }
 
#     return extracted_text_dict

# # Example usage
# # image = cv2.imread(image_path)
# # extracted_text_dict = perform_ocr(image, text_boxes)

# # Print the extracted texts and their positions
# # for idx, info in extracted_text_dict.items():
# #     print(f"Text #{idx}: {info['text']}")
# #     print(f"Bounding Box: {info['bounding_box']}")
# #     print()
