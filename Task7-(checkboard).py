import cv2
import numpy as np
def create_checkerboard():
    checkerboard = np.zeros((4, 4), dtype=np.uint8)
    checkerboard[::2, ::2] = 255  # White squares
    checkerboard[1::2, 1::2] = 255  # White squares
    return checkerboard

# Create a VideoWriter object to save the video
out = cv2.VideoWriter('checkerboard_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, (160, 160))

# Main loop to create the video frames
for _ in range(8):  # Create 8 frames (4 seconds)
    checkerboard = create_checkerboard()

    # Invert colors
    inverted_checkerboard = cv2.bitwise_not(checkerboard)

    # Resize the checkerboard for visualization
    resized_checkerboard = cv2.resize(inverted_checkerboard, (160, 160), interpolation=cv2.INTER_NEAREST)

    # Convert to BGR format for OpenCV
    resized_checkerboard_bgr = cv2.cvtColor(resized_checkerboard, cv2.COLOR_GRAY2BGR)

    # Write the frame to the video
    out.write(resized_checkerboard_bgr)

# Release the VideoWriter object
out.release()