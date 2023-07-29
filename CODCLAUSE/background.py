import cv2
import numpy as np

def remove_background(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the mask for background removal (assuming the background is close to white)
    lower_white = np.array([200, 200, 200], dtype=np.uint8)
    upper_white = np.array([255, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(image_rgb, lower_white, upper_white)

    # Invert the mask (to keep the foreground, which is not white)
    mask_inv = cv2.bitwise_not(mask)

    # Create an all-white image (for the background)
    white_background = np.ones_like(image_rgb) * 255

    # Apply the mask to the original image and the white background
    foreground = cv2.bitwise_and(image_rgb, image_rgb, mask=mask_inv)
    background = cv2.bitwise_and(white_background, white_background, mask=mask)

    # Combine the foreground and background
    result = cv2.add(foreground, background)

    # Save the result to the output path
    cv2.imwrite(output_path, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))

if __name__ == "__main__":
    input_image_path = "image.jpg.jpg"    # Replace with the path to your input image
    output_image_path = "output_image.jpg"  # Replace with the desired output path

    remove_background(input_image_path, output_image_path)
