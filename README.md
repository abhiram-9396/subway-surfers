# 🏃 Subway Surfers Game Using Hand Gestures

An innovative undergraduate project enabling hands-free gameplay of **Subway Surfers** using **hand gestures**, built with **Python** and **OpenCV**. This project showcases real-time palm detection and hand landmarking techniques to control the game seamlessly without physical controllers.

## 🚀 Features

- **Hands-Free Gameplay:** Control the player using only hand movements.
- **Real-Time Hand Tracking:** Detect and recognize palm gestures with low latency.
- **Optimized Performance:** Engineered to minimize processing delays for smoother interaction.
- **Computer Vision Powered:** Built using OpenCV’s advanced image processing and hand landmarking models.
- **Research-Driven:** Based on extensive analysis of computer vision techniques from multiple research papers.
- **Published Research:** Findings presented and published at **ICDECT-2022**.

## 🛠️ Built With

- **Python 3.x** – Core programming language
- **OpenCV** – Real-time computer vision library
- **MediaPipe** (optional extension) – For efficient hand landmark detection
- **PyAutoGUI** – To simulate keyboard/mouse actions based on gestures

## 📸 Demo

[![Subway Surfers Game Demo](https://img.youtube.com/vi/y8y2KbotnZo/hqdefault.jpg)](https://youtu.be/y8y2KbotnZo)

> _Click the image above to watch the demo video on YouTube!_


## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhiram-9396/subway-surfers.git
   cd subway-surfers
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python3 main.py
   ```

## 🔍 How It Works

- The webcam captures the real-time video stream.
- **OpenCV** processes each frame to detect palm gestures.
- Hand landmark detection maps the number of fingers shown to game actions:
  - Jump (one finger)
  - Roll (two fingers)
  - Move right (Three Fingers)
  - Move left (Four Fingers)
  
- **PyAutoGUI** triggers the respective keyboard events to control the Subway Surfers player.

## 📚 Research Contributions

- Conducted an in-depth review of multiple computer vision and hand-tracking research papers.
- Implemented low-latency gesture recognition techniques based on research insights.
- Published a research paper titled _"Subway Surfers Game Using Hand Gestures"_ at **ICDECT-2022**.

## ✨ Future Enhancements

- Support for dynamic gestures like swipe gestures for multiple moves.
- Multiplayer gesture-controlled versions.
- Integrate with other games and VR platforms.

## 🙌 Acknowledgments

- Thanks to the OpenCV and computer vision community.
- Special thanks to ICDECT-2022 for providing the platform to present this work.

---

**Note:** This project was built purely for academic and experimental purposes.
