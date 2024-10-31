# Tugas Besar Komputasi Cerdas
[(https://github.com/tasya1509/RBLKomcer)](https://rblkomcer-immxsacfjbrb62h46dgrpm.streamlit.app/)

# Introduction to Computer Vision and the YOLO Model
Computer vision, a branch of artificial intelligence, empowers machines to interpret and analyze visual data, enabling applications like facial recognition and autonomous driving. A significant advancement in this field is the YOLO (You Only Look Once) model, which transformed object detection by simultaneously predicting classifications and bounding boxes in a single neural network pass, enhancing speed and real-time detection capabilities. The latest iteration, YOLOv8 from Ultralytics, leverages advanced machine learning techniques to further improve accuracy and efficiency, while its open-source nature promotes widespread adoption and ongoing development. As a result, YOLO has become a fundamental tool in computer vision, facilitating effective object detection, instance segmentation, and classification across various projects.

# Parking Car Detection System
This project is a Parking Car Detection System that uses YOLO (You Only Look Once) model to detect cars in a parking lot image. It is designed to be deployed for monitoring the number of cars parked at the ITERA campus parking area. The system runs on Python and utilizes the YOLOv8 model for object detection.

# How it works
1. Image Input: The system accepts an image input (static image or live feed) that captures the parking area.
2. Object Detection: YOLOv8 model is used to detect cars in the image.
3. Bounding Box Visualization: Detected cars are highlighted with bounding boxes drawn on the image.
4. Car Count: The system returns the total number of cars detected.

# Features
1. Real-time object detection with YOLOv8.
2. Easy-to-use interface for uploading images.
3. Visualization of detected cars with bounding boxes.
4. Counts the total number of cars in the parking lot.

# Installation
1. Clone the repository
2. Install the required packages
3. Run the script

Berikut adalah kombinasi alur lengkap arsitektur YOLOv8n yang disesuaikan untuk mendeteksi dan menghitung jumlah mobil di parkiran sekitar ITERA:
1. Lapisan Input
Sistem menerima gambar atau frame video dari area parkiran sekitar ITERA sebagai input. Gambar ini bisa berasal dari kamera CCTV atau foto statis yang menangkap keseluruhan area parkiran. Input ini berfungsi sebagai data visual yang akan dianalisis untuk mendeteksi keberadaan mobil.
2. *Backbone* (Ekstraksi Fitur)
Conv (Konvolusi): Pada tahap awal, lapisan konvolusi digunakan untuk mengekstraksi fitur dasar dari gambar, yang merupakan karakteristik visual awal yang dapat digunakan untuk mendeteksi objek.
C2f (Cross Stage Partial Network): Blok konvolusi khusus ini berfungsi menangkap fitur yang lebih kompleks dan membantu mengenali pola-pola khas yang menggambarkan bentuk serta karakteristik mobil.
SPPF (Spatial Pyramid Pooling - Fast): Bagian ini menciptakan piramida fitur untuk berbagai ukuran objek dalam gambar, membantu deteksi mobil pada berbagai skala dan posisi di parkiran. SPPF sangat berguna untuk mendeteksi mobil dalam berbagai skala, baik yang berada dekat maupun jauh dari kamera.
3. *Neck* (Peningkatan Fitur dan Multi-Skala)
C2f (Blok Konvolusi): Lapisan ini membantu memproses fitur lebih lanjut agar lebih spesifik terhadap objek mobil.
Concat (Concatenate): Tahap ini menggabungkan peta fitur dari berbagai lapisan dan skala. Fitur-fitur dari skala yang berbeda di backbone disatukan untuk mendapatkan informasi detail dari objek kecil hingga besar, sehingga deteksi mobil dapat dilakukan dengan lebih presisi.
Upsample (Upsampling): Peta fitur yang dihasilkan dikembalikan ke resolusi lebih besar agar objek-objek kecil, seperti mobil yang berada jauh dari kamera, dapat terdeteksi dengan baik. Ini penting dalam konteks parkiran, terutama untuk mobil yang lebih kecil atau lebih jauh.
4. *Feature Pyramid Network (FPN)*
*Multi-Scale Representation*: FPN menggabungkan fitur dari berbagai lapisan backbone untuk meningkatkan akurasi deteksi, khususnya untuk objek dengan variasi ukuran seperti mobil.
*P3, P4, P5 Layers: FPN menghasilkan representasi fitur multi-skala yang ditandai sebagai **P3, **P4, dan **P5*, yang menggabungkan informasi dari berbagai skala backbone. Fitur multi-skala ini membantu sistem mendeteksi mobil pada berbagai posisi dan ukuran, sehingga mobil-mobil kecil maupun besar dapat dideteksi dengan akurasi yang tinggi.
5. *Detection Heads (Kepala Deteksi)*
*Detect (Deteksi Mobil)*: Pada setiap skala (P3, P4, P5), terdapat kepala deteksi yang memproses peta fitur untuk menghasilkan prediksi berupa kotak pembatas (bounding boxes), skor kepercayaan (confidence scores), dan probabilitas kelas.
*Loss Function: Fungsi loss, seperti **Cross Entropy Loss* untuk klasifikasi dan *L1 Loss* untuk posisi kotak, diterapkan pada setiap kepala deteksi untuk mengoptimalkan akurasi. Sistem ini dirancang untuk mengenali objek "mobil" dan mengabaikan objek lain seperti motor atau orang, sesuai kebutuhan deteksi parkiran mobil.
6. Filter Kelas Objek (Mobil)
Setelah deteksi dilakukan, sistem hanya memilih kotak pembatas yang memiliki label "mobil". Ini dilakukan dengan memfilter prediksi berdasarkan label kelas hasil deteksi YOLOv8n. Filter ini memastikan bahwa hanya objek berlabel "mobil" yang dihitung, sehingga data yang diterima akurat dan relevan dengan kebutuhan pengelolaan parkiran.
7. Perhitungan Jumlah Mobil
Sistem menghitung jumlah kotak pembatas yang lolos filter dengan label "mobil" untuk mendapatkan total jumlah mobil yang terdeteksi di parkiran. Informasi ini kemudian bisa digunakan untuk memantau kapasitas parkir secara real-time dan memperkirakan tingkat kepadatan parkiran.
8. *Output*
Gambar Hasil Deteksi: Sistem menampilkan gambar yang telah diproses dengan kotak pembatas pada setiap mobil yang terdeteksi. Setiap kotak pembatas diberi warna atau label yang menunjukkan deteksi mobil.
Jumlah Mobil Terdeteksi: Sistem mencetak jumlah total mobil yang terdeteksi di area parkiran. Informasi ini dapat digunakan untuk melihat ketersediaan tempat parkir dan memperkirakan tingkat kepadatan parkiran secara otomatis.

Dengan arsitektur ini, model YOLOv8n mampu melakukan deteksi dan perhitungan jumlah mobil secara efisien dan akurat, mendukung kebutuhan pengelolaan parkir di lingkungan sekitar ITERA.
