import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Fried Rice Report Text Quiz", layout="centered")

# --- CUSTOM CSS FOR COLORS & SLIDE FEEL ---
st.markdown(
    """
    <style>
    body {
        background-color: #FFF8E7;
    }
    .main {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(0,0,0,0.2);
    }
    .title {
        color: #D35400;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: #A04000;
        font-size: 20px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# --- QUESTIONS ---
questions = [
    {
        "text": "1. What is the main idea of the second paragraph?",
        "options": [
            "A. Fried Rice is a truly delicious meal",
            "B. Fried Rice is a truly complete meal",
            "C. Fried Rice is a truly Nusantara food",
            "D. Fried Rice is the best choice",
        ],
        "answer": 1,
    },
    {
        "text": "2. The word 'advantages' (paragraph 3) has the closest meaning to...",
        "options": ["A. profits", "B. difficulties", "C. stories", "D. ingredients"],
        "answer": 0,
    },
    {
        "text": "3. What is Fried Rice commonly served with?",
        "options": ["A. ice cream", "B. vegetables", "C. cereal", "D. bread"],
        "answer": 1,
    },
    {
        "text": "4. What is the purpose of the text?",
        "options": [
            "A. to describe about fried rice",
            "B. to describe about my breakfast menu",
            "C. to describe my favourite menu",
            "D. to describe about food",
        ],
        "answer": 0,
    },
    {
        "text": "5. What topping can be added on fried rice?",
        "options": [
            "A. fries",
            "B. coco chip",
            "C. butter",
            "D. vegetables, scrambled eggs, shredded chicken",
        ],
        "answer": 3,
    },
]

# --- TEXT STORY PAGE (PAGE 0) ---
if st.session_state.page == 0:
    st.markdown('<div class="title">THE WONDERFUL OF BREAKFAST "FRIED RICE"</div>', unsafe_allow_html=True)
    st.write("### Student Identity")
    name = st.text_input("Name:")
    class_name = st.text_input("Class:")

    st.write(
        """
        **Fried Rice, or Nasi Goreng**, is an unmatched and deeply beloved breakfast dish in Indonesia, 
        promising a satisfying start to the day. When served, it appears like a culinary artwork itself—a beautiful mosaic of vibrant colors. 
        The base of the rice, perfectly stir-fried, gleams with an appetizing golden-brown hue.
        
        Despite its simple appearance, a nutritionally balanced plate of Fried Rice is a truly complete meal. 
        The rice provides abundant carbohydrates, protein from scrambled eggs or chicken, and vitamins from vegetables.
        
        Choosing Fried Rice for breakfast offers strategic advantages, especially for students and employees who need stable energy and focus.
        """
    )

    if st.button("Start Quiz"):
        if name and class_name:
            st.session_state.name = name
            st.session_state.class_name = class_name
            st.session_state.page = 1
        else:
            st.warning("Please fill in your name and class first!")

# --- QUESTION PAGES ---
elif 1 <= st.session_state.page <= len(questions):
    q_index = st.session_state.page - 1
    q = questions[q_index]

    st.markdown(f"### {q['text']}")
    choice = st.radio("Choose your answer:", q["options"], key=f"q{q_index}")

    if st.button("Next"):
        selected = q["options"].index(choice)
        if selected == q["answer"]:
            st.session_state.score += 20
            st.markdown("<div style='padding:12px; background:#D4EFDF; border-left:8px solid #2ECC71; animation: pop 0.6s;'>✅ <b>Correct!</b></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='padding:12px; background:#FADBD8; border-left:8px solid #E74C3C; animation: pop 0.6s;'>❌ <b>Wrong!</b></div>", unsafe_allow_html=True)

        st.markdown("""
        <style>
        @keyframes pop {
            0% {transform: scale(0.5); opacity: 0;}
            80% {transform: scale(1.05); opacity: 1;}
            100% {transform: scale(1);}
        }
        </style>
        """, unsafe_allow_html=True)

        st.session_state.page += 1

# --- RESULTS PAGE ---
elif st.session_state.page == len(questions) + 1:
    st.markdown('<div class="title">RESULT</div>', unsafe_allow_html=True)
    st.write(f"### Name: **{st.session_state.name}**")
    st.write(f"### Class: **{st.session_state.class_name}**")
    st.write(f"## Your Score: **{st.session_state.score} / 100** 🎉")

    # --- SAVE SCORE TO FILE ---
    import csv
    with open('scores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([st.session_state.name, st.session_state.class_name, st.session_state.score])
    st.success("Your score has been saved to file ✔")

    if st.button("Restart"):
        st.session_state.page = 0
        st.session_state.score = 0
