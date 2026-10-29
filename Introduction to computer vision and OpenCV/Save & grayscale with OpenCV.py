# pip install opencv-python

import cv2

# Load the image

image = cv2.imread('img.jpeg')

# Resize the window to a specific size without resizing the image

# Create a resizable window

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

# Set the window size to 800x500 (width x height)

cv2.resizeWindow('Loaded Image', 800, 500)

# Display the image in the resized window

cv2.imshow('Loaded Image', image)

# Wait for a key press

cv2.waitKey(0)

# Close the window

cv2.destroyAllWindows()

# Print image properties

# Height, Width, Channels

# Height: The number of pixels vertically (1080 rows).

# Width: The number of pixels horizontally (1920 columns).

# Channels: The color layers (3 for Red, Green, Blue).

print(f"Image Dimensions: {image.shape}")

