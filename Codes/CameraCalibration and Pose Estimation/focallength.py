import pickle

# Load the camera calibration data (assuming you saved it as "calibration.pkl")
with open('calibration.pkl', 'rb') as f:
  cameraMatrix, dist = pickle.load(f)

# Focal length is usually represented by the first two elements in the diagonal of the camera matrix
focal_length_x = cameraMatrix[0, 0]  # Focal length in x-direction (pixels)
focal_length_y = cameraMatrix[1, 1]  # Focal length in y-direction (pixels)

print("Focal Length (x-direction):", focal_length_x, "pixels")
print("Focal Length (y-direction):", focal_length_y, "pixels")

# Assuming square pixels (often the case), calculate the average focal length
average_focal_length = (focal_length_x + focal_length_y) / 2.0
print("Average Focal Length:", average_focal_length, "pixels")
