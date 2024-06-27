import cv2


# Load the image
def find_face(imagePath,newpath): 
    image = cv2.imread(imagePath)
    # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for displaying with matplotlib

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale (required by the classifier)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Find the largest face based on area (width * height)
    largest_face = None
    max_area = 0

    for (x, y, w, h) in faces:
        area = w * h
        if area > max_area:
            max_area = area
            largest_face = (x, y, w, h)

    # Display the largest face only
    if largest_face is not None:
        x, y, w, h = largest_face
        # Crop the largest face region from the original image
        largest_face_image = image[y-40:y+h+40, x-10:x+w+10]

        # Display the largest face using matplotlib
        # plt.imshow(cv2.cvtColor(largest_face_image, cv2.COLOR_BGR2RGB))
        cv2.imwrite(newpath+'/face3.jpg', largest_face_image)
        
        # plt.axis('off')  # Turn off axis numbers and ticks
        # plt.title('Largest Face')
        # plt.show()
       
    else:
        print("No faces detected or unable to determine the largest face.")

# find_face('zOCR/R14a.jpg')