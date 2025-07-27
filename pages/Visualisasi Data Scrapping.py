import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


# Membaca dataset
file_path = "mytelkomseltfidf_scrapping.csv"
data = pd.read_csv(file_path, encoding='ISO-8859-1')


# Judul aplikasi
st.title("Visualisasi Analisis Sentimen")
st.markdown('''Halo semuanya,
            \n Halaman ini berisi hasil visualisasi data dari penelitian mengenai analisis perbandingan sentimen ulasan pengguna aplikasi mytelkomsel. ''')
st.markdown('<div style="text-align: justify;"> Penelitian ini bertujuan untuk menganalisis perbandingan sentimen ulasan pengguna aplikasi mytelkomsel. Data sentimen didapat dari komentar google play store  dengan kriteria sebagai berikut\
            <br>1. Data berbahasa Indonesia\
            <br>2. Data diambil berjumlah 1400 dan menggunakan kata kunci "Mytelkomsel","Aplikasi MyTelkomsel"\
            <br>3. Data merupakan postingan, repost, maupun komentar pengguna google play store dari bulan Januari 2025 hingga Maret 2025\
            </div>', unsafe_allow_html=True)

# Menampilkan dataset
st.subheader("Dataset")
st.write("Berikut adalah beberapa baris dari dataset yang digunakan:")
#st.dataframe(data.head())
st.dataframe(data[['content']].head(5)) 

# Pilihan jenis visualisasi
st.subheader("Visualisasi Data")
options = ["Distribusi Sentimen (Pie Chart)", "Frekuensi Sentimen (Bar Chart)", "Wordcloud"]
choice = st.selectbox("Pilih visualisasi:", options)

# Visualisasi Distribusi Sentimen (Pie Chart)
if choice == "Distribusi Sentimen (Pie Chart)":
    st.subheader("Distribusi Sentimen")
    sentimen_counts = data['sentiment'].value_counts()
    
    fig, ax = plt.subplots()
    ax.pie(sentimen_counts, labels=sentimen_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    ax.set_title("Distribusi Sentimen")
    st.pyplot(fig)

# Visualisasi Frekuensi Sentimen (Bar Chart)
elif choice == "Frekuensi Sentimen (Bar Chart)":
    st.subheader("Frekuensi Sentimen")
    sentimen_counts = data['sentiment'].value_counts()
    
    fig, ax = plt.subplots()
    sns.barplot(x=sentimen_counts.index, y=sentimen_counts.values, palette="viridis", ax=ax)
    ax.set_xlabel("Sentimen")
    ax.set_ylabel("Frekuensi")
    ax.set_title("Frekuensi Sentimen")
    st.pyplot(fig)

# Visualisasi Wordcloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

if choice == "Wordcloud":
    st.subheader("Wordcloud")
    combined_text = " ".join(data['clean_text'].dropna())
    wordcloud = generate_wordcloud(combined_text)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)

    ##KESIMPULAN##

def main():
    st.subheader("Kesimpulan")
    st.write("Berikut kesimpulan hasil dari penelitian ini")

    # Membuat container
    with st.container():
    
        # Membagi container menjadi 3 kolom
        col1, col2, col3 = st.columns(3, border=True)

        with col1:
            st.write("#### 1.")
            st.markdown('<div style="text-align: justify;"> Hasil analisis menunjukkan bahwa sentimen netral lebih mendominasi sebesar 569\
                        disusul dengan sentimen negatif sebesar 517 dan sentimen positif sebesar 314.\
                         sehingga terbukti efektif untuk mengevaluasi persepsi pengguna dan meningkatkan layanan aplikasi.\
                         </div>', unsafe_allow_html=True) 
           
        with col2:
            st.write("#### 2.")
            st.markdown('<div style="text-align: justify;"> Terdapat perbedaan ulasan sentimen antara ulasan platform twitter ' \
            'dan ulasan google play store yang dimana ulasan twitter cenderung ingin berbagi pengalaman buruk atau mencari' \
            ' dukungan dari pengguna lain. sedangkan ulasan google play store cenderung mengungkapkan keluhan yang dimana lebih berharap mendapatkan solusi langsung dari pihak pengembang.</div>', unsafe_allow_html=True) 
           
        with col3:
            st.write("#### 3.")
            st.markdown('<div style="text-align: justify;"> Hasil akurasi Metode naive bayes yaitu 70% </div>', unsafe_allow_html=True) 
           
            
            

if __name__ == "__main__":
    main()

    