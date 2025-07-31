# Probabilistic Turnover Risk Scoring with Tiered Classification

![Project Status](https://img.shields.io/badge/status-OnProgress-red)
![Language](https://img.shields.io/badge/language-Python-blue)
![Tool](https://img.shields.io/badge/tool-Google_Colab-orange)

---

## 🚀 Project Overview

Proyek ini bertujuan untuk mengatasi tingginya tingkat *turnover* karyawan di TalentaHub (62.9%) dengan mengembangkan sebuah model *machine learning*. Model ini secara proaktif mengidentifikasi karyawan yang berisiko tinggi untuk keluar dari perusahaan dengan memberikan skor risiko probabilistik. Berdasarkan skor ini, karyawan diklasifikasikan ke dalam tiga tingkatan risiko (Tinggi, Sedang, Rendah) untuk memungkinkan tim HR menerapkan strategi retensi yang lebih terfokus dan efisien dari segi biaya.

**Links:**
* **[Notebook Google Colab](https://github.com/Naufaliffa/final-project/tree/main/notebooks)**
* **[Live Demo (Streamlit)](streamlit.io)**
* **[Presentasi Proyek]()**

## Daftar Isi
1.  [Business Problem & Objective](#1--business-problem--objective)
2.  [Business Value & Impact](#2--business-value--impact)
3.  [Metodologi: CRISP-DM](#3-metodologi-crisp-dm)
4.  [Hasil Analisis & Temuan Utama](#4-hasil-analisis--temuan-utama)
5.  [Detail Teknis](#5-detail-teknis)
6.  [Tantangan yang Dihadapi](#6-tantangan-yang-dihadapi)
7.  [Struktur Proyek](#7-struktur-proyek)

---

## 1. 🎯 Business Problem & Objective

TalentaHub, sebuah perusahaan di bidang rekrutmen dan manajemen talenta sales, menghadapi tantangan serius dengan **tingkat turnover karyawan yang mencapai 62.9%** pada akhir tahun lalu. Tingginya angka ini berdampak langsung pada:
* **Peningkatan Biaya**: Biaya rekrutmen dan pelatihan karyawan baru yang signifikan.
* **Penurunan Produktivitas**: Hilangnya pengetahuan institusional dan terganggunya kontinuitas kerja tim.
* **Kehilangan Peluang**: Waktu yang seharusnya digunakan untuk pengembangan bisnis terpakai untuk proses rekrutmen.

Meskipun telah ada program kompensasi dan *engagement*, TalentaHub belum memiliki sistem untuk **mengidentifikasi karyawan berisiko secara proaktif**. Pendekatan yang ada saat ini bersifat reaktif, bukan preventif.

## 2. 💼 Business Value & Impact
Analisis tingkat risiko karyawan resign berdasarkan pendekatan **Risk-Based Prioritization** untuk mengalokasikan sumber daya dan perhatian pada area yang memiliki risiko tertinggi terlebih dahulu.

### Risk Categories

| Risk Level | Kemungkinan Resign | Estimasi Biaya/Orang | Komponen Biaya Dampak | Penjelasan |
|------------|-------------------|---------------------|----------------------|------------|
| 🔴 **High** | >90% | 60% | • Biaya rekrutmen baru<br>• Biaya pelatihan onboarding<br>• Hilangnya produktivitas<br>• Kehilangan pengetahuan organisasi (IP loss)<br>• Disengagement tim | Berdasarkan pendekatan Risk-Based Prioritization bahwa mengalokasikan sumber daya dan perhatian pada area yang memiliki risiko tertinggi terlebih dahulu |
| 🟠 **Medium** | 38–90% | 30% | • Biaya rekrutmen (kemungkinan resign sedang)<br>• Pelatihan ulang sebagian<br>• Supervisi tambahan | Belum tentu resign, tapi potensi kerugian tetap ada jika tidak dimitigasi |
| 🟢 **Low** | <38% | 10% | • Biaya monitoring & engagement<br>• Survey kepuasan, wellness, dsb. | Biaya retensi pasif, seperti wellbeing support, check-in, dan engagement plan |

### Business Impact

### Model Performance
| Metric | Value |
|--------|-------|
| **Total Karyawan Berisiko** | 629 karyawan |
| **Recall Rate** | 90% |
| **Hasil Identifikasi** | 567 karyawan |

### Turnover Reduction Results
| Periode | Jumlah Turnover | Persentase |
|---------|----------------|------------|
| **Sebelum** | 629 | 62.9% |
| **Sesudah** | 63 | 0.63% |

**Model ini berhasil menurunkan risiko turnover dari 62.9% menjadi 0.63%**

### Key Insights

1. **Prioritas Utama:** Fokus pada karyawan dengan risk level tinggi (>90% kemungkinan resign)
2. **Cost Impact:** Biaya tertinggi terjadi pada kategori high risk dengan estimasi 60% dari gaji tahunan per orang
3. **Prevention Strategy:** Investasi pada monitoring dan engagement untuk kategori low risk lebih cost-effective
4. **Resource Allocation:** Alokasi sumber daya sebaiknya mengikuti tingkat risiko untuk efisiensi maksimal

### Implementation Strategy

- **High Risk:** Immediate intervention dan retention program intensif
- **Medium Risk:** Monitoring ketat dengan action plan siaga
- **Low Risk:** Maintenance program dan preventive measures

---

*Risk-Based Prioritization Framework untuk Employee Retention Management*

#### 📈 **Pengambilan Keputusan Berbasis Data**
Dengan pendekatan ini, perusahaan dapat **mengoptimalkan pengeluaran** dan secara signifikan **menurunkan tingkat *turnover*** dengan menargetkan intervensi pada segmen yang paling krusial. Serta menyediakan *insight* objektif bagi manajemen dan HR untuk diskusi retensi, menggantikan intuisi dengan bukti data.

---

## 3. Metodologi: CRISP-DM

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

## 4. Hasil Analisis & Temuan Utama

#### Temuan Kunci 1: Tingkat Pendidikan Berpengaruh
Analisis menunjukkan bahwa karyawan dengan jenjang pendidikan **Diploma** memiliki kecenderungan *turnover* yang lebih tinggi dibandingkan dengan jenjang pendidikan lainnya. Ini bisa menjadi indikasi adanya ketidaksesuaian antara ekspektasi karir dengan peluang yang ada.

#### Temuan Kunci 2: Faktor Pendorong Utama Turnover
Tiga faktor yang paling signifikan mempengaruhi keputusan seorang karyawan untuk *turnover* adalah:
1.  **`target_achievement`**: Pencapaian target yang rendah secara konsisten.
2.  **`job_satisfaction`**: Tingkat kepuasan kerja yang rendah.
3.  **`manager_support_score`**: Kurangnya dukungan dari manajer.

*Placeholder untuk visualisasi seperti Feature Importance Chart:*

---

## 5. Detail Teknis

* **Tools**: Google Colaboratory, Jupyter Notebook
* **Libraries**:
    * **Analisis Data**: Pandas, NumPy
    * **Visualisasi**: Matplotlib, Seaborn
    * **Machine Learning**: Scikit-learn
* **Dataset**: `employee_churn_prediction_updated.csv`
* **Model**: Model klasifikasi yang menghasilkan probabilitas, menggunakan *Random Forest*, untuk interpretasi yang mudah bagi pemangku kepentingan bisnis.

---

## 6. Tantangan yang Dihadapi

* **Data**: Kualitas data yang tidak sempurna memerlukan pembersihan ekstensif. Tanpa konteks bisnis yang kuat, data bisa disalahartikan.
* **Model**: Terdapat risiko *overfitting* atau *underfitting* serta potensi bias dalam model yang dapat menghasilkan evaluasi yang tidak sesuai dengan kenyataan.
* **Adopsi Pengguna**: Potensi penolakan dari *stakeholder* atau pengguna akhir jika hasil model tidak dikomunikasikan dengan baik, yang dapat menghambat implementasi proyek.

---

## 7. Struktur Proyek

```
.
├── data/
│   └── raw_data.csv
├── deploy/
│   └── README.md
│   └── backend.py
│   └── frontend.py
│   └── requirements.txt
├── image/
│   └── gambar.img
├── notebooks/
│   └── turnover_analysis.ipynb
├── presentation/
│   └── project_slides.pdf
├── README.md
└── .gitignore
```

-----


