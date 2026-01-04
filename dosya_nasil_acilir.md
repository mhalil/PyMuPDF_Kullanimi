# Tüm Belge Metni Nasıl Çıkarılır

Bu komut dosyası, parametre olarak bir belge adı alacak ve belgedeki metnin tamamından bir metin dosyası oluşturacaktır.  

Belge [desteklenen dosya türleri](desteklenen_dosya_turleri.md)nden herhangi biri olabilir.  

Komut dosyası (betik), belge adının parametre olarak belirlenmesini bekleyen bir komut satırı aracı olarak çalışır. Betik dizininde “dosyaadı.txt” adında bir metin dosyası oluşturur. Sayfaların metni bir form besleme karakteriyle ayrılır:

```python
import sys, pathlib, pymupdf

fname = sys.argv[1]  # belge adını al
with pymupdf.open(fname) as doc:  # belgeyi aç
    text = chr(12).join([page.get_text() for page in doc])

# ASCII olmayan karakterleri desteklemek için ikili dosya olarak yazın
pathlib.Path(fname + ".txt").write_bytes(text.encode())
```

Çıktı, belgede kodlandığı gibi düz metin olacaktır. Hiçbir şekilde güzelleştirme çabası gösterilmiyor. Özellikle PDF için bu, çıktının normal okuma sırasında olmaması, beklenmeyen satır sonları vb. anlamına gelebilir.  

Bunu düzeltmek için birçok seçeneğiniz vardır; bkz. [bölüm Ek 2: Gömülü Dosyalarla İlgili Dikkat Edilmesi Gerekenler.](https://pymupdf.readthedocs.io/en/latest/app2.html#appendix2). 

Bunlar arasında:

1. Metni HTML biçiminde çıkarın ve herhangi bir tarayıcıda görüntülenebilmesi için HTML belgesi olarak kaydedin.  

2. *Page.get_text(“blocks”)* aracılığıyla metni, metin bloklarının bir listesi olarak çıkarın. Bu listenin her bir öğesi, uygun bir okuma sırası oluşturmak için kullanılabilecek, metninin konum bilgilerini içerir.  

3. *Page.get_text(“words”)* aracılığıyla tekli kelimelerin  bir listesini çıkartın. Öğeleri konum bilgisi içeren kelimelerdir. Belirli bir dikdörtgenin içindeki metni belirlemek için bunu kullanın -- sonraki bölüme bakın.  

Örnekler ve daha fazla açıklama için aşağıdaki iki bölüme bakın.



...

...

devamı gelecek.
