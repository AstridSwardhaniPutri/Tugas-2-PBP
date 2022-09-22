Jelaskan perbedaan antara JSON, XML, dan HTML!

**Json** atau JavaScript Object Notation menurut w3shools.com merupakan sebuah format ringan untuk menyimpan dan mengirim data.JSON sering digunakan untuk mengirimkan data dari server ke web page. JSON menyimpan datanya dengan efisien tetapi tidak rapih sehingga sulit dibaca dan dipahami oleh manusia. 
Contoh:
![image](https://user-images.githubusercontent.com/101729344/191658775-9e5b634b-40a7-471c-9d2d-cb6e617dd9a3.png)
Selain itu, JSON juga dapat menyimpan data dalam bentuk array sehingga melakukan transfer data lebih mudah.

**XML** atau eXtensible Markup Language menurut w3shools.com merupakan sebuah software dan hardware-independent tool untuk menyimpan dan membagikan data. XML bersifat self descriptive dengan adanya informasi pengirim dan penerima. XML menyimpan filenya dengan rapih karena terstruktur sehingga mudah dibaca oleh manusia tetapi tidak efisien. 

**HTML** atau HyperText Markup Language bahasa standar untuk membuat web pages. HTML bisa membuat struktur dari sections, paaragraf, dan link dengan elemen dari HTML seperti tags atau attributes.

Perbedaan 
 
Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery digunakan untuk mengirimkan data dari satu stack ke stack lainnya dengan berbagai tipe yaitu JSON, XML, dst. Data delivery ini bisa dilakukan dari developer ke developer atau dari daeveloper ke user. 

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  1. Melakukan startapp mywatchlist di terminal dengan directory sesuai dengan repository
  2. Menambahkan apps mywatchlist di settings.py 
  3. Menambahkan model-model yang diperlukan seperti watched, dst ke model.py
  4. Menambahkan folder fixtures dengan isi initial file untuk load 10 data film
  5. Mengedit views.py untuk menambahkan fitur json dan xml yaitu show_json/xml dan return_xml/json_id
  6. Menambahkan initial file json mywatchlist ke Procfile agar load data sampai ke Heroku
  7. Melakukan deploy ke Heroku dengan normal

Link Heroku mywatchlist:
https://tugas-2-pbp-astrid.herokuapp.com/mywatchlist/

Screenshoot Postman XML
![image](https://user-images.githubusercontent.com/101729344/191657601-23c0019c-f339-476a-b4f8-04ed636a7f1a.png)

Screenshoot Postman JSON
![image](https://user-images.githubusercontent.com/101729344/191657755-f57793ad-f6c0-41ae-8108-314d43cd0944.png)

