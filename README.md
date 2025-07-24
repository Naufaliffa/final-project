# Probabilistic Turnover Risk Scoring with Tiered Classification

![Project Status](https://img.shields.io/badge/status-OnProgress-red)
![Language](https://img.shields.io/badge/language-Python-blue)
![Tool](https://img.shields.io/badge/tool-Google_Colab-orange)

---

## 🚀 Project Overview

Proyek ini bertujuan untuk mengatasi tingginya tingkat *turnover* karyawan di TalentaHub (32.9%) dengan mengembangkan sebuah model *machine learning*. Model ini secara proaktif mengidentifikasi karyawan yang berisiko tinggi untuk keluar dari perusahaan dengan memberikan skor risiko probabilistik. Berdasarkan skor ini, karyawan diklasifikasikan ke dalam tiga tingkatan risiko (Tinggi, Sedang, Rendah) untuk memungkinkan tim HR menerapkan strategi retensi yang lebih terfokus dan efisien dari segi biaya.

**Links:**
* **[Notebook Google Colab](https://github.com/Naufaliffa/final-project/tree/main/notebooks)**
* **[Live Demo (Streamlit)](streamlit.io)**
* **[Presentasi Proyek]()**

## Daftar Isi
1.  [Business Problem & Objective](#1-Business-Problem-&-Objective)
2.  [Business Value & Impact](#2-nilai-bisnis--dampak)
3.  [Metodologi: CRISP-DM](#3-metodologi-crisp-dm)
4.  [Hasil Analisis & Temuan Utama](#4-hasil-analisis--temuan-utama)
5.  [Detail Teknis](#5-detail-teknis)
6.  [Tantangan yang Dihadapi](#6-tantangan-yang-dihadapi)
7.  [Struktur Proyek](#7-struktur-proyek)

---

### 1. 🎯 Business Problem & Objective

TalentaHub, sebuah perusahaan di bidang rekrutmen dan manajemen talenta sales, menghadapi tantangan serius dengan **tingkat turnover karyawan yang mencapai 62.9%** pada akhir tahun lalu. Tingginya angka ini berdampak langsung pada:
* **Peningkatan Biaya**: Biaya rekrutmen dan pelatihan karyawan baru yang signifikan.
* **Penurunan Produktivitas**: Hilangnya pengetahuan institusional dan terganggunya kontinuitas kerja tim.
* **Kehilangan Peluang**: Waktu yang seharusnya digunakan untuk pengembangan bisnis terpakai untuk proses rekrutmen.

Meskipun telah ada program kompensasi dan *engagement*, TalentaHub belum memiliki sistem untuk **mengidentifikasi karyawan berisiko secara proaktif**. Pendekatan yang ada saat ini bersifat reaktif, bukan preventif.

### 2. 💼 Business Value & Impact

Solusi berbasis data ini memberikan skor risiko *turnover* untuk setiap karyawan, yang memungkinkan perusahaan untuk:

🎯 **Alokasi Sumber Daya yang Tepat Sasaran**
Dengan menerapkan **Prinsip Pareto**, di mana 20% karyawan yang *turnover* dapat menyebabkan 80% kerugian, kami mengusulkan alokasi anggaran retensi yang berjenjang sesuai tingkat risiko:
* **Risiko Tinggi**: Alokasi sumber daya **60%** (misalnya: sesi *coaching* intensif, penyesuaian kompensasi, program mentoring).
* **Risiko Sedang**: Alokasi sumber daya **25%** (misalnya: program pelatihan tambahan, *feedback* rutin).
* **Risiko Rendah**: Alokasi sumber daya **15%** (misalnya: program *engagement* umum).

📈 **Pengambilan Keputusan Berbasis Data**
Dengan pendekatan ini, perusahaan dapat **mengoptimalkan pengeluaran** dan secara signifikan **menurunkan tingkat *turnover*** dengan menargetkan intervensi pada segmen yang paling krusial. Serta menyediakan *insight* objektif bagi manajemen dan HR untuk diskusi retensi, menggantikan intuisi dengan bukti data.

---

### 3. Metodologi: CRISP-DM

Proyek ini mengikuti metodologi *Cross-Industry Standard Process for Data Mining* (CRISP-DM) untuk memastikan proses yang terstruktur dan berorientasi pada tujuan bisnis.

| Fase | Deskripsi |
| :--- | :--- |
| **1. Business Understanding** | Mendefinisikan masalah tingginya *turnover* dan menetapkan tujuan untuk membangun model prediksi risiko guna mengurangi *turnover* secara proaktif. |
| **2. Data Understanding** | Menganalisis dataset `employee_churn_prediction_updated.csv` yang berisi 990+ baris dan 19 kolom, termasuk data demografis, metrik kinerja (`target_achievement`, `monthly_target`), dan faktor kepuasan (`job_satisfaction`, `manager_support_score`). |
| **3. Data Preparation** | Melakukan pembersihan data, menangani nilai yang hilang, melakukan *feature engineering*, dan melakukan *encoding* pada variabel kategorikal (`gender`, `education`, `work_location`) serta penskalaan pada fitur numerik. |
| **4. Modeling** | Mengembangkan model klasifikasi (contoh: *Logistic Regression* atau *Random Forest*) untuk memprediksi probabilitas *turnover*. Model ini dilatih untuk menghasilkan skor risiko individual. |
| **5. Evaluation** | Mengevaluasi performa model menggunakan metrik seperti *Accuracy*, *Precision*, *Recall*, dan *F1-Score*. Ambang batas probabilitas ditetapkan untuk mengklasifikasikan karyawan ke dalam kategori risiko Tinggi, Sedang, dan Rendah. |
| **6. Deployment** | Hasil akhir disajikan dalam notebook Google Colab. Model dapat diintegrasikan untuk menghasilkan laporan berkala yang berisi daftar karyawan beserta skor risikonya untuk ditindaklanjuti oleh tim HR. |

---

### 4. Hasil Analisis & Temuan Utama

#### Temuan Kunci 1: Tingkat Pendidikan Berpengaruh
Analisis menunjukkan bahwa karyawan dengan jenjang pendidikan **Diploma** memiliki kecenderungan *turnover* yang lebih tinggi dibandingkan dengan jenjang pendidikan lainnya. Ini bisa menjadi indikasi adanya ketidaksesuaian antara ekspektasi karir dengan peluang yang ada.

#### Temuan Kunci 2: Faktor Pendorong Utama Turnover
Tiga faktor yang paling signifikan mempengaruhi keputusan seorang karyawan untuk *turnover* adalah:
1.  **`target_achievement`**: Pencapaian target yang rendah secara konsisten.
2.  **`job_satisfaction`**: Tingkat kepuasan kerja yang rendah.
3.  **`manager_support_score`**: Kurangnya dukungan dari manajer.

*Placeholder untuk visualisasi seperti Feature Importance Chart:*

---

### 5. Detail Teknis

* **Tools**: Google Colaboratory, Jupyter Notebook
* **Libraries**:
    * **Analisis Data**: Pandas, NumPy
    * **Visualisasi**: Matplotlib, Seaborn
    * **Machine Learning**: Scikit-learn
* **Dataset**: `employee_churn_prediction_updated.csv`
* **Model**: Model klasifikasi yang menghasilkan probabilitas, menggunakan *Random Forest*, untuk interpretasi yang mudah bagi pemangku kepentingan bisnis.

---

### 6. Tantangan yang Dihadapi

* **Data**: Kualitas data yang tidak sempurna memerlukan pembersihan ekstensif. Tanpa konteks bisnis yang kuat, data bisa disalahartikan.
* **Model**: Terdapat risiko *overfitting* atau *underfitting* serta potensi bias dalam model yang dapat menghasilkan evaluasi yang tidak sesuai dengan kenyataan.
* **Adopsi Pengguna**: Potensi penolakan dari *stakeholder* atau pengguna akhir jika hasil model tidak dikomunikasikan dengan baik, yang dapat menghambat implementasi proyek.

---

### 7. Struktur Proyek

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


