pip install torch --upgrade

from ultralytics import YOLO
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from ultralytics import settings
from PIL import Image
from numpy import asarray



# Load the image
dir = "mobil1.jpg"
image = Image.open(dir)
image = image.convert('RGB')
# plt.axis('off')
# plt.imshow(image)
# Load YOLO model
detector = YOLO('yolov8n.pt')
# Run object detection on the image
results = detector(dir)
# Function to draw boxes only for cars
def draw_yolo_boxes_for_cars(result_list):
    # Load the image
    data = plt.imread(dir)  # Directly using 'a.jpg' as the filename

    # Plot the image
    plt.imshow(data)

    # Get the context for drawing boxes
    ax = plt.gca()

    # Initialize object count
    car_count = 0

    # Plot each detection result
    for result in result_list:
        # YOLO returns a boxes attribute which contains all bounding boxes and their labels
        for box in result.boxes:
            # Get the label index for the detected object
            label_index = int(box.cls[0])

            # Convert the label index to its string representation (e.g., "car", "bus", etc.)
            label = detector.model.names[label_index]

            # Check if the detected object is a car
            if label == 'car':
                # Get bounding box coordinates (x1, y1, x2, y2)
                x1, y1, x2, y2 = box.xyxy[0]

                # Calculate width and height
                width = x2 - x1
                height = y2 - y1

                # Create a rectangle for the bounding box
                rect = plt.Rectangle((x1, y1), width, height, fill=False, color='yellow')

                # Draw the bounding box
                ax.add_patch(rect)

                # Increment the car count
                car_count += 1

    # Show the plot
    plt.show()

    # Return the total number of detected cars
    return car_count

# # Call the function to draw boxes for cars
car_count = draw_yolo_boxes_for_cars(results)

# # Print the total number of cars detected
print(f"Total number of cars detected:{car_count}")
