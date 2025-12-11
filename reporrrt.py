import streamlit as st
from PIL import Image

st.set_page_config(page_title="Fried Rice Report Text Quiz", layout="wide")

# ========== CUSTOM PAGE STYLE ==========
page_bg = """
<style>
body {
    background-image: url("https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg");
    background-size: cover;
}
.block-container {
    background: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 15px;
}
h1, h2, h3, h4 {
    color: #b80000 !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


# ========== IDENTITAS ==========
st.title("📘 *Report Text Quiz – The Wonderful of Breakfast ‘Fried Rice’*")

name = st.text_input("Masukkan Nama:")
kelas = st.text_input("Masukkan Kelas:")

if not name or not kelas:
    st.warning("Silakan isi identitas dulu sebelum mulai.")
    st.stop()


# ========== TEKS SOAL DI AWAL ==========
with st.expander("📖 Klik untuk membuka teks bacaan"):
    st.write("""
### **The Wonderful of Breakfast “Fried Rice”**

Fried Rice, or Nasi Goreng, is an unmatched and deeply beloved breakfast dish in Indonesia, promising a satisfying start to the day. When served, it appears like a culinary artwork itself—a beautiful mosaic of vibrant colors. The base of the rice, perfectly stir-fried, gleams with an appetizing golden-brown hue, harmonizing with the pieces of bright green scallions, orange carrot slices, and the red spice from chilies. Every spoonful offers a satisfying mix of textures, from the soft rice to the crunchiness of the vegetables. The dominant aroma is a warm, savory blend of garlic, shallots, and the characteristic smoky scent, giving a visual that this is a flavorful dish that will fuel your energy.

Despite its simple appearance, a nutritionally balanced plate of Fried Rice is a truly complete meal. The rice provides abundant carbohydrates, which is the primary fuel converted into glucose for brain and muscle energy. Protein intake is served through slices of scrambled eggs, shredded chicken, or seafood, which are vital for cell repair and long-lasting satiety. Furthermore, added vegetables such as mustard greens, cucumber, or tomato are not merely garnish, but essential sources of vitamins, minerals, and dietary fiber that support digestive health. These components work together to ensure that Fried Rice not only fills the stomach but also provides the necessary macro and micronutrients for morning activity.

Choosing Fried Rice for breakfast offers strategic advantages, especially for students and employees who have high performance demands. For students, the complex carbohydrate content provides stable energy, preventing drowsiness in class and enhancing concentration during critical lessons. The savory taste and warm spices also serve to awaken mental alertness, helping them transition smoothly into their studies. Meanwhile, for employees, the combination of carbohydrates and protein in Fried Rice ensures sustained satiety, reducing distractions caused by hunger during meetings or busy work hours. With stable energy and adequate nutrition, Fried Rice helps maintain high levels of productivity and vigor until lunchtime arrives.
""")


# ========== DATA SOAL ==========
questions = [
    {
        "q": "1. What is the main idea of the second paragraph?",
        "opts": {
            "A": "Fried Rice is a truly delicious",
            "B": "Fried Rice is a truly complete meal",
            "C": "Fried Rice is a truly nusantara food",
            "D": "Fried Rice is a truly best choice"
        },
        "answer": "B"
    },
    {
        "q": "2. The word 'advantages' in paragraph 3 has closest meaning...",
        "opts": {
            "A": "impact",
            "B": "purpose",
            "C": "beneficial",
            "D": "loss"
        },
        "answer": "C"
    },
    {
        "q": "3. What topping can be added on fried rice?",
        "opts": {
            "A": "fries",
            "B": "coco chip",
            "C": "butter",
            "D": "vegetables, scrambled eggs, shredded chicken"
        },
        "answer": "D"
    },
    {
        "q": "4. What is the purpose of the text?",
        "opts": {
            "A": "to describe about fried rice",
            "B": "to describe about my breakfast menu",
            "C": "to describe my favourite menu",
            "D": "to describe about food"
        },
        "answer": "A"
    },
    {
        "q": "5. What topping can be added on fried rice?",
        "opts": {
            "A": "fries",
            "B": "coco chip",
            "C": "butter",
            "D": "vegetables, scrambled eggs, shredded chicken"
        },
        "answer": "D"
    }
]


# ========== SESSION STATE ==========
if "num" not in st.session_state:
    st.session_state.num = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False


# ========== MENAMPILKAN SOAL BERDASARKAN SLIDE ==========
i = st.session_state.num
q = questions[i]

st.subheader(q["q"])

choice = st.radio("Pilih jawabanmu:", list(q["opts"].keys()),
                  format_func=lambda x: f"{x}. {q['opts'][x]}")


# ========== CEK JAWABAN ==========
if st.button("Cek Jawaban"):
    if not st.session_state.answered:
        if choice == q["answer"]:
            st.success("✔ Jawaban benar!")
            st.session_state.score += 20
        else:
            st.error("✘ Jawaban salah!")
        st.session_state.answered = True


# ========== NEXT ==========
if st.session_state.answered:
    if st.button("Next"):
        st.session_state.num += 1
        st.session_state.answered = False


# ========== SELESAI ==========
if st.session_state.num >= len(questions):
    st.balloons()
    st.title("🎉 Quiz Completed!")
    st.subheader(f"👤 Nama: **{name}**")
    st.subheader(f"🏫 Kelas: **{kelas}**")
    st.header(f"🏆 Score Akhir: **{st.session_state.score} / 100**")
    st.stop()
