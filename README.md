Nama : Aaron Nathanael Suhaendi

NPM : 2406437073

Kelas : PBP B

Tautan PWS: https://aaron-nathanael-aaronkickstore.pbp.cs.ui.ac.id/


Tugas 5

Nomor 1

Urutan dari prioritas tertinggi hingga terendah:

1.!important
Alasan: Dipakai untuk menandai aturan yang harus meng-override semua aturan lain
Bobot: Tidak dihitung dalam specificity, tapi langsung diprioritaskan paling tinggi

2.Inline styles
Alasan: Ditulis langsung di elemen HTML, dianggap paling spesifik
Contoh: <h1 style="color:pink;">
Bobot: 1000

3.ID selector
Alasan: karena ID unik di dalam satu halaman, jadi tingkat spesifisitasnya tinggi
Contoh: #header { color: blue; }
Bobot: 0100

4.Class, attribute, pseudo-class
Alasan: Class bisa dipake berulang kali, jadi lebih lemah dari ID, tapi lebih kuat dari elemen biasa
Contoh: .title {}, [type="text"] {}, :hover {}
Bobot: 0010

5.Element dan pseudo-element
Alasan: Selector paling umum, hanya menargetkan tag HTML atau pseudo-element
Contoh: p {}, h1 {}, ::before {}
Bobot: 0001

6.Universal selector & :where()
Alasan: Digunakan untuk menargetkan semua elemen atau reset, tanpa menambah kekuatan spesifisitas
Contoh: * { margin:0; }, :where(.box) {}
Bobot: 0000


Nomor 2

Mengapa Responsive Design Penting dalam Web Development:

1.Perbedaan Ukuran Layar
Pengguna mengakses web lewat berbagai perangkat: laptop, tablet, smartphone. Responsive design memastikan tampilan menyesuaikan ukuran layar.

2.User Experience/UX
Web yang tidak responsive bikin teks terlalu kecil, tombol susah diklik, atau layout berantakan. Responsive design membuat navigasi tetap nyaman di semua perangkat.

3.SEO (Search Engine Optimization)
Google memberi peringkat lebih tinggi pada website yang mobile-friendly. Jadi, responsive design langsung berdampak ke visibilitas di search engine.

4.Efisiensi Maintenance
Daripada bikin versi desktop dan mobile terpisah, responsive design cukup dengan satu basis kode, lebih efisien dan mudah dipelihara.

Aplikasi yang sudah menerapkan responsive design:
Tokopedia / Shopee: Diakses lewat laptop, tampilannya berupa grid produk besar. Kalo di HP, tampilannya berubah jadi list dengan tombol besar agar mudah ditekan jari.
Alasan: Membuat pengguna nyaman belanja dari device apapun sehingga dapat meningkatkan engagement dan penjualan.

Aplikasi yang belum responsive: 
Website lama instansi pemerintah atau portal berita jadul, biasanya kalo dibuka di HP harus zoom in–out, tombol terlalu kecil, dan layout pecah.
Alasan: Karena belum didesain untuk mobile-first, jadinya UX masih jelek sehingga pengguna lebih cepet bosen.


Nomor 3

Margin, border, dan padding adalah bagian dari CSS box model yang berfungsi mengatur tata letak elemen di halaman web. Margin adalah ruang kosong di bagian luar elemen yang berfungsi memberi jarak antara satu elemen dengan elemen lainnya. Ruang ini tidak terlihat karena sifatnya transparan, tapi sangat penting untuk menjaga tata letak agar elemen tidak saling menempel. Sementara itu, border adalah garis yang mengelilingi elemen dan berada di antara margin dan padding. Border dapat diatur ketebalannya, warnanya, maupun jenis garisnya, sehingga selain sebagai pembatas, border juga dapat digunakan sebagai elemen dekoratif. Dan yang terakhir, padding adalah ruang kosong di dalam elemen, yaitu jarak antara konten (seperti teks atau gambar) dengan border. Padding memastikan konten tidak terlalu menempel pada border, sehingga tampilannya lebih rapi dan nyaman dibaca.


Cara Implementasi di CSS

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Implementasi Margin, Border, dan Padding</title>
  <style>
    .box {
      margin: 30px;
      border: 5px solid blue;
      padding: 20px;
      background-color: lightyellow;
    }
  </style>
</head>
<body>
  <div class="box">
    Test doang
  </div>
</body>
</html>


Nomor 4

