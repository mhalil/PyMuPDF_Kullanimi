# PyMuPDF Kütüphanesi ve Metotları

## Kütüphaneyi İçe aktar

Bildiğiniz gibi kütüphaneyi kullanabilmek için öncelikle, projemize dahil etmemiz gerekir ve bunu klasik yöntem olan `import` metodu ile gerçekleştiriyoruz.

```python
import pymupdf
```

## `.open()` ile Dosya Açmak veya Dosya Oluşturmak

`.open()` metodu, mevcut bir PDF dosyasını açmak veya yeni bir belge nesnesi oluşturmak için kullanılır.

```python
doc = pymupdf.open("dosya_adi.pdf")
```

## `.metadata` ile Dosya Bilgilerini Görüntüle

`.metadata` metodu, genellikle dosyanın **başlığı, yazarı, oluşturulma tarihi, düzenlenme tarihi ve dosya formatı** gibi bilgileri içeren bir Python sözlüğü (dictionary) döndürür.

```python
doc.metadata
```

`.metadata` metodu bir kitabın **kapak bilgilerine veya künye sayfasına** bakmak gibidir. Kitabı hiç açmadan yazarının kim olduğunu, ne zaman basıldığını ve adının ne olduğunu bu sayede hemen öğrenebiliriz.

## `.load_page()` ile Sayfaya Erişmek

`.load_page()` metodu ile açılan belgenin belirli bir sayfasına (sayfa numarası üzerinden) erişim sağlanır.

```python
page = doc.load_page(pno)
```

## `.get_text()` ile Metin Ayıklamak

`.get_text()` metodu, seçilen sayfadaki tüm metni ayıklayıp almanıza olanak tanır.

```python
text = page.get_text()
```

`get_text()` metodu, kullanılan parametrelere göre farklı detay seviyelerinde veri sunar:

• **Temel Çıktı:** Varsayılan ayarlarda metni tek bir karakter dizisi (string) olarak döndürür.

• **Blok Yapısı:** `blocks` parametresi; metnin konumunu, içeriğini ve blok numarasını içeren bir liste sunar.

• **Detaylı Sözlük (Dict):** `dict` parametresi; yazı tipi, boyutu, rengi ve yazım yönü gibi en detaylı bilgileri içeren bir sözlük yapısı döndürür.

• **Gelişmiş Ayarlar:** Metinlerin doğal okuma sırasına göre dizilmesi için `sort=True` parametresi kullanılabilir. Ayrıca, `clip` parametresi ve bir `rect` (dikdörtgen) nesnesi ile sayfanın sadece belirli bir alanındaki metinler ayıklanabilir.

## `.get_pixmap()` ile Sayfayı Resme Dönüştür

`.get_pixmap()` metodu, PDF sayfasını bir resim dosyasına (raster görüntü) dönüştürmek için kullanılır.

```python
page.get_pixmap()
```

## `.new_page()` ile Yeni Sayfa Eklemek

Yeni bir sayfa eklemek için `new_page()` komutu kullanılır.

```python
doc.new_page() # PARAMETRE NE OLACAK , EKLE
```

## `.move_page()` ile Sayfa Sırasını Değiştirmek

Sayfaların sırasını değiştirmek için `move_page()`

## `.delete_page()` ile Sayfa Silmek

Belirli bir sayfayı silmek / kaldırmak için `.delete_page()` metodu kullanılır.

## `.full_copy_page()` ile Sayfayı Kopyala / Çoğalt

Bir sayfayı çoğaltmak / kopyalamak için `.full_copy_page()` metodu kullanılır.

## `.find_tables()` ile Sayfadaki Tabloları Bul

Sayfadaki tabloları bulmak için `.find_tables()` metodu kullanılır.

## `.extract()` ile Tablo verilerini Almak

Tablo verileri `.extract()` metodu ile Python listesi olarak alınabilir .

## `.to_pandas()` ile Tabloyu Veri Çerçevesine Çevir

Tablo verileri, doğrudan **pandas** DataFrame'ine dönüştürülmek üzere `to_pandas()` metodu kullanılabilir.

## `.get_page_images()` ile Görselleri Listelemek

Bir sayfadaki görseller `.get_page_images()` metodu ile listelenebilir.

## `.extract_image()` ile Görüntü Bilgileri Elde Etmek

Görselin referans numarası (xref) kullanılarak `extract_image()` metodu ile görüntünün içeriği (ikili formatta), uzantısı ve boyutları elde edilir. Alternatif olarak, `xref_length()` üzerinden tüm belge taranarak da görüntülere ulaşılabilir.

## `.insert_text()` ile Basit Metin Eklemek

`.insert_text()` metodu ile belirli bir koordinata basit metin eklenir.

## `.insert_htmlbox()` ile Zengin Metin ve Tablo Eklemek

`.insert_htmlbox()` metodu, HTML etiketleri ve CSS kullanarak stil verilmiş metinler, tablolar veya linkler eklemeye olanak tanır.

## `.insert_textbox()` ile Metni Alana Yerleştirmek

.`insert_textbox()` metodu, metni tanımlanan bir dikdörtgen alan (rect) içine sığdıracak şekilde yerleştirir.

## `.write_text()` ile Gelişmiş Özl. Metin Eklemek

`.write_text()`:`TextWriter` nesneleri aracılığıyla opaklık ve istenilen açıda döndürme (rotation) gibi gelişmiş özelliklerle metin eklenmesini sağlar.

## `.save()` ile Kaydet

`.save()` Metodu, belge üzerinde yapılan ekleme veya düzenlemeleri kaydeder.

```python
`doc.save("yeni_dosya.pdf")`
```
