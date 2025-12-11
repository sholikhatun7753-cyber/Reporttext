import streamlit as st
import base64

st.set_page_config(page_title="Quiz Slide Show", layout="centered")

# --- Jawaban dienkripsi (disembunyikan) ---
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

# --- Session State ---
if "slide" not in st.session_state:
    st.session_state.slide = -1     # -1 untuk halaman identitas
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "nama" not in st.session_state:
    st.session_state.nama = ""
if "kelas" not in st.session_state:
    st.session_state.kelas = ""


# --- Halaman IDENTITAS ---
if st.session_state.slide == -1:
    st.title("📘 Report Text Quiz – Student Identity")

    st.session_state.nama = st.text_input("Nama:")
    st.session_state.kelas = st.text_input("Kelas:")

    if st.button("Start Quiz"):
        if st.session_state.nama == "" or st.session_state.kelas == "":
            st.warning("⚠ Silakan isi nama dan kelas terlebih dahulu.")
        else:
            st.session_state.slide = 0
    st.stop()


# --- Halaman Soal ---
i = st.session_state.slide
q = questions[i]

st.title("📘 Report Text Quiz – Slide Show")
st.write(f"👤 **Nama:** {st.session_state.nama}")
st.write(f"🏫 **Kelas:** {st.session_state.kelas}")
st.markdown("---")

st.subheader(q["question"])

selected = st.radio(
    "Pilih jawaban:",
    list(q["options"].keys()),
    format_func=lambda x: f"{x}. {q['options'][x]}"
)

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

# --- Tombol Next ---
if st.session_state.answered:
    if st.button("Next"):
        st.session_state.slide += 1
        st.session_state.answered = False

# --- Selesai ---
if st.session_state.slide >= len(questions):
    st.balloons()
    st.title("🎉 Quiz Completed!")
    st.subheader(f"👤 Nama: **{st.session_state.nama}**")
    st.subheader(f"🏫 Kelas: **{st.session_state.kelas}**")
    st.markdown("---")
    st.subheader(f"🏆 Final Score: **{st.session_state.score} / {len(questions)*20}**")
    st.stop()