Flexbox (Flexible Box Layout) adalah sebuah metode tata letak di CSS yang dirancang untuk mengatur elemen dalam satu dimensi, baik secara horizontal (baris) maupun vertikal (kolom). Flexbox sangat berguna ketika kita ingin membuat elemen di dalam sebuah container agar mudah diatur jarak, ukuran, dan posisinya tanpa harus menggunakan float atau positioning manual. Kelebihan utama flexbox adalah fleksibilitasnya dalam menyesuaikan elemen sesuai ukuran layar atau ruang yang tersedia. Sementara itu, CSS Grid Layout adalah sistem tata letak dua dimensi yang lebih kuat karena memungkinkan kita mengatur elemen baik dalam baris maupun kolom secara bersamaan. Grid nya bekerja seperti tabel yang modern, di mana kita bisa mendefinisikan baris dan kolom, lalu menempatkan elemen ke posisi tertentu dengan mudah.


Nomor 5

Checklist 1: Untuk implementasi fitur edit product, saya menambahkan fungsi edit_product di views.py, membuat file HTML bernama edit_product.html, melakukan routing URL, dan melakukan sedikit modifikasi pada tombol di main.html. Proses yang mirip juga saya lakukan untuk implementasi fitur delete product. Dengan langkah ini, aplikasi menjadi lebih interaktif karena user tidak hanya bisa menambah produk, tetapi juga mengedit maupun menghapus produk yang sudah ada.

Checklist 2: Saya menggunakan tailwind untuk CSS framework pada aplikasi yang saya buat. Saya menyambungkan django dan tailwind dengan menambahkan script cdn tailwind di bagian head base.html.

Checklist 3: Untuk halaman login, register, tambah product, edit product, dan detail product, saya melakukan kustomisasi tampilan supaya lebih menarik. Perubahan yang saya lakukan adalah mengganti palet warna default yang awalnya hijau-putih menjadi ungu neon dengan kombinasi hitam/abu gelap sebagai latarnya. Saya juga menambahkan efek glow (drop shadow neon) pada teks maupun tombol agar lebih konsisten dengan tema gelap yang saya mau.

Checklist 4: Untuk halaman daftar product, saya mengimplementasikan tampilan dengan gaya card tetapi memodifikasi dari tutorial. Jika belum ada produk, halaman akan menampilkan gambar ilustrasi beserta pesan bahwa belum ada product yang terdaftar. Jika sudah ada produk, maka tiap produk ditampilkan dalam bentuk card dengan border ungu neon dan ada shadownya, sehingga tidak terlalu menyatu dengan background. Pada tiap card, saya menambahkan dua tombol untuk mengedit dan menghapus product, dengan warna ungu neon juga.

Checklist 5: Untuk navigation bar, saya membuatnya responsive sehingga tampilannya menyesuaikan antara versi mobile dan desktop. Navbar memiliki logo "Aaron Kickstore" dengan efek ungu neon dan juga udah saya integrasikan ke halaman utama (main.html). Pada versi desktop, menu navigasi tampil horizontal, sedangkan pada versi mobile menggunakan tombol hamburger menu yang bisa diklik untuk menampilkan daftar link. Saya juga menambahkan efek transisi hover berwarna neon agar lebih interaktif.



Tugas 4


Nomor 1

AuthenticationForm adalah form bawaan Django yang digunakan untuk proses login user. Form ini berfungsi untuk memeriksa apakah username dan password yang dimasukkan pengguna sudah sesuai dengan data user yang sudah terdaftar di database. Kelebihan utama AuthenticationForm adalah karena sudah disediakan langsung oleh Django sehingga kita tidak perlu membuat form login dari awal lagi. Selain itu, keamanannya juga sudah terjamin karena Django otomatis menangani validasi password, pengecekan akun aktif, serta sudah terintegrasi dengan sistem autentikasi bawaan. Namun, AuthenticationForm memiliki beberapa kekurangan, seperti kurang fleksibel ketika aplikasi membutuhkan metode login khusus, misalnya login dengan email, nomor telepon, atau kode OTP (ini karena hanya mendukung metode login dengan username dan password). Tampilan default nya juga bisa dibilang cukup sederhana sehingga biasanya perlu penyesuaian biar sesuai dengan desain aplikasi. 

Nomor 2

Autentikasi itu proses untuk memastikan identitas pengguna. Contohnya misal kita login dengan username dan password yg kita punya, sistem akan ngecek apakah data itu benar dan cocok dengan akun yang ada. Sementara Otorisasi itu proses untuk menentukan apa saja yang boleh dilakukan pengguna setelah dia berhasil login. Contohnya misal seorang admin bisa menghapus data, tapi user biasa hanya bisa melihat datanya aja dan gabisa menghapusnya. 
Dalam Django, autentikasi dilakukan dengan bantuan model User, fungsi login()/logout(), serta form bawaan seperti AuthenticationForm. Prosesnya adalah Django akan mencocokkan username atau email dan password yang dimasukkan dengan data user di database. Kalau cocok, Django akan membuat session sehingga user dianggap sudah login. Sementara itu, otorisasi di Django diatur lewat sistem permissions dan groups. Setiap user bisa diberi izin tertentu, misalnya can_add_product atau can_delete_user, atau dimasukkan ke dalam grup seperti "Admin" yang memiliki hak akses khusus. Dengan cara ini, Django bisa mengatur siapa aja yang boleh melakukan tindakan tertentu atau mengakses halaman tertentu di dalam aplikasi.

