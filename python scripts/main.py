from vehicle_count import count_vehicles
from frame import get_frame
import cv2

# Example usage:
# image_path = r'C:\Users\KIIT\Downloads\Vehicle Detection System\data\demo9.jpg'  # Path to the image
# number = count_vehicles(image_path)

def main():
    video_path = r'C:\Users\KIIT\Downloads\Vehicle Detection System\data\vid1.mp4'
    frame_number = 5500
    # frame_number = 6500

    # Call the function to get the frame
    frame, saved_file_path = get_frame(video_path, frame_number)

    # if frame is not None:
    #     cv2.imshow('Resized Frame', frame)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    # else:
    #     print('Error: Failed to retrieve frame.')

    number = count_vehicles(r'C:\Users\KIIT\Downloads\Vehicle Detection System\python scripts\temp.jpg')

if __name__ == "__main__":
    main()
