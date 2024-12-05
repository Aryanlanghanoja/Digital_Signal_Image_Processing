import cv2


def perform_gray_level_operation(image, operation):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform the desired gray level operation
    if operation == 'contrast':
        # Perform contrast adjustment
        contrast_image = cv2.equalizeHist(gray_image)
        processed_image = cv2.cvtColor(contrast_image, cv2.COLOR_GRAY2BGR)
    elif operation == 'brightness':
        # Perform brightness correction
        alpha = 1.5  # brightness factor
        processed_image = cv2.convertScaleAbs(gray_image, alpha=alpha)
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_GRAY2BGR)
    elif operation == 'thresholding':
        # Perform image thresholding
        _, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        processed_image = cv2.cvtColor(threshold_image, cv2.COLOR_GRAY2BGR)
    else:
        print("Invalid operation. Available operations: 'contrast', 'brightness', 'thresholding'")
        return None

    return processed_image

# Load the input image
image_path = './Images.jpg'
input_image = cv2.imread(image_path)

# Perform gray level operation
operation_type = 'contrast'  # Change this to the desired operation: 'contrast', 'brightness', 'thresholding'
output_image = perform_gray_level_operation(input_image, operation_type)

if output_image is not None:
    # Display the processed image
    cv2.imshow('Processed Image', output_image)
    cv2.waitKey(0)

    # Save the processed image (optional)
    output_path = 'output_image.jpg'
    cv2.imwrite(output_path, output_image)
    print(f"Processed image saved at: {output_path}")
