✨🚦 gesture-based-driving-simulation ✋🏎️

Control your car simulation with just your hands 🙌 — Brake 🛑 & Accelerate 🏎️ using AI-powered real-time hand gesture recognition 🤖✨.

🌟 Table of Contents

🎯 Motivation & Vision

📖 Introduction

✨ Features

🛠 Tech Stack

📂 Project Structure

⚙️ How It Works

🚀 Installation & Setup (macOS 🍏)

▶️ Usage

📸 Hand Landmarks Explained

🌍 Applications

📈 Future Scope

⚡ Challenges & Learnings

🤝 Contributions

📜 License

💡 Conclusion

🙏 Acknowledgments

🎯 Motivation & Vision 🚀

Human–computer interaction (HCI) has always been defined by devices:
⌨️ Keyboards, 🖱️ Mice, 🎮 Controllers.

But… what if our body itself could be the controller? 🤔

The vision of Gesture-Drive-AI is to remove physical barriers and build an intuitive, touchless interface where machines understand human gestures naturally.

👉 This project is not just about driving games 🎮🚗 — it’s about pushing forward towards:

🕶️ Immersive AR/VR experiences

♿ Accessibility-first interfaces for all users

💡 Smart homes & IoT controlled with gestures

🌍 A future where gestures become a universal language for machines

📖 Introduction 💡

Gesture-Drive-AI is a Python-based project that uses:

Computer Vision (OpenCV) 📸 to process video

MediaPipe Hand Tracking ✋ to detect 21 hand landmarks

DirectKeys Automation ⌨️ to simulate keypresses

Together, they form a gesture-based driving control system where:

✋ Raise hand → Gas 🏎️

✋ Different pose → Brake 🛑

⚡ All in real-time, with low latency and visual feedback overlays.

✨ Features 🌟

🎥 Real-Time Tracking → MediaPipe detects 21 landmarks

✋ Gesture Recognition → Map hand poses to actions

⌨️ Keyboard Input Simulation → No hardware controllers needed

🛑 Brake Gesture & 🏎️ Accelerator Gesture

🖼️ Visual Feedback with OpenCV → Overlays "BRAKE" / "GAS"

⚡ Ultra Responsive → Minimal delay

🔧 Extendable → Add more gestures (e.g., Steering Left/Right)

🕹️ Works with Driving Games → Any game that uses keyboard input

| Technology                 | Purpose                              | Emoji |
| -------------------------- | ------------------------------------ | ----- |
| **Python 🐍**              | Core programming language            | 🟦    |
| **OpenCV 📸**              | Real-time video capture & processing | 🎥    |
| **MediaPipe ✋**            | 21-point hand landmark detection     | 🖐️   |
| **NumPy 🔢**               | Numerical operations                 | 📊    |
| **DirectKeys / PyAuto ⌨️** | Key press simulation                 | 🎮    |
| **Time ⏱️**                | Delay & timing control               | ⌚     |

Gesture-Drive-AI/
│
├── main.py              # 🎯 Core script: CV + gesture mapping
├── directkeys.py        # ⌨️ Key press simulation
├── hand_landmarks.png   # ✋ MediaPipe hand landmark reference
├── step.txt             # 📝 Step-wise gesture logic
└── README.md            # 📖 Documentation

⚙️ How It Works 🔎

Capture Video 🎥 – Webcam feed using OpenCV

Hand Detection ✋ – MediaPipe locates 21 hand points

Gesture Recognition 🔍 – Identify if gesture = Brake or Accelerator

Map to Keypress ⌨️ – DirectKeys simulates keystrokes

Overlay Feedback 🖼️ – OpenCV shows "BRAKE" / "GAS" in green box

Key Release 🔄 – Ensures smooth switching between gestures

📊 Flow:
🖐️ → 📷 → ✋ → 🔎 → ⌨️ → 🚦

🚀 Installation & Setup on macOS 🍏💻

Here’s how to set up and run Gesture-Drive-AI on macOS:

1️⃣ Update Homebrew & Python Environment 🐍
brew update                  # Update Homebrew  
brew install python3         # Install Python3  
python3 --version            # Check Python version  
pip3 --version               # Check pip version  

