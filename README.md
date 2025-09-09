Nama : Aaron Nathanael Suhaendi

NPM : 2406437073

Kelas : PBP B

Tautan PWS: https://aaron-nathanael-aaronkickstore.pbp.cs.ui.ac.id/

Nomor 1

Checklist 1: Pertama saya membuat direktori bernama "Aaron Kickstore" yang saya gunakan untuk menyimpan proyek Git-nya. Kemudian saya menginisiasi repositori baru dengan perintah git init. Selanjutnya, saya juga membuat repository baru di Github bernama "Aaron-Kickstore". Setelah melakukan inisiasi repositori lokal, langkah selanjutnya adalah menghubungkannya dengan repositori di GitHub. Setelah menghubungkan antara repositori lokal dengan repositori github, saya melakukan clone repositori ke komputer lokal. Selanjutnya, saya mengaktifkan Virtual Environment dengan melakukan "python -m venv env" kemudian mengaktifkannya. Setelah itu, saya membuat berkas requirements.txt dan tambahkan beberapa dependencies. Langkah terakhir, saya membuat dan memodifikasi file ".env", ".env.prod", dan "settings.py", kemudian menjalankan migrasi database dengan cara "python manage.py migrate" dan menjalankan server Django dengan perintah "python manage.py runserver". Proyek Django baru berhasil dibuat.


Checklist 2: Masuk ke direktori utama, kemudian aktifkan virtual environment yang telah dibuat sebelumnya dengan menjalankan perintah "env\Scripts\activate". Kemudian jalankan perintah "python manage.py startapp main" untuk membuat aplikasi baru dengan nama main. Kemudian saya menambahkan "main" dalam list bernama INSTALLED_APPS yang ada di settings.py dari direktori proyek.


Checklist 3: Saya buka berkas urls.py yang ada di dalam direktori proyek dan saya tambahkan rute URL "path('', include('main.urls'))," di list urlpatterns sehingga aplikasi main dapat diakses.


Checklist 4: Saya membuat model pada aplikasi main dengan cara membuat class Product di models.py. Di dalam Class tersebut berisi atribut seperti id, name, price, description, thumbnail, category, dan is_featured.


Checklist 5: Saya memodifikasi views.py dengan menambahkan sebuah function bernama show_main. Function ini akan menyiapkan sebuah dictionary yang berisi data dengan key npm, nama, app_name, dan class. Selanjutnya, saya juga mengubah main.html agar dapat menampilkan data tersebut menggunakan template variables. Terakhir, di bagian akhir function pada views.py, saya return render untuk menangani request HTTP dan menampilkan halaman HTML sesuai data yang telah dikirim dari dictionary tadi.


Checklist 6: Pertama, saya mengonfigurasi routing URL aplikasi main dengan cara membuat berkas urls.py di dalam direktori main, jangan lupa import path dan fungsi show_main dari views.py pada direktori main, kemudian saya mendefinisikan app_name untuk penamaan routing dan urlpatterns yang berisi "path('', show_main, name='show_main')".


Checklist 7: Saya melakukan migration dan commit semua perubahan yang telah dilakukan. Di terminal ketik "git remote add pws https://pbp.cs.ui.ac.id/aaron.nathanael/aaronkickstore", kemudian git branch -M master dan kemudian "git push pws master". Terakhir tinggal buka "https://aaron-nathanael-aaronkickstore.pbp.cs.ui.ac.id/".



Nomor 2

Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya:
https://share.google/images/ki38szasSv8O51SYQ

Penjelasan bagan:

Client

Pengguna mengirim request lewat browser, misalnya membuka URL tertentu di aplikasi Django.

URLconf

Django akan mencocokkan URL yang diminta dengan daftar pola URL yang ada di urls.py. Jika cocok, maka Django akan meneruskan permintaan tersebut ke fungsi View yang sesuai.

Views

View adalah tempat logika utama aplikasi. Dari sini, Django bisa mengambil data dari model dan memilih template untuk menampilkan hasil ke pengguna.

Model

Model berhubungan langsung dengan Database. Di sini terjadi data transaction (membaca, menulis, memperbarui, atau menghapus data). Hasil query dari model dikembalikan ke View dalam bentuk QuerySet atau data lain.

Template

Template adalah file HTML yang sudah diberi placeholder (variabel Django). View akan mengisi template dengan data yang diperoleh dari Model.

Client(Browser)

Akhirnya, Django mengirimkan webpage (HTML yang sudah di-render) kembali ke browser client sebagai respon.


Nomor 3

File settings.py adalah pusat pengaturan untuk proyek Django. Jadi, semua konfigurasi penting dalam proyek yang kita buat akan disimpan di sini, seperti pengaturan keamanan app, pengaturan database, pengaturan aplikasi, pengaturan static dan media files, dll.


Nomor 4

Untuk makemigrations, Django akan mencatat semua perubahan pada file model dan membuat file migrasi yang berisi instruksi bagaimana database perlu diubah. Namun, perubahan ini belum benar-benar diterapkan. Supaya database benar-benar mengikuti perubahan tersebut, kita perlu menjalankan perintah migrate. Perintah ini akan mengeksekusi file migrasi tadi sehingga tabel atau kolom dalam database akan sesuai dengan definisi yang ada di model.


Nomor 5

Menurut saya sendiri, ada beberapa alasan kenapa Django cocok untuk permulaan pembelajaran pengembangan perangkat lunak:
1.Batteries Included

Django sudah menyediakan banyak fitur bawaan seperti autentikasi user, admin panel, ORM, keamanan, routing, dsb. Jadi pemula tidak perlu membangun semuanya dari nol.

2.Struktur proyek yang jelas

Django mengikuti pola arsitektur Model-View-Template (MVT), sehingga pemula lebih cepat untuk memahami alur kerja aplikasi web.

3.Dokumentasi sangat lengkap

Django punya dokumentasi resmi yang mudah dipahami sehingga cocok buat kita untuk belajar secara mandiri.

4.Dipakai di dunia nyata

Banyak perusahaan besar juga memakai Django (misalnya Instagram, Pinterest), jadi belajar Django tidak hanya untuk belajar, tapi juga akan sangat berguna saat kita kerja nanti.


Nomor 6
Sudah bagus, thank you kak!