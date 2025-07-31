## 📊 Aplikasi Prediksi Churn Karyawan (TalentaHub)
Aplikasi ini adalah sebuah dashboard web interaktif yang dibangun untuk memprediksi probabilitas seorang karyawan akan berhenti dari perusahaan (churn). Dengan memasukkan beberapa atribut terkait karyawan, model machine learning akan memberikan prediksi probabilitas churn, mengklasifikasikannya ke dalam kelompok risiko (Rendah, Sedang, Tinggi), dan memberikan saran tindakan yang bisa diambil.

Aplikasi ini terdiri dari dua komponen utama:

1. **Backend (FastAPI):** Menyediakan API untuk menerima data karyawan dan menjalankan model prediksi.
2. **Frontend (Streamlit):** Antarmuka web yang ramah pengguna untuk memasukkan data dan menampilkan hasil prediksi secara visual.

## ✨ Fitur
1. **Prediksi Real-time:** Masukkan data karyawan dan dapatkan probabilitas churn secara instan.
2. **Analisis Risiko:** Hasil prediksi dikategorikan ke dalam kelompok risiko Rendah, Sedang, atau Tinggi untuk mempermudah pengambilan keputusan.
3. **Saran Tindakan:** Setiap prediksi disertai dengan rekomendasi tindakan yang relevan untuk membantu retensi karyawan.
4. **Riwayat Prediksi:** Lihat kembali semua prediksi yang telah Anda buat selama sesi penggunaan aplikasi.
5. **Antarmuka Interaktif:** Slider dan input numerik yang mudah digunakan untuk memasukkan data.

## ⚙️ Menjalankan Aplikasi
Aplikasi ini memerlukan dua terminal yang berjalan secara bersamaan: satu untuk backend dan satu untuk frontend.
1. **Terminal 1: Jalankan Backend**
   ```
    uvicorn backend:app --reload
   ```
2. **Terminal 2: Jalankan Frontend (Streamlit)**
   ```
   streamlit run frontend.py
   ```
   
