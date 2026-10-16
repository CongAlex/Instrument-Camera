
import threading

import cv2
import numpy as np
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


latest_frame = None
frame_lock = threading.Lock()


@app.post("/frame")
def receive_frame():
    global latest_frame

    # Decode the incoming JPEG bytes into an OpenCV image.
    image_bytes = np.frombuffer(request.get_data(), dtype=np.uint8)
    frame = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

    if frame is None:
        return "Invalid image", 400

    with frame_lock:
        latest_frame = frame

    return "OK", 200


def run_server():
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True,
    )


if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()

    print("Waiting for phone camera frames. Press Q to quit.")

    try:
        while True:
            with frame_lock:
                frame = (
                    latest_frame.copy()
                    if latest_frame is not None
                    else None
                )

            if frame is not None:
                cv2.imshow("Phone Camera Feed", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cv2.destroyAllWindows()
