import cv2
import os

def extract_frames(video_path, output_folder):
    """
    Extracts all frames from a video file and saves them as images.
    
    Args:
        video_path (str): The path to the input .mov file.
        output_folder (str): The directory where images will be saved.
    """
    
    # 1. Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created directory: {output_folder}")

    # 2. Load the video
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Get total frame count (for progress tracking)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames to extract: {total_frames}")

    frame_count = 0

    while True:
        # 3. Read a frame
        success, frame = cap.read()

        # If no frame is returned, we've reached the end of the video
        if not success:
            break

        # 4. Save the frame
        # We use :05d to pad with zeros (e.g., frame_00001.jpg) for proper sorting
        output_filename = os.path.join(output_folder, f"frame_{frame_count:05d}.jpg")
        
        # You can change '.jpg' to '.png' for lossless quality (but larger file sizes)
        cv2.imwrite(output_filename, frame)

        frame_count += 1

        # Optional: Print progress every 100 frames to avoid spamming console
        if frame_count % 100 == 0:
            print(f"Extracted {frame_count}/{total_frames} frames...")

    # 5. Release resources
    cap.release()
    print(f"Done! Successfully extracted {frame_count} images to '{output_folder}'.")

# --- usage ---
if __name__ == "__main__":
    # Replace these with your actual file paths
    input_video = "my_video.mov" 
    output_dir = "extracted_frames"

    extract_frames(input_video, output_dir)