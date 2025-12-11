import streamlit as st
import base64

st.set_page_config(page_title="Quiz Slide Show", layout="centered")

# --- Jawaban dienkripsi (tidak terlihat jelas) ---
encoded_keys = [
    base64.b64encode("B".encode()).decode(), 
    base64.b64encode("C".encode()).decode(),
    base64.b64encode("D".encode()).decode()
]

def get_answer(i):
    return base64.b64decode(encoded_keys[i]).decode()

# --- Data soal ---
questions = [
    {
        "question": "1. What is the main idea of the second paragraph?",
        "options": {
            "A": "Fried Rice is a truly delicious",
            "B": "Fried Rice is a truly complete meal",
            "C": "Fried Rice is a truly nusantara food",
            "D": "Fried Rice is a truly best choice"
        }
    },
    {
        "question": "2. The word 'advantages' in paragraph 3 has closest meaning...",
        "options": {
            "A": "impact",
            "B": "purpose",
            "C": "beneficial",
            "D": "loss"
        }
    },
    {
        "question": "3. What topping can be added on fried rice?",
        "options": {
            "A": "fries",
            "B": "coco chip",
            "C": "butter",
            "D": "vegetables, scrambled eggs, shredded chicken"
        }
    }
]

# --- State untuk slide ---
if "slide" not in st.session_state:
    st.session_state.slide = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

# --- UI Judul ---
st.title("📘 Report Text Quiz – Slide Show Mode")

# --- Menampilkan pertanyaan sesuai slide ---
i = st.session_state.slide
q = questions[i]
st.subheader(q["question"])

selected = st.radio("Choose one answer:", list(q["options"].keys()), format_func=lambda x: f"{x}. {q['options'][x]}")

# --- Tombol Cek Jawaban ---
if st.button("Check Answer"):
    if not st.session_state.answered:
        correct = get_answer(i)
        if selected == correct:
            st.success("✔ Correct! Good job!")
            st.session_state.score += 20
        else:
            st.error("✘ Wrong answer!")
        st.session_state.answered = True

# --- Tombol Next Slide ---
if st.session_state.answered:
    if st.button("Next"):
        st.session_state.slide += 1
        st.session_state.answered = False

# --- Jika selesai ---
if st.session_state.slide >= len(questions):
    st.balloons()
    st.title("🎉 Quiz Completed!")
    st.subheader(f"Your Final Score: **{st.session_state.score} / {len(questions)*20}**")
    st.stop()

