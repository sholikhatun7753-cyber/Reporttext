import streamlit as st

st.set_page_config(page_title="Quiz Report Text", layout="centered")

# ======== CUSTOM STYLE (WARNA MENARIK) ==========
page_bg = """
<style>
    body {
        background: linear-gradient(135deg, #8EC5FC 0%, #E0C3FC 100%) !important;
    }
    .quiz-box {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 18px rgba(0,0,0,0.15);
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #6C5CE7;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #4B4AE1;
        transform: scale(1.05);
        cursor: pointer;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ======== DATA SOAL ==========
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
    },
    {
        "question": "4. What is the purpose of the text?",
        "options": [
            "A. to describe about fried rice",
            "B. to describe about my breakfast menu",
            "C. to describe my favourite menu",
            "D. to describe about food"
        ],
        "answer": "A"
    },
    {
        "question": "5. What topping can be added on fried rice?",
        "options": [
            "A. fries",
            "B. coco chip",
            "C. butter",
            "D. vegetables, scrambled eggs, shredded chicken"
        ],
        "answer": "D"
    }
]

# ======== STATE ==========
if "slide" not in st.session_state:
    st.session_state.slide = -1   # mulai dari form identitas

if "answers" not in st.session_state:
    st.session_state.answers = [""] * len(questions)

if "nama" not in st.session_state:
    st.session_state.nama = ""

if "kelas" not in st.session_state:
    st.session_state.kelas = ""

# ======== FUNGSI ==========
def start_quiz():
    if st.session_state.nama and st.session_state.kelas:
        st.session_state.slide = 0

def next_slide():
    if st.session_state.slide < len(questions) - 1:
        st.session_state.slide += 1

def previous_slide():
    if st.session_state.slide > 0:
        st.session_state.slide -= 1

def restart_quiz():
    st.session_state.slide = -1
    st.session_state.answers = [""] * len(questions)
    st.session_state.nama = ""
    st.session_state.kelas = ""

# ======== FORM IDENTITAS SISWA ==========
if st.session_state.slide == -1:
    st.markdown("<div class='quiz-box'>", unsafe_allow_html=True)
    st.title("📝 Identitas Siswa")

    st.session_state.nama = st.text_input("Nama Lengkap")
    st.session_state.kelas = st.text_input("Kelas")

    if st.button("Mulai Quiz ▶", on_click=start_quiz):
        pass

    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ======== SLIDE HASIL ==========
if st.session_state.slide == len(questions):
    st.markdown("<div class='quiz-box'>", unsafe_allow_html=True)
    st.title("🎉 Quiz Completed!")
    st.subheader("Hasil Quiz")

    score = 0
    for i, q in enumerate(questions):
        if st.session_state.answers[i] == q["answer"]:
            score += 100 // len(questions)

    st.write(f"### Nama: **{st.session_state.nama}**")
    st.write(f"### Kelas: **{st.session_state.kelas}**")
    st.write(f"### ⭐ Skor kamu: **{score} / 100**")

    st.write("---")
    st.subheader("Kunci Jawaban")
    for i, q in enumerate(questions):
        st.write(f"**Soal {i+1}:** Kunci = {q['answer']} | Jawabanmu = {st.session_state.answers[i]}")

    st.button("🔄 Mulai Lagi", on_click=restart_quiz)
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ======== TAMPILAN SLIDE SOAL ==========
q = questions[st.session_state.slide]

st.markdown("<div class='quiz-box'>", unsafe_allow_html=True)
st.title("📚 Report Text Quiz")
st.write(f"### Slide {st.session_state.slide + 1} dari {len(questions)}")
st.write(f"**{q['question']}**")

selected_option = st.radio(
    "Pilih jawaban:",
    options=["A", "B", "C", "D"],
    index=["A", "B", "C", "D"].index(st.session_state.answers[st.session_state.slide]) 
          if st.session_state.answers[st.session_state.slide] else 0,
    key=f"radio_{st.session_state.slide}"
)

st.session_state.answers[st.session_state.slide] = selected_option

col1, col2 = st.columns(2)

with col1:
    if st.session_state.slide > 0:
        st.button("⬅ Sebelumnya", on_click=previous_slide)

with col2:
    if st.session_state.slide < len(questions) - 1:
        st.button("Lanjut ➡", on_click=next_slide)
    else:
        st.button("Selesai 🎉", on_click=lambda: st.session_state.update({"slide": len(questions)}))

st.markdown("</div>", unsafe_allow_html=True)
