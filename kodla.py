import pymupdf

# #dosya = pymupdf.open("excel.pdf")
dosya = pymupdf.open("calc.pdf")

sayfa_sayisi = len(dosya)
metadata = dosya.metadata
sayfa = dosya.load_page(119)
icerik = sayfa.get_text()
resim  = sayfa.get_pixmap()

# #for _ in range(3):
	# #dosya.new_page()	# dosya sonuna döngü sayısı kadar boş sayfa ekle
	
# #kayit = dosya.save("sayfa eklendi.pdf") # yapılan değişiklikleri kaydet, değişiklik yoksa dosyayı kopyalar

tablo_bul = sayfa.find_tables()	# sayfadaki tabloları bulur. Obje döndürür. tablo için en az 2x2 veri olmalı.
tablolar = tablo_bul.tables		# liste yapısında çıktı verir. liste içinde obje bilgileri bulunur.
tablo_sayisi = len(tablolar)	# liste sayısı, tablo uzunluğu demektir.
tablo_1_icerigi = tablolar[0].extract()	# liste içinde liste veri yapısı döndürür. Satır verileri, listeler halinde peşpeşe eklenir.

df = tablolar[0].to_pandas()	# sayfadaki ilk tablo içeriği df'ye dönüşür




# #print(tablo_1_icerigi)
# #print(tablo_sayisi)
print(df)