2️⃣ Create & Activate Virtual Environment 🛠️
python3 -m venv gesture-drive-env   # Create virtual environment  
source gesture-drive-env/bin/activate   # Activate virtual environment  

3️⃣ Clone the Repository 📂
git clone https://github.com/your-username/gesture-drive-ai.git  
cd gesture-drive-ai  

4️⃣ Install Dependencies 📦
pip3 install --upgrade pip setuptools wheel   # Upgrade pip & tools  
pip3 install opencv-python mediapipe numpy    # Install project dependencies  


⚡ Optional (for M1/M2 Macs if cv2 fails):

brew install opencv  
pip3 install opencv-contrib-python  

5️⃣ Allow Webcam Permissions 🎥

On macOS, OpenCV needs camera access:

👉 Go to System Preferences → Security & Privacy → Camera → Enable Python3

Check available cameras:

system_profiler SPCameraDataType  

6️⃣ Run the Program ▶️
python3 main.py  

7️⃣ Test in Driving Simulation 🎮

Open your driving game

Use gestures 🙌 to Brake 🛑 and Accelerate 🏎️

8️⃣ Deactivate Virtual Environment ❌
deactivate  

▶️ Usage 🎯

✋ Show hand in webcam

🟥 Perform Brake Gesture → Activates Brake 🛑

🟩 Perform Accelerator Gesture → Activates Gas 🏎️

🖼️ Watch visual overlay feedback (rectangle + text)

🚦 Enjoy hands-free immersive driving 🎉

📸 Hand Landmarks Explained ✋

MediaPipe tracks 21 landmarks per hand:

0 → Wrist ⌚

4 → Thumb tip 👍

8 → Index fingertip ☝️

12 → Middle fingertip ✌️

16 → Ring fingertip ✋

20 → Pinky fingertip 🤟

📌 See hand_landmarks.png for reference.

🌍 Applications 🔮

🎮 Gaming → AI-driven controller-free gameplay
🕶️ AR/VR → Natural interactions in immersive environments
♿ Accessibility → For people with limited mobility
💡 IoT / Smart Homes → Gesture-controlled appliances
📊 Presentations → Slide navigation using gestures
🎼 Media Control → Play/Pause with hand signs

📈 Future Scope 🚀

🔄 Steering Gesture Controls (Left/Right) ↔️

🤖 Train custom ML gesture models

🙌 Dual-hand gesture support

🎤 Hybrid Voice + Gesture system

🖼️ GUI with live gesture previews

⚡ Challenges & Learnings 💭

✔️ Real-time latency optimization ⚡
✔️ Avoiding false positives in detection 🎯
✔️ Mapping 21 landmarks into simple actions ✋
✔️ Creating a reliable DirectKeys module ⌨️

🤝 Contributions 🙌

We ❤️ contributions!

🍴 Fork repo

🌿 Create branch

💾 Commit changes

🔄 PR for review

📜 License 📑

MIT License ✅ – Free to use, share, and improve.

💡 Conclusion ✨

Gesture-Drive-AI 🚦 = AI 🤖 + Computer Vision 👀 + Human Gestures ✋ → Future Interaction 🚀

This project proves:

🌍 Tech can be touchless & immersive

🎮 Gaming can be next-level fun

♿ Interfaces can be inclusive & accessible

💡 AI can feel human-like

Raise your hand ✋.
Take control 🚗.
Step into the future of interaction.

🙏 Acknowledgments 💐

🎥 OpenCV
 – Real-time CV library

✋ MediaPipe
 – Hand tracking magic

🐍 Python community – Open-source ecosystem

💡 Inspiration from AI + CV + HCI research








## 🔄 New Update (v2) – Smarter & Smoother Control

I recently updated the project to make it **more stable, more adaptive, and more user-friendly** 🚀

### ✨ Key Enhancements:
- 📏 **Resolution-independent control** – works on any screen size  
- ✋ **Improved gesture classification** – detects fingers up/down reliably  
- ⚡ **Debouncing logic** – prevents false triggers with confirm frames & cooldown  
- 🔄 **State machine stability** – smoother transition between Brake 🛑 and Gas 🏎️  
- 🖼️ **Visual UI feedback** – glowing Brake/Gas indicators on screen  
- ✅ **Safe shutdown** – prevents stuck keys on exit  

Check out the updated [`main.py`](main.py) 👈