Nomor 3

Session dan cookies sama-sama digunakan untuk menyimpan state atau informasi pengguna di aplikasi web, tapi cara kerjanya berbeda dan masing-masing punya kelebihan dan kekurangan. Cookies disimpan langsung di browser pengguna sehingga server tidak perlu menyimpan banyak data. Kelebihannya adalah cookies ringan untuk server dan bisa dipakai lintas sesi atau perangkat. Namun, cookies lebih rentan terhadap pencurian data dan ukuran datanya terbatas. Sementara itu, session menyimpan data di server, sedangkan browser nya hanya menyimpan ID session lewat cookie. Kelebihannya adalah data lebih aman karena detailnya ada di server, dan bisa menyimpan informasi yang lebih besar atau sensitif. Kekurangannya adalah session ini membebani server karena harus menyimpan data setiap user dan kalo gak dikelola dengan baik bisa membuat server cepet penuh. Jadi pada intinya, cookies cocok untuk menyimpan data kecil yang tidak terlalu penting, sedangkan session lebih cocok untuk data sensitif.

Nomor 4

Penggunaan cookies sebenernya tidak sepenuhnya aman secara default karena ada beberapa resiko yang harus diwaspadai, seperti pencurian cookies lewat serangan Cross-Site Scripting (XSS) atau penyalahgunaan cookies lewat Cross-Site Request Forgery (CSRF). Jika cookie berisi informasi penting, maka kebocoran bisa sangat berbahaya. Tapi untuk mengurangi resiko ini, Django sudah menyediakan pengaturan keamanan bawaan, misalnya HttpOnly agar cookie tidak bisa diakses lewat JavaScript, Secure agar cookie hanya terkirim lewat HTTPS, dan CSRF token untuk melindungi dari serangan CSRF. Selain itu, Django juga punya SESSION_COOKIE_AGE SESSION_COOKIE_SECURE, dan SESSION_COOKIE_HTTPONLY untuk mengatur seberapa lama dan seaman apa cookie disimpan.

Nomor 5

Checklist 1: Saya mengimplementasikan fitur registrasi, login, dan logout agar pengguna bisa mengakses aplikasi sebelumnya sesuai dengan status login/logout mereka. Untuk registrasi, saya menggunakan UserCreationForm bawaan Django dengan bantuan messages untuk menampilkan notifikasi. Saya juga membuat fungsi register di views.py yang akan memproses data dari form dan otomatis membuat akun baru ketika data disubmit, lalu menampilkan halaman register.html. Untuk login, saya membuat fungsi login_user di views.py yang berfungsi mengautentikasi pengguna dan juga membuat halaman login.html untuk tampilannya. Untuk logout, saya menambahkan fungsi logout_user agar pengguna bisa logout. Kemudian saya hubungkan semua fungsi tadi lewat urls.py dengan menambahkan path nya masing-masing. Selain itu, saya juga membuat fungsi show_main dan show_product yang hanya bisa diakses oleh pengguna yang sudah login dan juga menambahkan @login_required pada kedua fungsi tersebut.


Checklist 2: Saya membuat 2 akun pengguna dan menambahkan 3 dummy data pada masing-masing akun. Ini saya lakukan di local, bukan di PWS.


Checklist 3: Saya import User dan menambahkan atribut baru bernama user di dalam class Product di models.py. Kemudian, saya memodifikasi fungsi show_main dan create_product di dalam views.py.


Checklist 4: Pada fungsi show_main, saya menambahkan request.user ke dalam context agar informasi pengguna yang sedang login bisa dipindahkan ke template melalui fungsi render. Selain itu, saya juga menambahkan request.COOKIES.get('last_login', 'Never') untuk mengirimkan data last login dari cookies. Saya juga mengatur Cookies last_login saat pengguna melakukan login melalui fungsi login_user dan akan dihapus ketika pengguna logout melalui fungsi logout_user. Saya juga mengedit main.html dengan menambahkan {{ last_login }} agar informasi waktu last login bisa ditampilkan kepada pengguna.


Tugas 3

Nomor 1

