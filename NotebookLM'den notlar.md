# NotebookLM Notları

**PyMuPDF** kütüphanesinin temel işleyişine dair genel teknik bilgileri aşağıda özetliyorum.

Bir PDF belgesini bir kütüphane kitabı olarak düşünürsek; `get_text` komutu kitabın içindeki sayfaları okumak gibidir,

**Analoji:** PyMuPDF kütüphanesini kullanmak, **akıllı bir büyüteçle kapalı bir kitabı incelemeye** benzer; 

`open` komutuyla kitabı elinize alır, 

`load_page` ile istediğiniz sayfayı açar ve 

`get_text` ile büyüteciniz sayesinde sayfadaki tüm yazıları anında kağıda dökersiniz.

----------------

**PyMuPDF** kütüphanesi PDF belgelerini **oluşturmak, düzenlemek ve veri ayıklamak** için kullanılan kapsamlı bir araçtır.

• **Görselleştirme:** Ayıklanan ve temizlenen veriler, analiz edildikten sonra **Matplotlib** gibi kütüphanelerle grafiklere dönüştürülebilir.



**Özet Analoji:** PyMuPDF kullanımı bir **restoran mutfağını yönetmeye** benzer; `open` ile mutfağa girer, `get_text` veya `find_tables` ile dolaptaki malzemeleri (verileri) istediğiniz detayda seçip çıkarır, `insert_text` veya `move_page` ile tabağı (sayfayı) yeniden düzenler ve en sonunda `save` ile hazırladığınız yemeği (belgeyi) sunuma hazır hale getirirsiniz.





BURADA KALDIM

___

PyMuPDF kütüphanesinde `get_text` metodu kullanılırken "**`blocks`**" ve "**`dict`**" parametreleri, belgeden elde edilecek verinin **ayrıntı düzeyini ve veri yapısını** belirleyen iki temel seçenektir.

İki parametre arasındaki temel farklar şunlardır:

1. Veri Yapısı ve İçerik Kapsamı

• **"`blocks`" Parametresi:** Çıktı olarak <u>bir liste döndürür</u>. Bu listedeki her bir öğe bir "blok"tur ve bloğun **konumunu, metin içeriğini, blok numarasını ve blok tipini** içerir.

• **"`dict`" Parametresi:** Çok katmanlı <u>bir Python sözlüğü (dictionary) yapısı döndürür</u>. "blocks" seçeneğinden farklı olarak, "dict" parametresi çıktıda **görüntü bloklarını (image blocks) da içerir**. Bu yapıda metin blokları "0", görüntü blokları ise "1" tip koduyla ayırt edilir.

2. Detay Seviyesi (Meta Veriler)

"`dict`" parametresi, "`blocks`" parametresinin sunmadığı çok daha derinlemesine teknik detaylar sağlar:

• **Hiyerarşik Yapı:** "`dict`" çıktısında her blok, satırları ifade eden `lines` anahtarına; her satır ise `spans` (aralıklar) anahtarına bölünür.

• **Yazım Bilgileri:** `lines` anahtarı altında metnin **yazım yönü** ve yazım modunun (yatay veya dikey) bilgisi yer alır.

• **Stil Detayları:** `spans` yapısı içerisinde metnin sadece içeriği değil; **yazı tipi (font) adı, yazı tipi özellikleri, boyutu ve rengi** gibi görsel detaylar da bulunur. "`blocks`" parametresi bu tarz biçimlendirme bilgilerini sağlamaz.

3. Ortak Özellikler

Her iki parametre ile çalışırken, blokların belgedeki doğal okuma sırasına göre dizilmesini sağlamak için `sort=True` parametresi eklenebilir. Ayrıca her iki yöntem de `clip` parametresi kullanılarak sayfanın sadece belirli bir dikdörtgen alanı (rect) üzerinde çalıştırılabilir.

**Özet Analoji:** Bir binayı incelediğinizi düşünün; **"blocks"** parametresi size sadece odaların isimlerini ve nerede olduklarını söylerken, **"dict"** parametresi odadaki mobilyaların renginden, duvar kağıdının dokusuna ve odada asılı olan tablolara (görsellere) kadar her türlü detayı rapor eder.

____

PyMuPDF kütüphanesinde, bir PDF sayfasının tamamı yerine sadece belirli bir bölgesindeki metinleri ayıklamak için `get_text()` metodu içerisinde **clip** parametresi kullanılır.

Bu işlemin temel çalışma prensibi şu şekildedir:

