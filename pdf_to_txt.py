# #### PDF'ten TXT'ye Dönüştür ###

import pymupdf

pdf_dosyasi = input("PDF dosyasının adını (uzantısız) yazın (Ör.: E-Kitap): ")
icerik = pymupdf.open(pdf_dosyasi + ".pdf") # a.pdf dosyasını aç
cikti_dosyasi = open(pdf_dosyasi + ".txt", "wb") # çıktı için bir metin dosyası oluştur.

for sayfa in icerik: # belge sayfalarında gezinin
    text = sayfa.get_text().encode("utf8") # düz metni al (UTF-8)
    cikti_dosyasi.write(text) # sayfanın metnini çıktı dosyasına yaz/ekle
cikti_dosyasi.close()
