import cv2
import mediapipe as mp
import pyautogui
from collections import deque
import time

# Initialize MediaPipe
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
tipIds = [4, 8, 12, 16, 20]

# Game button positions (from your screenshot)
BRAKE_POS = (150, 650)   # Brake button center
GAS_POS = (1030, 650)    # Gas button center

# Track state
gas_pressed = False
brake_pressed = False
last_press_time = 0
hold_duration = 0.3  # minimum hold time (seconds)

# Store last few gesture detections for smoothing
gesture_history = deque(maxlen=10)

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5) as hands:
    while True:
        ret, image = video.read()
        if not ret:
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

        gesture = "none"
        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = fingers.count(1)

            if total == 0:
                gesture = "brake"   # ✊
            elif total == 5:
                gesture = "gas"     # ✋
            else:
                gesture = "none"

        # Add gesture to history
        gesture_history.append(gesture)

        stable_gesture = "none"
        if len(gesture_history) == gesture_history.maxlen:
            for g in ["brake", "gas", "none"]:
                if gesture_history.count(g) >= 7:  # must appear in at least 7/10 frames
                    stable_gesture = g
                    break

        current_time = time.time()

        # Apply actions with minimum hold time
        if stable_gesture == "brake":
            cv2.putText(image, "✊ BRAKE", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
            if not brake_pressed:
                pyautogui.moveTo(BRAKE_POS[0], BRAKE_POS[1])
                pyautogui.mouseDown()
                brake_pressed = True
                last_press_time = current_time
            if gas_pressed and (current_time - last_press_time > hold_duration):
                pyautogui.mouseUp()
                gas_pressed = False

        elif stable_gesture == "gas":
            cv2.putText(image, "✋ GAS", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 255, 0), 5)
            if not gas_pressed:
                pyautogui.moveTo(GAS_POS[0], GAS_POS[1])
                pyautogui.mouseDown()
                gas_pressed = True
                last_press_time = current_time
            if brake_pressed and (current_time - last_press_time > hold_duration):
                pyautogui.mouseUp()
                brake_pressed = False

        else:
            if (gas_pressed or brake_pressed) and (current_time - last_press_time > hold_duration):
                pyautogui.mouseUp()
                gas_pressed = False
                brake_pressed = False

        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

# Cleanup
video.release()
cv2.destroyAllWindows()
pyautogui.mouseUp()
