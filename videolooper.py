import cv2


def play_video_loop(video_path, width=None, height=None):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    # Get original video dimensions
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calculate new dimensions if width or height is provided
    if width is None and height is None:
        width, height = original_width, original_height
    elif width is None:
        aspect_ratio = original_width / original_height
        width = int(height * aspect_ratio)
    elif height is None:
        aspect_ratio = original_width / original_height
        height = int(width / aspect_ratio)

    # Create a named window
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

    # Set the window to stay on top
    cv2.setWindowProperty('Video', cv2.WND_PROP_TOPMOST, 1)

    # Resize the window
    cv2.resizeWindow('Video', width, height)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If we've reached the end of the video, reset to the beginning
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Resize the frame
        resized_frame = cv2.resize(frame, (width, height))

        # Display the frame
        cv2.imshow('Video', resized_frame)

        # Press 'q' to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()


# Your specific video path
video_path = '/Users/anhthientbd/PycharmProjects/video looper/youtube_AR24XK1WAb8_1920x1080_h264.mp4'

# Call the function with desired width and height
play_video_loop(video_path, width=200, height=100)  # Change these values as needed