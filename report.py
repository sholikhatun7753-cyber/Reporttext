import tkinter as tk
from tkinter import messagebox
import pygame
import datetime

# ----------- SOUND SYSTEM SETUP -----------
pygame.mixer.init()

# Files (pastikan ada di folder yang sama)
sound_correct = "sound_good.wav"
sound_wrong = "sound_bad.wav"
background_music = "background_music.mp3"


def play_correct():
    pygame.mixer.music.load(sound_correct)
    pygame.mixer.music.play()


def play_wrong():
    pygame.mixer.music.load(sound_wrong)
    pygame.mixer.music.play()


def play_background_music():
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play(-1)  # LOOP FOREVER


# ----------- QUESTIONS DATA -----------
questions = [
    {
        "question": "1. What is the main idea of the second paragraph?",
        "options": [
            "A. Fried Rice is a truly delicious",
            "B. Fried Rice is a truly complete meal",
            "C. Fried Rice is a truly Nusantara food",
            "D. Fried Rice is a truly best choice"
        ],
        "answer": "B"
    },
    {
        "question": "2. Choosing Fried Rice for breakfast offers strategic advantages.\nThe word 'advantages' has closest meaning...",
        "options": [
            "A. impact",
            "B. purpose",
            "C. beneficial",
            "D. loss"
        ],
        "answer": "C"
    },
    {
        "question": "3. What topping can be added on fried rice?",
        "options": [
            "A. fries",
            "B. coco chip",
            "C. butter",
            "D. vegetables, scrambled eggs, shredded chicken"
        ],
        "answer": "D"
    }
]

# ----------- GUI SETUP -----------
root = tk.Tk()
root.title("English Report Text Quiz")
root.geometry("750x450")

# ----------- THEME (BACKGROUND + COLORS) -----------
root.configure(bg="#2E4053")  # DARK BLUEish background

font_question = ("Arial", 17, "bold")
font_option = ("Arial", 15)
font_button = ("Arial", 14, "bold")

fg_color = "white"       # text color
button_color = "#5DADE2"  # light blue
button_fg = "black"

# ----------- STATE CONTROL -----------
current_slide = 0
score = 0
selected_answer = tk.StringVar()

# ----------- GUI ELEMENTS -----------
question_label = tk.Label(root, text="", font=font_question,
                          wraplength=680, bg="#2E4053", fg=fg_color)
question_label.pack(pady=30)

radio_buttons = []


def create_radio_buttons():
    global radio_buttons
    for btn in radio_buttons:
        btn.destroy()

    radio_buttons = []
    for option in questions[current_slide]["options"]:
        rb = tk.Radiobutton(root, text=option,
                            variable=selected_answer,
                            value=option[0],
                            font=font_option,
                            anchor="w",
                            justify="left",
                            bg="#2E4053",
                            fg=fg_color,
                            selectcolor="#1B2631")
        rb.pack(fill="x", padx=60)
        radio_buttons.append(rb)


# ----------- LOAD SLIDE FUNCTION -----------
def load_slide():
    selected_answer.set("")
    question_label.config(text=questions[current_slide]["question"])
    create_radio_buttons()


# ----------- SAVE SCORE FUNCTION -----------
def save_score_to_file(score):
    with open("score_history.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Score: {score}/{len(questions)}\n")


# ----------- NEXT FUNCTION -----------
def next_slide():
    global current_slide, score

    if selected_answer.get() == "":
        messagebox.showwarning("Warning", "Please choose an answer!")
        return

    correct = questions[current_slide]["answer"]

    if selected_answer.get() == correct:
        play_correct()
        score += 1
    else:
        play_wrong()

    current_slide += 1

    if current_slide >= len(questions):
        show_result()
    else:
        load_slide()


# ----------- SHOW FINAL RESULT -----------
def show_result():
    save_score_to_file(score)
    messagebox.showinfo("Quiz Finished",
                        f"Your Score: {score}/{len(questions)}\n\nScore saved to file!")
    root.destroy()


# ----------- NEXT BUTTON -----------
next_button = tk.Button(root, text="Next ➜", font=font_button,
                        bg=button_color, fg=button_fg,
                        command=next_slide)
next_button.pack(pady=25)

# ----------- START QUIZ -----------
play_background_music()
load_slide()

root.mainloop()
