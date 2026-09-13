# Simple AI Inference Analyzer

Aplikasi Python mudah untuk membaca, menapis dan menganalisis
data inferens AI serta menghasilkan carta bar.

Projek ini disediakan bagi Practical Test 1 kursus
DKA3223 Artificial Intelligence for Computer Vision.

## Objektif

- Membaca fail CSV menggunakan pandas.
- Menapis rekod berdasarkan nilai ambang keyakinan.
- Mengira statistik data selepas tapisan.
- Menghasilkan carta bar menggunakan Matplotlib.
- Mengurus versi projek menggunakan Git dan GitHub.

## Keperluan

- Python 3.10 atau lebih baharu
- pandas
- numpy
- matplotlib

## Pemasangan

Jalankan arahan berikut dalam terminal folder projek:

    python -m venv .venv
    .venv\Scripts\activate
    python -m pip install -r requirements.txt

Arahan pengaktifan di atas digunakan dalam Windows Command Prompt.

## Cara Menjalankan

Jalankan:

    python main.py

Masukkan nilai ambang antara 0 hingga 1, contohnya 0.70.

## Fail Utama

- main.py: Mengawal perjalanan program dan input pengguna.
- analysis.py: Mengandungi fungsi bacaan, tapisan, statistik dan graf.
- data/inference_data.csv: Menyimpan data asal.
- requirements.txt: Menyenaraikan pustaka yang diperlukan.
- AI_USAGE.md: Merekodkan penggunaan bantuan AI.

## Output

- output/filtered_data.csv
- output/object_count.png

Statistik dan carta menggunakan data selepas tapisan,
kecuali jumlah keseluruhan rekod yang merujuk kepada data asal.

Jika tiada rekod diterima, CSV mengandungi pengepala sahaja
dan carta tidak dihasilkan.

## Keputusan Ujian pada Ambang 0.70

- Jumlah rekod asal: 10
- Jumlah rekod diterima: 7
- Purata confidence: 0.85
- Confidence tertinggi: 0.95
- Confidence terendah: 0.73
- Purata masa inferens: 44.86 ms
- Bilangan objek: person = 3, car = 3, cat = 1

## Pengendalian Input

Program menolak input bukan nombor dan nilai di luar julat
0 hingga 1. Pengguna diminta memasukkan nilai semula.

## Nota

Aplikasi ini menganalisis data CSV sebagai persediaan sebelum
pelaksanaan pada NVIDIA Jetson. Aplikasi ini tidak menjalankan
model pengesanan objek secara langsung.