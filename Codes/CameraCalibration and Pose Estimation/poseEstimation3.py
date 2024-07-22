import cv2
import numpy as np

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Actual diameter of the docking station (in meters)
actual_diameter = 0.081

# Focal length of the camera (in pixels)
# This needs to be calibrated beforehand
focal_length = 809.408

while True:
    # Read the current frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold the image to get the LEDs (adjust threshold value if needed)
    # 220, 255
    _, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If enough contours are detected, fit a circle to them
    if len(contours) > 0:
        # Combine all contours into one array
        points = np.concatenate(contours)

        # Fit a circle to the points
        (x, y), r = cv2.minEnclosingCircle(points)

        # Calculate the center of the frame
        center_x = frame.shape[1] // 2
        center_y = frame.shape[0] // 2

        # Calculate the X and Y distances (in pixels)
        distance_x_pixels = x - center_x
        distance_y_pixels = y - center_y

        # Convert the distances from pixels to meters
        distance_x_meters = (distance_x_pixels * actual_diameter) / (2*r)
        distance_y_meters = (distance_y_pixels * actual_diameter) / (2*r)

        # Estimate the distance to the docking station (Z distance)
        perceived_diameter = 2 * r
        distance_z_meters = (actual_diameter * focal_length) / perceived_diameter
    
        # Display the X, Y and Z distances on the frame as labels in different colors
        cv2.putText(frame, f"X Distance: {distance_x_meters:.2f} m", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)  # Green for X
        cv2.putText(frame, f"Y Distance: {distance_y_meters:.2f} m", (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)  # Blue for Y
        cv2.putText(frame, f"Z Distance: {distance_z_meters:.2f} m", (10, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)  # Red for Z

        # Determine the direction to move
        color = (0, 255, 0)  # Green

        # Check for alignment and draw arrows if needed
        if abs(x - center_x) < 10 and abs(y - center_y) < 10:
            color = (0, 0, 255)  # Red - Docking Ready
        else:
            # Draw arrows for x and y directions for alignment guidance
            if x < center_x:
                cv2.arrowedLine(frame, (int(x + r), int(y)), (center_x, int(y)), (255, 0, 0), 2)
            elif x > center_x:
                cv2.arrowedLine(frame, (int(x - r), int(y)), (center_x, int(y)), (255, 0, 0), 2)

            if y < center_y:
                cv2.arrowedLine(frame, (int(x), int(y + r)), (int(x), center_y), (255, 0, 0), 2)
            elif y > center_y:
                cv2.arrowedLine(frame, (int(x), int(y - r)), (int(x), center_y), (255, 0, 0), 2)

        # Draw the circle in the output image
        cv2.circle(frame, (int(x), int(y)), int(r), color, 4)

        # If the docking station is perfectly aligned and the distance is 0.25 meter, display "Ready to dock"
        if color == (0, 0, 255) and abs(distance_z_meters - 0.25) < 0.01:
            cv2.putText(frame, "Ready to dock", (10, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the output frame
    cv2.imshow("Frame", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