Kita butuh data delivery dalam sebuah platform agar data bisa dikirim dari satu tempat ke tempat lain dengan benar, cepat, dan aman. Kalau tidak ada data delivery, platform tidak akan bisa jalan karena tidak ada cara untuk mengirim atau menerima data antara pengguna, server, atau sistem. Dengan adanya data delivery, informasi bisa sampe ke pengguna dengan tepat, aksesnya cepat, dan data juga tetap aman. Selain itu, data delivery juga penting kalau platform harus terhubung dengan layanan lain, misalnya payment gateway atau API. Misalnya user minta data produk, server harus bisa mengirim datanya dengan format tertentu(misal XML/JSON/HTML). Tanpa adanya mekanisme ini, user tidak akan bisa melihat data yang mereka butuhkan di platform.

Nomor 2

Menurut saya sendiri, JSON lebih baik dibandingkan XML. Alasannya adalah karena JSON punya ukuran file yang lebih kecil sehingga proses transfer data bisa lebih cepat daripada XML. Selain itu, JSON juga lebih ringkas dan gampang dibaca karena strukturnya sederhana dan tidak dipenuhi tag-tag kosong seperti XML. File JSON juga terlihat lebih bersih dan terorganisir, sedangkan XML cenderung lebih rumit dan terkesan ketinggalan zaman karena struktur tag-nya bikin file jadi lebih besar dan susah dibaca. Jadi, menurut saya hal-hal tersebutlah yang membuat JSON lebih populer dan banyak dipake dibandingkan XML.

Nomor 3

is_valid() dipakai untuk ngecek apakah data yang diinput user sesuai aturan form (misalnya field wajib diisi, format email benar, dll). Kita butuh method ini supaya data yang masuk ke database tetep bersih dan valid, jadi tidak ada data aneh-aneh atau error saat diproses.

Nomor 4

csrf_token berfungsi untuk melindungi form dari serangan CSRF(Cross Site Request Forgery). Kalau kita gak pake token ini, penyerang bisa bikin form palsu di website lain yang diem-diem mengirim request ke server kita atas nama user yang sedang login. Akibatnya, data user bisa dimanipulasi tanpa sepengetahuan mereka.

Nomor 5

Checklist 1: Saya menambahkan empat fungsi baru di views.py, yaitu show_xml, show_json, show_xml_by_id, dan show_json_by_id. Keempat fungsi ini menggunakan HttpResponse dan serializers untuk menampilkan data dalam format XML atau JSON.

Checklist 2: Setelah itu, saya mengedit urls.py dengan mengimport fungsi tadi dan menambahkan path baru, supaya masing-masing fungsi bisa diakses lewat URL tadi.

Checklist 3: Saya membuat fungsi create_product dan show_product di views.py, lalu menambahkan route nya di urls.py. Lalu di main.html, saya menambahkan button “Add” dan juga looping supaya semua produk bisa ditampilkan. Saya juga membuat file create_product.html untuk menampilkan form tambah produk.

Checklist 4: Saya membuat forms.py yang berisi class ProductForm untuk menerima input data produk dari user. Lalu saya import ProductForm ke dalam views.py. Setelah itu, saya menambahkan product_list = Product.objects.all() ke dalam function show_main dan memasukkannya ke context supaya semua produk dari database bisa otomatis ditampilkan di halaman main.html.

Checklist 5: Saya membuat file product_detail.html yang terhubung dengan show_product di views.py untuk menampilkan detail setiap produk, lalu menambahkan routing nya di urls.py.


Nomor 6

Sudah mantap kak, semuanya sudah jelas. Thank you so much!!!

Nomor 7
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

Tugas 2

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


Penjelasan untuk kaitan antara urls.py, views.py, models.py, dan berkas html:

urls.py berfungsi sebagai peta jalur (routing). Saat client mengirim request lewat browser, Django akan mencocokkan alamat URL dengan daftar pola URL yang ada di urls.py. Dari sini, request diteruskan ke fungsi yang sesuai di views.py.

views.py berisi logika aplikasi. Di sini, request diproses: bisa saja views mengambil atau mengolah data dari models.py, lalu memilih template HTML yang sesuai untuk ditampilkan ke pengguna.

models.py bertugas sebagai penghubung dengan database. Jika views membutuhkan data, views akan meminta ke models. Models kemudian melakukan query ke database dan mengembalikan hasilnya ke views.

Berkas HTML (Template) digunakan untuk menampilkan hasil ke pengguna. Views akan mengisi template dengan data yang sudah diambil dari models. Template ini kemudian di-render menjadi halaman web yang utuh, lalu dikirim kembali sebagai response ke browser client.

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