• **Dikdörtgen Alan Tanımlama:** Metin çıkarımı yapılacak alanı sınırlandırmak için öncelikle bir **rect** **nesnesi** oluşturulur. Bu nesne, çıkarım yapılacak alanın koordinatlarını (x0, y0, x1, y1) belirler.

• **Koordinatların Tespiti:** Bu koordinatlar manuel olarak girilebileceği gibi, `search_for()` metodu kullanılarak belirli anahtar kelimelerin sayfadaki konumları üzerinden de dinamik olarak elde edilebilir.

• **Sınırlandırılmış Çıkarım:** `get_text(clip=rect_nesnesi)` komutu kullanıldığında, metin ayıklama işlemi yalnızca tanımlanan bu dikdörtgenin içinde kalan içerikle sınırlandırılır.

**Analoji:** Bu parametreyi kullanmak, bir gazetenin tamamını okumak yerine, sayfanın üzerine **sadece tek bir haberi açıkta bırakan bir çerçeve** yerleştirip yalnızca o çerçevenin içinde kalan kelimeleri okumaya benzer.

____

PyMuPDF kütüphanesinde `get_text` metodu kullanılırken metinlerin belgedeki görsel akışa uygun şekilde ayıklanmasını sağlamak için **`sort`** **parametresi kullanılır.**

Kaynaklara göre doğal okuma sırasını sağlamanın detayları şunlardır:

• **`sort=True`** **Parametresi:** Blokların veya metin öğelerinin belgedeki doğal okuma düzenini takip etmesini garanti etmek için bu parametre **`True`** olarak ayarlanmalıdır.

• **Varsayılan Durum:** Varsayılan ayarlarda bloklar en düşük numaradan en yüksek numaraya göre sıralanır. Ancak bu sayısal sıralama, metnin belgede göründüğü gerçek okuma sırasından farklılık gösterebilir.

• **Farklı Çıktı Formatlarıyla Kullanım:** Bu parametre hem metin bloklarını listeleyen **`blocks`** formatında hem de daha detaylı teknik veriler sunan **`dict`** (sözlük) formatında kullanılabilir. Her iki durumda da `sort=True` ayarı, öğelerin mantıksal bir sıra ile sunulmasını sağlar.

Özetle, karmaşık sayfa yapılarında metnin anlamlı bir bütünlükle okunabilmesi için komutun `page.get_text("blocks", sort=True)` veya `page.get_text("dict", sort=True)` şeklinde kullanılması gerekmektedir.

____

PDF sayfalarındaki tabloları bulmak ve bu tablolarla çalışmak için temel olarak **`find_tables()`** metodu kullanılır.

Bu işlemle ilgili kaynaklarda belirtilen detaylar şunlardır:

• **Tablo Tespiti:** Bir sayfa nesnesi üzerinden `find_tables()` metodu çağrıldığında, o sayfadaki tüm tabloları içeren **yinelenebilir (iterable)** bir yapı elde edilir.

• **Veri Ayıklama:** Tespit edilen bir tablodaki verileri dışarı aktarmak için **extract()** metodu kullanılır; bu metot verileri satır ve sütunlardan oluşan bir **Python listesi** şeklinde döndürür.

• **Pandas Entegrasyonu:** Ayıklanan tablo verilerini doğrudan analiz etmek amacıyla, verileri bir **pandas DataFrame** yapısına dönüştürmek için **`to_pandas()`** metodu kullanılabilir.

• **Tablo Oluşturma:** Mevcut bir tabloyu bulmanın aksine, bir PDF'e yeni bir tablo eklemek isterseniz, HTML ve CSS desteği sunan **`insert_htmlbox()`** metodu en pratik yoldur.

**Analoji:** `find_tables()` metodunu kullanmak, karmaşık bir arkeolojik kazı alanında **metal detektörü gezdirmeye** benzer; detektör size toprağın altındaki yapıların (tabloların) yerini tam olarak gösterir, `extract()` komutu ise bu yapıları gün yüzüne çıkarıp bir sergi listesine (Python listesi) dönüştürmenizi sağlar.

____

PyMuPDF kütüphanesini kullanarak bir sayfada kaç adet tablo olduğunu öğrenmek için **find_tables()** metodunu kullanmanız gerekir.

Bu işlemi gerçekleştirmenin adımları şunlardır:

1. **Tabloları Tespit Etme:** İlgili sayfa nesnesi üzerinde `find_tables()` metodunu çağırdığınızda, bu metod sayfadaki tabloları analiz eder ve bir tablo arama nesnesi döndürür.

