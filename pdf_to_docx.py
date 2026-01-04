### PDF'ten DOCX'e Dönüştür ###

from pdf2docx import Converter

pdf_dosyasi = input("PDF dosyasının adını (uzantısız) yazın (Ör.:  Dokuman): ")
docx_dosyasi = pdf_dosyasi + '.docx'

# PDF'i DOCX'e dönüştür
cv = Converter(pdf_dosyasi + ".pdf")
cv.convert(docx_dosyasi) # varsayılan olarak tüm sayfaları dönüştür
cv.close()
