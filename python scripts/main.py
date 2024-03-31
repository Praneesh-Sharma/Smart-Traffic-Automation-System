from vehicle_count import count_vehicles
from frame import get_frame
from signal import manage_traffic_lights
import cv2

# Example usage:
# image_path = r'C:\Users\KIIT\Downloads\Vehicle Detection System\data\demo9.jpg'  # Path to the image
# number = count_vehicles(image_path)

def main():
    video_path1 = r'C:\Users\KIIT\Downloads\Vehicle Detection System\data\vid1.avi'
    video_path2 = r'C:\Users\KIIT\Downloads\Vehicle Detection System\data\vid2.avi'
    video_path3 = r'C:\Users\KIIT\Downloads\Vehicle Detection System\data\vid3.avi'
    video_path4 = r'C:\Users\KIIT\Downloads\Vehicle Detection System\data\vid4.avi'
    # frame_number = 5500
    frame_number = 2
    lane = {}

    vid = [video_path1,video_path2,video_path3,video_path4]

    for i in range(4):
        frame, saved_file_path = get_frame(vid[i], frame_number)
        number = count_vehicles(r'C:\Users\KIIT\Downloads\Vehicle Detection System\python scripts\temp.jpg')
        lane[i+1] = number
    
    # for key, value in lane.items():
    #     print(f"{key}: {value}")
        
    manage_traffic_lights(lane)
    

if __name__ == "__main__":
    main()