<div class="w3-panel w3-red">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/w3.css">
<body background="anime1.JPG">
<div class="w3-container">
     <center>
	 <p><h1>MEMBUAT MENU NAVIGASI
</div>
</div>

<div class="w3-bar w3-brown w3-card-4">
<button class="w3-bar-item w3-button" onclick="openKota('Kucing Persia')">Kucing Persia</button>
<button class="w3-bar-item w3-button" onclick="openKota('Kucing Kampung')">Kucing Kampung</button>
<button class="w3-bar-item w3-button" onclick="openKota('Kucing Siam')">Kucing Siam</button>
<div class="w3-dropdown-hover">
    <button class="w3-button">Animasi</button>
	<div class="w3-dropdown-content w3-bar-block w3-card-4">
	  <button class="w3-bar-item w3-button" onclick="openKota('DataDiri')">DataDiri</button>
	  <button class="w3-bar-item w3-button" onclick="openKota('Spin')">Spin</button>
	  <button class="w3-bar-item w3-button" onclick="openKota('Left')">Left</button>
	  <button class="w3-bar-item w3-button" onclick="openKota('Right')">Right</button>
	  <button class="w3-bar-item w3-button" onclick="openKota('Opacity')">Opacity</button>
	  <button class="w3-bar-item w3-button" onclick="openKota('Zoom')">Zoom</button>
	</div>
</div>

<div id="Top" class="w3-container kota w3-animate-top" style="display:none">
 <h2>Animasi TOP</h2>
 <hr>
 <img src="css/anime6.jpg.JPEG" style="width:20%">
</div>
<div id="DataDiri" class="w3-container kota w3-animate-DataDiri" style="display:none">
 <h2>Nama : Asri Nurfadilah Azzahra
 <br>
 NIM : 10123099
 <br>
 Kelas : IF-2</h2>
 <hr>
 <img src="css/walpaperjpg.JPG" style="width:20%">
</div>
<div id="Spin" class="w3-container kota w3-spin" style="display:none">
 <h2>Animasi SPIN</h2>
 <hr>
 <img src="css/anime.2.jpg">
</div>
<div id="Left" class="w3-container kota w3-animate-left" style="display:none">
 <h2>Animasi LEFT</h2>
 <hr>
 <img src="css/anime.2.jpg">
</div>
<div id="Right" class="w3-container kota w3-animate-right" style="display:none">
 <h2>Animasi RIGHT</h2>
 <hr>
 <img src="css/anime.2.jpg">
</div>
<div id="Opacity" class="w3-container kota w3-animate-opacity" style="display:none">
 <h2>Animasi OPACITY</h2>
 <hr>
 <img src="css/anime.2.jpg">
</div>
<div id="Zoom" class="w3-container kota w3-animate-Zoom" style="display:none">
 <h2>Animasi Zoom</h2>
 <hr>
 <img src="css/anime.2.jpg">
</div>
<div id="Latihan10" class="w3-container kota w3-anime-zoom" style="display:none">
<div class="w3-panel w3-brown">
</div>
</div>
<div id="Kucing Persia" class="w3-container kota" style="display:none">
<img src="css/persia.JPG" style="width:20%"><img src="css/Kucingpersia.JPG" style="width:20%">
 <h2>Kucing persia adalah ras kucing domestik berbulu panjang dengan karakter wajah bulat dan moncong pendek. Namanya mengacu pada Persia, nama lama Iran, di mana kucing serupa ditemukan. Sejak akhir abad 19, kucing jenis ini dikembangkan di Britania Raya dan Amerika Serikat usai Perang Dunia II.</h2>
 <h2>Cara Perawatan Kucing Persia :
<br>
1. Melakukan Grooming.
2. Bersihkan Mata dan Telinga.
3. Memotong Kuku & Sikat Gigi.
4. Vaksin. 
5. Sterilisasi. 
6. Perhatikan Nutrisi.
7. Air Minum Bersih. 
8. Perhatikan Kebersihan Kandang dan Toilet Kucing.</h2>
</div>
<div id="Kucing Kampung" class="w3-container kota" style="display:none">
<img src="css/Kucingkampung.JPG" style="width:20%"><img src="css/Kucingkampung(2).JPG" style="width:20%">
<h2>Kucing liar adalah pemangsa berukuran kecil yang berasal dari Eropa, Asia bagian barat, dan Afrika. Binatang ini adalah pemburu mamalia kecil seperti tikus, burung, dan makhluk lain yang berukuran serupa. Kucing liar adalah salah satu pemanjat yang baik dan sering menangkap mangsanya di tanah.</h2>
<h2>Perawatan Kucing Kampung tidak memiliki perawatan khusus seperti kucing lainnya karena daya tubuh nya yang lebih kebal daripada kucing lainnya</h2>
</div>
<div id="Kucing Siam" class="w3-container kota" style="display:none">
<img src="css/Siam(2).JPEG" style="width:20%"><img src="css/Siam.JPEG" style="width:20%">
 <h2>Kucing siam adalah salah satu ras kucing pertama yang diakui jelas sebagai kucing berjenis oriental. Sesuai dengan namanya, kucing siam berasal dari negara Siam, sehingga ras kucing ini sangat mudah ditemukan di negara Thailand.</h2>
 <h2>Cara Perawatan Kucing Siam:
 <br>
1. Sediakan hiburan yang cukup, seperti mainan atau tempat terbuka.
2. Bersihkan bulu kucing secara berkala, minimal dua minggu sekali.
3. Berikan makanan sesuai usia.
4. Bawa ke dokter hewan secara berkala untuk memastikan kesehatannya.
4. Luangkan waktu selama 15–30 sehari untuk mengajak kucing bermain.</h2>
</div>
</div>


<script>
function openKota(namaKota) {
 var i;
 var x = document.getElementsByClassName("kota");
 for (i = 0; i < x.length; i++) {
 x[i].style.display = "none"; 
 }
 document.getElementById(namaKota).style.display = "block"; 
}
</script>