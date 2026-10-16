# Instrument Translation

A computer-vision project exploring a virtual piano played on paper using a phone camera, OpenCV, and MediaPipe.

## Requirements

- Python 3.12
- `pip`
- A phone with a camera and browser
- [ngrok](https://ngrok.com/download) for HTTPS camera access

## Setup

Clone the repository:

```powershell
git clone <repository-url>
cd Instrument-Translation
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

The MediaPipe Hand Landmarker model is included in `models/hand_landmarker.task`.

Install and configure ngrok using its [official documentation](https://ngrok.com/docs/).

## Running

1. Start the server:

   ```powershell
   python phone_server.py
   ```

2. Open a separate terminal and start the HTTPS tunnel:

   ```powershell
   ngrok http 5000
   ```

3. Open the HTTPS forwarding URL displayed by ngrok on your phone.
4. Select **Start Camera** and allow camera access.
5. Press `Q` in the OpenCV window to stop the server.

Keep both the Python server and ngrok running while using the camera.

## Project Structure

- `phone_server.py` — Flask server, frame processing, and hand tracking.
- `phone_camera.html` — Phone camera interface.
- `phone_camera.css` — Interface styling.
- `phone_camera.js` — Camera capture and frame transmission.
- `paper_detector.py` — Paper detection.
- `models/hand_landmarker.task` — MediaPipe hand-tracking model.
- `requirements.txt` — Python dependencies.

## Notes

- Phone camera access requires HTTPS; use the ngrok forwarding URL.
- Do not commit `.venv/`, authentication tokens, or other secrets.