2. **Liste Uzunluğunu Kontrol Etme:** Bu metodun döndürdüğü nesne içindeki **tables** özelliği, sayfada bulunan tüm tabloları içeren yinelenebilir (iterable) bir yapıdır. Python'daki standart `len()` fonksiyonunu bu yapı üzerinde kullanarak sayfadaki toplam tablo sayısına ulaşabilirsiniz.

**Örnek Mantık:** `tabs = page.find_tables()` komutunu çalıştırdıktan sonra, `len(tabs.tables)` ifadesi size sayfada kaç adet tablo bulunduğunun sayısal değerini verecektir.

**Analoji:** Bu işlem, bir odadaki eşyaları saymaya benzer; `find_tables()` ile odaya (sayfaya) hızlıca göz gezdirir, `len(tabs.tables)` ile de gördüğünüz her bir masayı (tabloyu) parmağınızla sayarak toplam adedi belirlersiniz.

____

Bir PDF sayfasındaki görsel bloklarını ayırt etmek için en etkili yöntem, `get_text()` metodunu **"dict"** parametresi ile birlikte kullanmaktır.

Bu yöntemle görsel blokları şu şekilde ayırt edilir:

• **Blok Tipi Kontrolü:** "`dict`" parametresi kullanıldığında, **metin blokları**nın yanı sıra **görsel blokları** da çıktıya dahil edilir. Her bir blok içerisinde yer alan **"type"** (tip) değeri, bloğun içeriğini tanımlar.

• **Ayırt Edici Değerler:**

    ◦ Eğer bir bloğun tipi **1** (`type: 1`) ise, bu bir **görsel bloğudur**.

    ◦ Eğer bir bloğun tipi **0** (`type: 0`) ise, bu bir **metin bloğudur**.

• **Veri Yapısı:** Görsel blokları, metin bloklarından farklı olarak metin içeriği yerine görselle ilgili teknik veriler sunar. Bu ayrımı programatik olarak yapmak için bir `if` ifadesi kullanılarak sadece belirli bir tipe sahip bloklar filtrelenebilir.

Ayrıca, blokların sayfadaki konumuna göre anlamlı bir sırada gelmesini sağlamak için bu işleme **sort=True** parametresi de eklenebilir.

**Analoji:** Bu ayrımı yapmak, bir kargo paketinin üzerindeki **barkodu okumaya** benzer. Paketlerin dış görünüşü birbirine benzese de (sayfadaki koordinatları olan bloklar), barkodu (tip değerini) okuduğunuzda içeriğin kırılacak bir eşya mı (görsel) yoksa sadece kağıt evrak mı (metin) olduğunu anında anlarsınız.

____

PyMuPDF ile `get_text("dict")` komutunu kullandığınızda, çıktı olarak çok katmanlı bir Python sözlüğü (dictionary) elde edersiniz. Bu sözlük yapısının içindeki her bir içerik bloğu, içeriğin ne olduğunu belirten bir **"`type`" (tip)** anahtarına sahiptir.

Programatik ayrımı sağlayan `if` ifadesinin çalışma mantığı şu detaylara dayanır:

• **Tip Değerleri:** Kaynaklara göre, bir bloğun tipi **0** ise bu bir **metin bloğudur**; eğer tipi **1** ise bu bir **görsel (resim) bloğudur**.

• **Filtreleme Süreci:** Kod içerisinde bir döngü (for loop) kurularak sayfadaki tüm bloklar üzerinden geçilir. Bu döngü sırasında bir `if` koşulu eklenerek, sadece `"type" == 0` olan blokların içeriğinin (metinlerin) alınması sağlanır.

• **Veri Yönetimi:** Bu yöntem sayesinde, görsel bloklarının getirdiği karmaşık veriler (boyutlar, binary içerik vb.) ayıklanarak sadece metin verisine odaklanılabilir. Ayrıca bu işlem sırasında `sort=True` parametresi de kullanılırsa, filtrelenen metin blokları belgedeki doğal okuma sırasına göre dizilmiş olur.

**Özetle:** Bir liste içerisindeki her bir öğenin "etiketine" bakarak, sadece "metin" etiketi taşıyanları seçip diğerlerini (görselleri) görmezden gelme işlemidir.

**Analoji:** Bu durumu, içinde hem fotoğraflar hem de mektuplar bulunan bir kutuyu boşaltmaya benzetebiliriz. Elinize aldığınız her nesneyi (bloğu) kontrol edersiniz; **"Eğer (if) bu nesne bir mektupsa (tip 0), onu oku; değilse kenara koy"** dersiniz. Böylece kutunun içindeki fotoğraflarla (tip 1) vakit kaybetmeden sadece yazılı metinlere odaklanmış olursunuz.
