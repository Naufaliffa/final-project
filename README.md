Probabilistic Turnover Risk Scoring with Tiered Classification
Ringkasan Proyek: Proyek ini bertujuan untuk mengatasi tingginya tingkat turnover karyawan di divisi sales (62.9%) dengan mengembangkan model machine learning. Model ini memberikan skor probabilitas turnover untuk setiap karyawan dan mengklasifikasikannya ke dalam tiga tingkatan risiko (High, Medium, Low) untuk memungkinkan intervensi yang tepat sasaran dan efisien dari segi biaya.

Tautan Penting:

Live Demo/Dashboard: [Link ke Looker Dashboard Anda]

Code Repository: [Link ke GitHub Repository Anda]

Slide Presentasi: [Link ke Google Slides Anda]

1. Business Problem
Tingkat turnover karyawan di divisi sales saat ini mencapai 62.9%, lebih dari dua kali lipat angka ideal industri yaitu 30%. Tingginya angka ini menyebabkan kerugian signifikan bagi perusahaan, mencakup biaya rekrutmen, pelatihan karyawan baru, dan hilangnya produktivitas. Mengidentifikasi karyawan yang berisiko turnover secara proaktif sangat krusial untuk menekan biaya dan menjaga stabilitas tim.

2. Solusi & Dampak Bisnis
Kami mengembangkan sebuah model klasifikasi probabilistik untuk memprediksi kemungkinan seorang karyawan akan turnover. Model ini tidak hanya memprediksi "ya" atau "tidak", tetapi memberikan skor risiko yang kemudian dikategorikan menjadi tiga tingkatan:

High Risk: Karyawan dengan kemungkinan turnover sangat tinggi.

Medium Risk: Karyawan yang menunjukkan tanda-tanda awal risiko turnover.

Low Risk: Karyawan yang cenderung bertahan.

Dampak Bisnis:
Pendekatan ini memungkinkan alokasi sumber daya yang lebih cerdas. Sesuai prinsip Pareto, di mana ~20% karyawan berisiko tinggi dapat menyebabkan ~80% kerugian, kami mengusulkan alokasi anggaran retensi dan pelatihan sebagai berikut:

High Risk: Alokasi 60% dari budget untuk intervensi intensif.

Medium Risk: Alokasi 25% untuk program pengembangan.

Low Risk: Alokasi 15% untuk program apresiasi umum.

Strategi ini memastikan intervensi yang paling mahal diberikan kepada mereka yang paling membutuhkannya, sehingga memaksimalkan ROI dari program retensi karyawan.

3. Tech Stack & Tools
Analisis & Pemodelan: Python, Pandas, Scikit-learn, Matplotlib

Lingkungan Kerja: Google Colab

Visualisasi & Dashboard: Looker

Version Control: Git & GitHub

4. Metodologi
Proses pengembangan model mengikuti alur kerja data science standar:

Data Preprocessing: Membersihkan dataset internal yang terdiri dari 1000 baris, menangani nilai yang hilang, dan melakukan encoding pada fitur kategorikal.

Feature Engineering: Membuat fitur-fitur baru yang relevan yang dapat meningkatkan performa model (contoh: rasio gaji terhadap rata-rata industri, masa kerja).

Pemodelan: Menggunakan model Logistic Regression untuk mendapatkan skor probabilitas yang mudah diinterpretasikan oleh pihak bisnis.

Klasifikasi Bertingkat: Menerapkan ambang batas (thresholds) pada skor probabilitas untuk mengelompokkan karyawan ke dalam kategori risiko High, Medium, dan Low.

Evaluasi: Mengevaluasi performa model menggunakan metrik seperti AUC-ROC dan Precision-Recall untuk memastikan keandalannya dalam mengidentifikasi kandidat turnover.

5. Temuan Utama
[Temuan Utama 1]: Masukkan temuan kunci pertama di sini. Contoh: "Karyawan dengan masa kerja kurang dari 1 tahun dan tingkat pencapaian target di bawah 70% memiliki korelasi tertinggi dengan risiko turnover."

[Temuan Utama 2]: Masukkan temuan kunci kedua di sini. Contoh: "Faktor seperti 'jarak ke kantor' dan 'jumlah proyek yang ditangani' juga terbukti menjadi prediktor yang signifikan."

6. Tantangan & Pembelajaran
Tantangan Teknis: Risiko overfitting dan bias dalam model menjadi perhatian utama. Hal ini dimitigasi dengan teknik regularisasi dan validasi silang (cross-validation).

Tantangan User: Versi awal model ditolak oleh tim HR karena dianggap kurang intuitif. Ini menjadi pembelajaran berharga untuk fokus pada kebutuhan pengguna. Proyek ini kemudian diiterasi untuk menyertakan dasbor yang lebih interaktif dan penjelasan yang lebih sederhana mengenai cara kerja model.

7. Cara Menjalankan Proyek
Clone repository ini:

git clone [URL-GITHUB-ANDA]

Buka notebook di Google Colab:
Navigasi ke file Turnover_Risk_Scoring.ipynb dan buka menggunakan Google Colab.

Jalankan semua sel:
Dataset employee_data.csv sudah disertakan di dalam repository untuk memastikan reproduktifitas.
