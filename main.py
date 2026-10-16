import cv2

def main():
    # Open the default webcam (usually camera 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Webcam started. Press 'q' to quit.")

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the video frame
        cv2.imshow("Instrument Translation", frame)

        # Quit when the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()