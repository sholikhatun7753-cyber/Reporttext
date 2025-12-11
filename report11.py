import streamlit as st

st.set_page_config(page_title="Quiz Report Text", layout="centered")

# --- DATA SOAL ---
questions = [
    {
        "question": "1. What is the main idea of the second paragraph?",
        "options": [
            "A. Fried Rice is a truly delicious",
            "B. Fried Rice is a truly complete meal",
            "C. Fried Rice is a truly nusantara food",
            "D. Fried Rice is a truly best choice"
        ],
        "answer": "B"
    },
    {
        "question": "2. The word 'advantages' in paragraph 3 has the closest meaning to…",
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

# --- STATE: Menyimpan slide & jawaban user ---
if "slide" not in st.session_state:
    st.session_state.slide = 0

if "answers" not in st.session_state:
    st.session_state.answers = [""] * len(questions)

# --- FUNGSIONALITAS SLIDE ---
def next_slide():
    if st.session_state.slide < len(questions) - 1:
        st.session_state.slide += 1

def previous_slide():
    if st.session_state.slide > 0:
        st.session_state.slide -= 1

def restart_quiz():
    st.session_state.slide = 0
    st.session_state.answers = [""] * len(questions)

# --- SLIDE TERAKHIR: TAMPILKAN HASIL ---
if st.session_state.slide == len(questions):
    st.title("🎉 Quiz Completed!")
    st.subheader("Your Score")

    score = 0
    for i, q in enumerate(questions):
        if st.session_state.answers[i] == q["answer"]:
            score += 100 // len(questions)

    st.write(f"### ⭐ Your score: **{score} / 100**")

    st.write("---")
    st.subheader("Answer Key")
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** Correct answer = {q['answer']} | Your answer = {st.session_state.answers[i]}")

    st.button("🔄 Restart Quiz", on_click=restart_quiz)

    st.stop()

# --- TAMPILKAN SLIDE SOAL ---
q = questions[st.session_state.slide]

st.title("📚 Report Text Quiz (Slideshow Mode)")
st.write(f"### Slide {st.session_state.slide + 1} of {len(questions)}")

st.write(f"**{q['question']}**")

selected = st.radio(
    "Choose your answer:",
    options=["A", "B", "C", "D"],
    index=["A", "B", "C", "D"].index(st.session_state.answers[st.session_state.slide]) if st.session_state.answers[st.session_state.slide] else 0,
    key=f"radio_{st.session_state.slide}"
)

# Simpan jawaban user
st.session_state.answers[st.session_state.slide] = selected

# Navigasi Slide
col1, col2 = st.columns(2)

with col1:
    if st.session_state.slide > 0:
        st.button("⬅ Previous", on_click=previous_slide)

with col2:
    if st.session_state.slide < len(questions) - 1:
        st.button("Next ➡", on_click=next_slide)
    else:
        st.button("Finish Quiz 🎉", on_click=lambda: st.session_state.update({"slide": len(questions)}))
