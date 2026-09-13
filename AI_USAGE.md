# Rekod Penggunaan AI Code Assistant

## 1. Nama AI Code Assistant

ChatGPT.

## 2. Prompt yang Digunakan

Antara mesej yang saya gunakan ialah:
“saya nak langkah ii boleh bukan suruh yang siap”

Saya membekalkan soalan, tutorial, rubrik dan fail CSV.
Kemudian saya meminta panduan secara berperingkat serta
menghantar tangkapan skrin untuk semakan setiap langkah.

## 3. Cadangan yang Diberikan oleh AI

ChatGPT memberikan contoh kod dan penerangan untuk:
- Membaca CSV menggunakan pandas.
- Menapis data berdasarkan nilai confidence.
- Mengira statistik.
- Menghasilkan carta bar menggunakan Matplotlib.
- Mengesahkan input pengguna.
- Menyusun kod kepada fungsi dalam dua fail berasingan.

## 4. Bahagian Kod yang Dibantu

Dalam analysis.py:
- load_data()
- filter_data()
- calculate_statistics()
- create_bar_chart()

Dalam main.py:
- get_threshold()
- display_results()
- main()

ChatGPT turut membantu menyediakan draf dokumentasi dan
panduan arahan Git.

## 5. Perubahan yang Saya Lakukan

Saya memasukkan kod secara berperingkat ke dalam fail projek
dan menjalankan ujian selepas setiap bahagian.

Setakat ini, saya mengikuti cadangan kod ChatGPT.
Saya belum membuat perubahan logik secara bebas daripada
cadangan tersebut.

## 6. Cara Saya Menguji Kod

Saya menjalankan ujian berikut dalam Command Prompt:

1. Memanggil load_data() dan memaparkan lima rekod pertama.
   Keputusan: Data berjaya dibaca.

2. Menapis data menggunakan nilai ambang 0.70.
   Keputusan: Tujuh rekod diterima, iaitu image_id
   1, 2, 3, 5, 6, 7 dan 9.

3. Mengira statistik selepas tapisan.
   Keputusan: Purata confidence ialah 0.85 dan purata
   masa inferens ialah 44.86 ms.

4. Menghasilkan dan membuka carta bar.
   Keputusan: person = 3, car = 3 dan cat = 1.

5. Menguji input abc.
   Keputusan: Program memaparkan mesej nombor tidak sah
   dan meminta input semula.

6. Menguji input 1.5.
   Keputusan: Program memaparkan mesej nilai mesti
   antara 0 hingga 1 dan meminta input semula.

7. Menguji input 1 dan 0.70.
   Keputusan: Kedua-dua nilai diterima sebagai input sah.

8. Menjalankan python main.py dengan nilai 0.70.
   Keputusan: Program berjaya dilaksanakan serta menyimpan
   filtered_data.csv dan object_count.png dalam folder output.

## 7. Satu Manfaat AI Code Assistant

AI membantu saya membina program secara berperingkat
dengan contoh kod dan penerangan fungsi.

## 8. Satu Batasan AI Code Assistant

Cadangan AI boleh mengandungi kesalahan. Saya perlu
menyemak dan menguji kod sebelum menggunakannya.