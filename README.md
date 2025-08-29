gesture-based-driving-simulation 🚦✋🏎️

An AI-powered hand gesture recognition system that enables touchless driving simulation controls using Computer Vision, OpenCV, MediaPipe, and Python automation. This project demonstrates how real-time hand tracking can be mapped to keyboard inputs to simulate driving functions such as Brake 🛑 and Accelerator 🏎️.

📖 Introduction

In today’s world of Artificial Intelligence (AI) and Computer Vision (CV), gesture recognition is rapidly becoming one of the most exciting innovations. From gaming consoles to augmented reality (AR) and virtual reality (VR) headsets, to accessibility technologies, the ability to interact with machines without physical contact opens the door to endless possibilities.

This project, Gesture-Drive-AI, is designed as a real-time driving control simulator powered by hand gestures. Instead of relying on a physical steering wheel, joystick, or keyboard, users can simply raise their hand and use gestures to control acceleration and braking in a simulation.

The system uses MediaPipe for tracking 21 different hand landmarks, OpenCV for image processing and visualization, and a custom-built DirectKeys module to simulate keyboard inputs in Python. Together, these technologies provide an immersive, touchless, and innovative way of interacting with simulation environments.

✨ Key Features

🎥 Real-time Hand Tracking: Detects 21 hand landmarks with high accuracy.

✋ Gesture Recognition: Recognizes custom gestures for “Brake” 🛑 and “Accelerator” 🏎️.

⌨️ Keyboard Control Mapping: Simulates key presses using a custom directkeys.py.

⚡ Low Latency: Designed for real-time responsiveness with minimal delay.

🎮 Game/Simulation Compatibility: Can be integrated with any PC driving simulation that uses keyboard inputs.

🖼️ Visual Feedback: Overlays bounding boxes and labels (Brake / Gas) using OpenCV.

🛠️ Lightweight & Extendable: Easy to expand with new gestures and actions.

🛠️ Tech Stack

This project leverages the following tools and libraries:

Python 🐍 → Core programming language.

OpenCV 📸 → Image processing, drawing overlays, and real-time video handling.

MediaPipe ✋ → Hand landmark detection with 21 reference points.

NumPy 🔢 → Data handling and numerical processing.

DirectKeys / PyAuto ⌨️ → Simulates keyboard keypresses.

Time ⏱️ → Handling delays and timing of inputs.

📂 Project Structure
Gesture-Drive-AI/
│
├── main.py              # Main execution file (real-time hand tracking + gesture mapping)
├── directkeys.py        # Custom module for simulating key presses
├── hand_landmarks.png   # Reference diagram of 21 MediaPipe hand landmarks
├── step.txt             # Detailed step-wise processing logic
└── README.md            # Project documentation

⚙️ Project Workflow

Video Capture 🎥

The system captures frames from the webcam using OpenCV.

Hand Landmark Detection ✋

MediaPipe processes each frame and identifies 21 unique hand landmarks.

Gesture Processing 🔎

Based on landmark positions, the system determines whether the hand gesture matches “Brake” 🛑 or “Accelerator” 🏎️.

Key Mapping ⌨️

Using directkeys.py, the detected gesture is mapped to a simulated key press. For example:

Left arrow ⬅️ → Brake

Right arrow ➡️ → Accelerator

Visual Feedback 🖼️

OpenCV overlays green rectangles and text labels (BRAKE / GAS) on the screen to show the active control.

Key Release Logic 🛑

When no gesture is detected, the system ensures that previously pressed keys are released to avoid stuck inputs.

🚀 Installation

Clone the repository

git clone https://github.com/your-username/gesture-drive-ai.git
cd gesture-drive-ai


Install dependencies

pip install opencv-python mediapipe numpy


Run the main script

python main.py


Start your driving simulation game 🎮 and control it with gestures!

▶️ Usage

Show your hand in front of the webcam.

Perform the gesture for Brake 🛑 or Accelerator 🏎️.

Watch the on-screen overlay (OpenCV rectangle with labels).

The driving simulation/game will respond to your gesture as a keypress.

📸 Hand Landmarks Reference

MediaPipe provides 21 hand landmarks. Each landmark represents a specific point on the hand (e.g., wrist, finger joints, fingertips).

Example landmarks:

0 → Wrist

4 → Thumb tip

8 → Index fingertip

12 → Middle fingertip

20 → Pinky fingertip

(See hand_landmarks.png for the full diagram.)

🌍 Applications

Although developed for a driving simulation, this project can be extended to various domains:

🎮 Gaming → Touchless control for immersive experiences.

🕶️ AR/VR → Natural gesture-based interactions in virtual environments.

♿ Accessibility → Assistive tech for people with mobility limitations.

💡 IoT & Smart Interfaces → Gesture-based controls for smart devices and appliances.

🎤 Presentations & Media Control → Slide navigation and media playback via hand gestures.

📈 Future Improvements

Add steering wheel gestures (left/right control).

Incorporate machine learning classifiers for custom gesture recognition.

Support multi-hand gestures for more control options.

Expand to voice + gesture hybrid control.

Improve UI/UX with on-screen gesture guides.

🤝 Contribution

Contributions are welcome! 🎉 If you’d like to add new gestures, optimize performance, or extend functionality, feel free to:

Fork this repo

Create a new branch (feature-new-gesture)

Commit your changes

Submit a pull request 🚀

📜 License

This project is licensed under the MIT License – feel free to use and modify it for your own projects.

💡 Conclusion

Gesture-Drive-AI showcases how AI + Computer Vision + Automation can come together to redefine human-computer interaction. By enabling real-time gesture-based controls, this project not only enhances gaming simulations but also provides a stepping stone toward touchless, immersive, and accessible interfaces across industries.

The future is gesture-driven, intelligent, and interactive 🌍✨
