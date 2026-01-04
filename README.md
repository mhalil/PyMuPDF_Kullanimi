# PyMuPDF

**PyMuPDF**, **PDF** (ve diğer) belgelerden veri çıkarılması, analizi, dönüştürülmesi ve işlenmesi için yüksek performanslı bir Python kütüphanesidir / modülüdür.

**PyMuPDF** [GitHub](https://github.com/pymupdf/PyMuPDF)'da barındırılır ve [PyPI](https://pypi.org/project/PyMuPDF/)'a kayıtlıdır.

> Bu belge 1.26.7'ye kadar olan tüm sürümleri kapsamaktadır.

## Konu Başlıkları

## 1) Kurulum

1. Gereksinimler

Aşağıdaki örneklerin tümü, bir Python sanal ortamında çalıştığınızı varsaymaktadır. Ayrıntılar için https://docs.python.org/3/library/venv.html adresine bakın. Ayrıca 
pip'in güncel olduğunu varsayıyoruz.

Örneğin:

- **Windows**:

```python
py -m venv pymupdf-venv
.\pymupdf-venv\Scripts\activate
python -m pip install --upgrade pip
```

- **Linux, MacOS**:

```python
python -m venv pymupdf-venv
. pymupdf-venv/bin/activate
python -m pip install --upgrade pip
```

2. Kurulum

**PyMuPDF** aşağıdakilerle **pip** kullanılarak kurulmalıdır:

```python
pip install --upgrade pymupdf
```

Bu, platformunuz için mevcutsa bir Python tekerleğinden (wheel) kurulacaktır.

## 2) Temel Kullanım

### Dosya Açmak

Bir dosyayı açmak için aşağıdaki kodu kullanabilirsiniz:

```python
import pymupdf

doc = pymupdf.open("a.pdf") # a.pdf dosyasını aç
```

> **NOT**:
> 
> Daha gelişmiş seçenekler için [desteklenen dosya türleri](desteklenen_dosya_turleri.md)nin listesine ve [Dosya Nasıl Açılır](dosya_nasil_acilir.md) Konusundaki Kılavuza bakın.

### PDF'den Metin Çıkarmak

Bir PDF dosyasındaki <u>metnin tamamını</u> çıkarmak için aşağıdaki kodu kullanabilirsiniz:

```python
import pymupdf

doc = pymupdf.open("a.pdf") # a.pdf dosyasını aç
out = open("output.txt", "wb") # çıktı için bir metin dosyası oluştur.
for page in doc: # belge sayfalarında gezinin
    text = page.get_text().encode("utf8") # düz metni al (UTF-8)
    out.write(text) # sayfanın metnini çıktı dosyasına yaz
    out.write(bytes((12,))) # sayfa sınırlayıcıyı yaz
out.close()
```

Elbette metin çıkarılabilen dosya biçimi/formatı yalnızca **PDF** değildir; **MOBI, EPUB, TXT** gibi [desteklenen tüm belge formatları](desteklenen_dosya_turleri.md)ndan metin çıkarılabilir.

> **NOT**:
> 
> Belgeniz resim tabanlı metin içeriği barındırıyorsa, daha sonra metin çıkarmak için **OCR**'yi kullanın:
> 
> ```python
> tp = page.get_textpage_ocr()
> text = page.get_text(textpage=tp)
> ```
> 
> Belirli alanlardan nasıl metin çıkarılacağını veya belgelerden tabloların nasıl çıkarılacağını açıklayan daha birçok örnek var. Lütfen [Metin Nasıl Çıkarılır Kılavuzu](tum_belge_netni_nasil_cikarilir.md)'na bakın.
> 
> Artık metni **Markdown formatında** da çıkarabilirsiniz.
> 
> **API referansı**
> 
> - `Sayfa.get_text()`

### PDF'den Görüntüleri / Resimleri Çıkarın

Bir PDF dosyasındaki tüm görüntüleri / resimleri çıkarmak için aşağıdaki kodu kullanabilirsiniz:

```python
import pymupdf

doc = pymupdf.open("test.pdf") # a.pdf dosyasını aç

for page_index in range(len(doc)): # pdf sayfaları üzerinde gezin
    page = doc[page_index] # sayfayı al
    image_list = page.get_images()

    # sayfada bulunan görsellerin sayısını yazdırın
    if image_list:
        print(f"Found {len(image_list)} images on page {page_index}")
    else:
        print("No images found on page", page_index)

    for image_index, img in enumerate(image_list, start=1): # resim listesini numaralandır
        xref = img[0] # görüntünün XREF'ini alın
        pix = pymupdf.Pixmap(doc, xref) # Pixmap oluştur

        if pix.n - pix.alpha > 3: # CMYK: önce RGB'ye dönüştürün
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

        pix.save("page_%s-image_%s.png" % (page_index, image_index)) # resmi png olarak kaydet
        pix = None
```

> **NOT:**
> 
> Belirli alanlardan nasıl metin çıkarılacağını veya belgelerden tabloların nasıl çıkarılacağını açıklayan daha birçok örnek var. Lütfen [Metin Nasıl Çıkarılır Kılavuzu](tum_belge_netni_nasil_cikarilir.md)'na bakın.
> 
> **API referansı**
> 
> [`Page.get_images()`](https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_images)
> 
> [Pixmap](https://pymupdf.readthedocs.io/en/latest/pixmap.html#pixmap)

### Vektör Grafikleri Ayıklayın

Bir belge sayfasından tüm vektör grafiklerini çıkarmak için aşağıdaki kodu kullanabilirsiniz:

```python
doc = pymupdf.open("some.file")
page = doc[0]
paths = page.get_drawings()
```

Bu, sayfada bulunan herhangi bir vektör çizimi için bir yol sözlüğü döndürecektir.

> **NOT:**
> 
> Lütfen bakınız: [Çizimler Nasıl Çıkarılır.](https://pymupdf.readthedocs.io/en/latest/recipes-drawing-and-graphics.html#recipesdrawingandgraphics-extract-drawings)
> 
> **API referansı**
> 
> [`Page.get_drawings()`](https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_drawings)

...

...

...

devamı gelecek.

## Kaynak:

- [Installation - PyMuPDF documentation](https://pymupdf.readthedocs.io/en/latest/installation.html)
  
- [The Basics - PyMuPDF documentation](https://pymupdf.readthedocs.io/en/latest/the-basics.html)
