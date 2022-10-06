1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
2. 
  >Internal
    > Memasukan <style> tag ke dalam <head> tag
    > Cocok digunakan jika ingin mengedit single page
    > Memakan waktu yang banyak ketika mengedit multiple pages 
    > Dapat menggunakan class dan ID selector 
    > Kode tidak terlalu efisien dalam HTML dokumen karena akan menambahkan ukuran page dan loading time
  
  >Inline
    > Digunakan untuk melakukan styling elemen spesifik HTML
    > Tidak terlalu direkomendasikan karena setiap tag dikustomisasi secara individual
    > Tidak perlu menambahkan eksternal dokumen untuk melakukan styling
    > Melakukan styling banyak elemen dapat mempengaruhi ukuran dari page dan download time
  
  >External
    > Menghubungkan page kita dengan eksternal page dengan ekstensi .css
    > Efisien untuk melakukan styling website dengan jumlah yang besar
    > Memiliki struktur yang rapih karena terpisah dari file HTML
    > Satu page .css bisa digunakan untuk banyak pages
    > Terkadang page tidak terender dengan baik sampai eksternal css terloaded
  
2. Jelaskan tag HTML5 yang kamu ketahui.
  
  a. <img src="..."/> : merupakan sebuah tag untuk memunculkan gambar yang bisa berasal dari url maupun local file
  b. <button></button> : sebuah tag untuk menampilkan button yang bisa dikustomisasi warna dan aksi setelah ditekan
  c. <nav></nav> : tag untuk membuat navbar dengan isinya dapat kustomiasi berisi button, text, atau dropdown
  d. <table></table> : tag untuk membuat table 
     
3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
  
  a. * : digunakan untuk memilih seluruh elemen
  b. . : memilih elemen dengan suatu class tertentu
  c. # : memilih elemen dengan id tertentu
  d. " " : memilih elemen dengan string tertentu
  
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  
    a. Seluruh pengeditan diseluruh page dibuat pada HTML pages masing-masing dengan menggunakan framework Bootstrap.
    b. Menambahkan head HTML pad seluruh page
    c. Membuat seluruh elemen menjadi responsif
    d. Melakukan penambahan elemen yang diperlukan seperti button, dll
