import streamlit as st
#from PIL import Image
import base64

st.set_page_config(
   page_title="Analisis Sentimen")

##menampilkan logo sidebar

def image_to_base64(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")
    
# Path logo
logo1_path = "logo.png"  
logo2_path = "kampus.png" 

logo1_base64 = image_to_base64(logo1_path)
logo2_base64 = image_to_base64(logo2_path)

# HTML 
logos_html = f"""
<div style="display: flex; justify-content: left; align-items: center;">
    <img src="data:image/png;base64,{logo1_base64}" style="width:50px; margin-right:10px;" />
    <img src="data:image/png;base64,{logo2_base64}" style="width:50px;" />
</div>
"""
# Menampilkan di sidebar
st.sidebar.markdown(logos_html, unsafe_allow_html=True)

st.sidebar.title("About")
st.sidebar.caption("Haii, Perkenalkan nama saya Muhammad Hadi dari Program Studi Sistem Informasi Universitas Hang Tuah Pekanbaru.")
st.sidebar.caption("Aplikasi ini dibuat untuk tahap akhir dari skripsi saya yang berjudul Analisis Perbandingan Sentimen Ulasan Pengguna Aplikasi MyTelkomsel dengan Algoritma Naive Bayes di Platform Twitter dan Google Play Store \
                   ")

st.title("Analisis Sentimen MyTelkomsel")
st.image("mytelkomsel.jpg", width=300)
st.markdown('<div style="text-align: justify;">Selamat datang di aplikasi web interaktif Analisis Perbandingan Sentimen Ulasan Pengguna Aplikasi MyTelkomsel.\
             Aplikasi ini dibuat untuk memberikan wawasan mendalam mengenai persepsi pengguna terhadap aplikasi MyTelkomsel \
            yang diambil dari dua platform populer: Google Play Store dan Media Sosial Twitter (X). </div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Tujuan Aplikasi ini", "Metode yang digunakan"])
       
with tab1:
    
        lst = ['Menganalisis sentimen ulasan pengguna (positif, negatif, netral)', 'Membandingkan persepsi pengguna dari dua platform berbeda', ' Memberikan visualisasi yang mudah dipahami mengenai kinerja sentimen aplikasi']

        s = ''
        for i in lst:
            s += "- " + i + "\n"

        st.markdown(s)
#tab2.write("this is tab 2")

with tab2:
    lst = ['Preprocessing teks (cleansing, normalisasi, tokenisasi, dll)', 'Pemberian label sentimen menggunakan pendekatan lexicon', 'Pembobotan kata dengan TF-IDF',
           'Klasifikasi sentimen menggunakan algoritma Naïve Bayes']

    s = ''
    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('<div style="text-align: justify;">Aplikasi ini dibangun menggunakan Python dan framework Streamlit, \
            serta dilengkapi dengan berbagai visualisasi interaktif untuk membantu Anda memahami hasil analisis secara menyeluruh. </div>', unsafe_allow_html=True)


