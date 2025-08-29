import cv2
import mediapipe as mp
import pyautogui
import time

# ---------- Config ----------
BASE_W, BASE_H = 1181, 768
BRAKE_POS_REL = (150/BASE_W, 670/BASE_H)
GAS_POS_REL   = (1030/BASE_W, 670/BASE_H)

CONFIRM_FRAMES = 2
DROPOUT_TOLERANCE = 6
COOLDOWN_MS = 120
SHOW_DEBUG = True

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
TIP_IDS = [4, 8, 12, 16, 20]

SCREEN_W, SCREEN_H = pyautogui.size()

def get_scaled_positions():
    brake = (int(BRAKE_POS_REL[0] * SCREEN_W), int(BRAKE_POS_REL[1] * SCREEN_H))
    gas   = (int(GAS_POS_REL[0]   * SCREEN_W), int(GAS_POS_REL[1]   * SCREEN_H))
    return brake, gas

def classify_gesture(lm_list):
    if not lm_list:
        return "none"

    def finger_up(tip_id):
        return lm_list[tip_id][2] < lm_list[tip_id - 2][2]

    non_thumb_up = sum(1 for i in range(1, 5) if finger_up(TIP_IDS[i]))

    if non_thumb_up >= 3:
        return "gas"
    elif non_thumb_up == 0:
        return "brake"
    else:
        return "none"

def press_down(pos):
    pyautogui.mouseDown(x=pos[0], y=pos[1])

def release_at(pos):
    pyautogui.mouseUp(x=pos[0], y=pos[1])

state = "idle"
candidate = "idle"
candidate_count = 0
absent_frames = 0
last_transition = 0.0

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5) as hands:
    while True:
        ok, frame = video.read()
        if not ok:
            break

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb.flags.writeable = False
        results = hands.process(rgb)
        rgb.flags.writeable = True

        lm_list = []
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            h, w, _ = frame.shape
            for idx, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((idx, cx, cy))
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)

        raw_gesture = classify_gesture(lm_list)
        now = time.time()
        BRAKE_POS, GAS_POS = get_scaled_positions()

        if lm_list:
            absent_frames = 0
            effective_gesture = raw_gesture
        else:
            absent_frames += 1
            if state in ("gas", "brake") and absent_frames <= DROPOUT_TOLERANCE:
                effective_gesture = state
            else:
                effective_gesture = "none"

        target = (
            "gas" if effective_gesture == "gas" else
            "brake" if effective_gesture == "brake" else
            "idle"
        )

        if target == candidate:
            candidate_count += 1
        else:
            candidate = target
            candidate_count = 1

        if candidate_count >= CONFIRM_FRAMES and (now - last_transition) * 1000 >= COOLDOWN_MS:
            if state != candidate:
                if state == "gas":
                    release_at(GAS_POS)
                elif state == "brake":
                    release_at(BRAKE_POS)

                if candidate == "gas":
                    press_down(GAS_POS)
                elif candidate == "brake":
                    press_down(BRAKE_POS)

                state = candidate
                last_transition = now

        if SHOW_DEBUG:
            # Draw Brake button
            color_brake = (0, 0, 255)
            if state == "brake":
                cv2.circle(frame, BRAKE_POS, 50, color_brake, -1)  # filled
                cv2.circle(frame, BRAKE_POS, 70, color_brake, 4)   # glow outline
            else:
                cv2.circle(frame, BRAKE_POS, 40, color_brake, 3)

            cv2.putText(frame, "BRAKE", (BRAKE_POS[0]-50, BRAKE_POS[1]-80),
                        cv2.FONT_HERSHEY_DUPLEX, 1.0, color_brake, 3)

            # Draw Gas button
            color_gas = (0, 255, 0)
            if state == "gas":
                cv2.circle(frame, GAS_POS, 50, color_gas, -1)
                cv2.circle(frame, GAS_POS, 70, color_gas, 4)
            else:
                cv2.circle(frame, GAS_POS, 40, color_gas, 3)

            cv2.putText(frame, "GAS", (GAS_POS[0]-30, GAS_POS[1]-80),
                        cv2.FONT_HERSHEY_DUPLEX, 1.0, color_gas, 3)

        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
try:
    pyautogui.mouseUp()
except:
    pass
