Link menuju aplikasi Heroku : https://tugas-2-pbp-astrid.herokuapp.com/katalog/
![Bagan](/gambar_PBP/PBP.png)


Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual environment digunakan untuk memisahkan setiap pengaturan yang diinstall pada setiap proyek Django. Sehingga satu proyek dengan proyek lainnya tidak akan tercampur pengaturannya karena masing-masing project memiliki virtual environmentnya sendiri. Kita bisa membuat project Django tanpa menggunakan virtual environment tetapi tidak akan ada constraint atau pembatas antara satu project dengan project lainnya.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
    1. Membuat fungsi pada views. py bernama show_catalog dengan parameter request, lalu membuat dictionary dengan keynya berupa list_barang, nama, dan NPM. Lalu returnnya adalah  render(request, "katalog.html", context), katalog.html merupakan template.
    2. Untuk melakukan routing, maka kita melakukan pengaturan dalam urls.py dengan menuliskan nama dari aplikasi yaitu katalog dan menuliskan urlscode dengan input path('', show_catalog, name='show_catalog'),]. Lalu, kita juga melakukan setup urls.py pada folder project_django dengan menambahkan aplikasi katalog ke dalam urlpatterns dengan sintaks  path('katalog/',include('katalog.urls')),
    3. Lalu melakukan edit di katalog.html dengan membuat nama dan npm. Selain itu, juga membuat table di html yang memuat nama barang, rating barang, deskripsi barang, dll
    4. Melakukan deploy ke heroku dengan melakukan setup di github secret action memasukan heroku api key dan name

