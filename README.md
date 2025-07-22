# Probabilistic Turnover Risk Scoring with Tiered Classification

## 🚀 Project Overview

Proyek ini bertujuan untuk mengatasi **tingkat *turnover* karyawan yang tinggi (62.9%)** di departemen penjualan dengan mengembangkan model *machine learning*. Model ini memberikan skor probabilitas risiko *turnover* untuk setiap karyawan, yang kemudian diklasifikasikan ke dalam tiga tingkatan (Tinggi, Sedang, Rendah) untuk memungkinkan intervensi yang tepat sasaran dan efisien.

  * **Live Demo:** **[Lihat Dashboard Interaktif di Looker](https://lookerstudio.google.com/u/0/)** 
  * **Notebook Analisis:** **[Buka di Google Colab](https://github.com/Naufaliffa/final-project/tree/main/notebooks)**
  * **Dataset:** **[Dataset yang digunakan](https://www.kaggle.com/).**
  * **Presentasi Proyek:** **[Lihat Slide Deck](https://github.com/Naufaliffa/final-project/tree/main/presentation)** 

-----

## 🎯 Business Problem & Objective

Tingkat *turnover* di departemen penjualan telah mencapai **62.9%**, jauh di atas angka ideal industri sebesar 30%. Hal ini menyebabkan kerugian signifikan bagi perusahaan dalam bentuk biaya rekrutmen, pelatihan, dan hilangnya produktivitas.

Tujuan utama proyek ini adalah:

1.  **Mengidentifikasi** faktor-faktor utama yang memengaruhi keputusan karyawan untuk berhenti.
2.  **Mengembangkan** model klasifikasi untuk memprediksi probabilitas *turnover* setiap karyawan.
3.  **Menciptakan** sistem segmentasi risiko (*High, Medium, Low*) untuk memprioritaskan upaya retensi.

-----

## 🌊 Metodologi CRISP-DM

Proyek ini mengikuti metodologi **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*) untuk memastikan proses yang terstruktur dan berorientasi pada hasil bisnis.

1.  **Business Understanding:** Memahami masalah tingginya *turnover* dan mendefinisikan tujuan proyek bersama para pemangku kepentingan.
2.  **Data Understanding:** Melakukan analisis data eksplorasi (EDA) pada dataset internal yang berisi 1000 baris untuk menemukan pola dan wawasan awal.
3.  **Data Preparation:** Membersihkan data, menangani nilai yang hilang, dan melakukan rekayasa fitur (*feature engineering*) untuk mempersiapkan data untuk pemodelan.
4.  **Modeling:** Melatih beberapa model klasifikasi dan memilih yang terbaik berdasarkan metrik performa yang relevan.
5.  **Evaluation:** Mengevaluasi performa model secara menyeluruh untuk memastikan tidak terjadi *overfitting* atau *bias*, serta mengukur potensi dampak bisnisnya.
6.  **Deployment:** Menyajikan hasil, model, dan *dashboard* kepada tim HR dan manajemen sebagai alat bantu pengambilan keputusan strategis.

-----

## 🛠️ Tech Stack & Tools

  * **Analisis & Pemodelan:** Python, Pandas, Scikit-Learn, Jupyter Notebook (via Google Colab)
  * **Visualisasi & Dashboard:** Looker (Looker Studio)
  * **Version Control:** Git & GitHub

-----

## 📊 Key Findings & Analysis

Analisis data mengungkapkan beberapa pendorong utama *turnover* di departemen penjualan:

  * **Key Finding 1:** * *
  * **Key Finding 2:** * *

Berdasarkan analisis ini, model *machine learning* dikembangkan untuk menghasilkan skor risiko *turnover* bagi setiap individu.

-----

## 💼 Business Impact & Recommendations

Model ini memungkinkan perusahaan untuk beralih dari strategi retensi yang reaktif menjadi **proaktif dan berbasis data**. Dengan mengadopsi **prinsip Pareto** (di mana 20% karyawan yang berisiko *turnover* dapat menyebabkan 80% kerugian), kami merekomendasikan alokasi anggaran retensi dan pelatihan yang terfokus sebagai berikut:

| Tingkat Risiko | Proporsi Karyawan | Alokasi Anggaran Pelatihan | Rekomendasi Tindakan |
| :------------- | :----------------- | :----------------------- | :-------------------- |
| **Tinggi** | \~20%               | **60%** | Sesi konseling 1-on-1, penyesuaian insentif, program mentoring. |
| **Sedang** | \~35%               | **25%** | Pelatihan pengembangan karir, survei keterlibatan, *workshop* tim. |
| **Rendah** | \~45%               | **15%** | Program apresiasi reguler, peluang pengembangan standar. |

Dengan pendekatan ini, perusahaan dapat **mengoptimalkan pengeluaran** dan secara signifikan **menurunkan tingkat *turnover*** dengan menargetkan intervensi pada segmen yang paling krusial.

-----

## 💡 Challenges & Learnings

  * **Tantangan Teknis:** Risiko **overfitting** dan **bias** dalam model menjadi perhatian utama. Ini diatasi melalui validasi silang (*cross-validation*), regularisasi, dan analisis fitur yang cermat untuk memastikan keadilan dan generalisasi model.
  * **Tantangan Stakeholder:** Versi awal model **ditolak oleh tim HR** karena dianggap kurang intuitif dan tidak sepenuhnya sesuai dengan alur kerja mereka.
      * **Pembelajaran:** Hal ini menjadi pelajaran berharga tentang pentingnya **melibatkan *user* (pengguna akhir) sejak awal** (*user-centric design*) dan melakukan iterasi berdasarkan umpan balik mereka. Proyek ini menekankan bahwa keberhasilan solusi teknis sangat bergantung pada adopsi dan kegunaannya bagi pengguna.

-----

## 📂 Project Directory Structure

```
.
├── notebooks/
│   └── turnover_analysis.ipynb
├── data/
│   └── raw_data.csv
├── presentation/
│   └── project_slides.pdf
├── model/
│   └── model.pkl
├── image/
│   └── gambar.img
├── README.md
└── .gitignore
```

-----
