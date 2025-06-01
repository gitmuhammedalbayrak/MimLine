# MimLine

MimLine, "0"ın dizinin başında ve sonunda yer aldığı, "1"in ise merkezde bulunduğu çift kutuplu ve çok boyutlu bir sayı dizisi örneğidir. Bu dizide "1" merkezi bir konumda olup, pozitif komşusu "2", negatif komşusu ise "-2"dir. "-1" sayısı dizide mevcut değildir ancak kavramsal olarak dikey bir alt uzayda konumlandırılmıştır: unutmayın, bu tamamen kavramsal bir durumdur.

Negatif uzay, bir sayısal nesnenin özünü veya içsel içeriğini temsil ederken, pozitif uzay onun kapsamını veya kuşatan unsurlarını temsil eder. Kapsam ve özde, her katman farklı bir boyutu, her boyut da kendi seviyelerini içerir.

Örneğin:
Bir elma = "1"
Elmanın birinci derece özü (her zaman nesnenin tüm içeriğinin toplamını temsil eder) = -2
Elmanın ikinci derece özü (örneğin, fizik bağlamındaki özü) = -3

Boyut örneği için, -3'ü ele alırsak (yine elmayı kullanarak):
[-3[0,1]] = Burada, fiziksel olarak iki bölümde analiz edildiğini görüyoruz. Bu iki sayı için şu örnekleri verebiliriz:
0 = kütlesi
1 = hızı

Pozitif yönü daha sonra açıklanacaktır.

## Özellikler

- `name`: Örnek adını temsil eder.
- `centerArray`: Merkezi dizi olarak adlandırılan bir diziyi tutar.
- `dimensional_centerArray`: Boyutsal bir merkezi diziyi tutar.

## Kurulum

Ek bir kurulum gerekmez. Kodu doğrudan kullanabilirsiniz.

## Kullanım

Aşağıdaki örnek, MimLine sınıfının nasıl kullanılacağını gösterir:

```python
# Örnek kullanım
line = MimLine("Örnek", inEnd=2, outEnd=1, inDimension=3, outDimension=2)
line.display()
```

## Testler

MimLine sınıfının doğru çalıştığını doğrulamak için testler oluşturulmuştur. Aşağıdaki kod örneği, 5000 test çalıştıracak olan MimLineTest sınıfını içerir:

```python
import random

class MimLineTest:
    def __init__(self):
        self.tests = 5000

    def run_tests(self):
        for i in range(self.tests):
            print(f"--- Test {i+1} ---")
            inEnd = random.randint(1, 10)
            outEnd = random.randint(1, 10)
            inDimension = random.randint(1, 10)
            outDimension = random.randint(1, 10)
            line = MimLine(f"Örnek{i+1}", inEnd, outEnd, inDimension, outDimension)
            self.test_mimline(line)
            print()

    def test_mimline(self, line):
        # Başında ve sonunda sıfır olup olmadığını kontrol et
        if line.centerArray[0] == 0 and line.centerArray[-1] == 0:
            print("Başında ve sonunda sıfır var.")
        else:
            raise ValueError("Başında veya sonunda sıfır yok.")

        # Listede 1 değerinin olup olmadığını kontrol et
        if 1 in line.dimensional_centerArray:
            print("Listede 1 değeri mevcut.")
        else:
            raise ValueError("Listede 1 değeri yok veya değiştirilmiş.")
```

### MimLineTest Sınıfı ile Testleri Çalıştırma
```python
test = MimLineTest()
test.run_tests()
```

Testlerden kaynaklanan hatalar ValueError yükseltilerek gösterilecektir. Testler başarıyla geçerse herhangi bir çıktı üretilmeyecektir.

## Lisans

Bu proje T1 Lisansı altında lisanslanmıştır. Lisansı edinmek veya daha fazla bilgi için lütfen doğrudan benimle iletişime geçin. Eğer ulaşılamazsam, herhangi bir lisans verilmediği kabul edilmelidir.

## MimLine'ın Felsefi Arka Planı, Ufku ve Potansiyeli

MimLine'ın kavramsal temellerini anlamak, onun derin felsefi ve matematiksel fikirlerle olan bağlantılarını ortaya koyar ve sayı, boyutsallık ve analize benzersiz bir bakış açısı sunar. Bu bölüm, bu bağlantıları ve MimLine'ın açtığı potansiyel ufukları incelemektedir.

### İki Kutupluluk, Diyalektik ve Karşıtların Dansı

MimLine'ın, dizinin hem başında hem de sonunda "0" bulunan ve merkezde "1" yer alan, pozitif ("kapsam") ve negatif ("öz") komşularla (örneğin, 1 için +2 ve -2) çevrili yapısı, felsefi **iki kutupluluk** ve **diyalektik** kavramlarını çağrıştırır.

*   **Hegelci Diyalektik:** Alman filozof G.W.F. Hegel, gerçekliğin ve düşüncenin tez, antitez ve sentez süreciyle geliştiğini tanımlamıştır. MimLine'ın merkezi "1"i (bir "elma" gibi bir varlık) bir tez olarak görülebilir. Negatif "öz" değerleri (-2, -3, vb.) ve pozitif "kapsam" değerleri (+2, +3, vb.), "1"i tanımlayan ve ifade eden antitetik yönler olarak yorumlanabilir. Bu iki kutuplu yönleriyle anlaşılan varlığın kendisi, daha zengin bir sentez haline gelir. Hegel'in *Aufheben* (aşmak, koruyarak üstesinden gelmek) kavramı burada önemlidir: "1", basitliğinde "aşılır" ancak temel içeriği ve kapsayıcı kapsamı aracılığıyla "korunur" ve daha derinden anlaşılır.
*   **Karşıtların Birliği:** Heraklitos gibi filozoflar, gerçekliğin temeli olarak karşıtların uyumunu ve gerilimini vurgulamışlardır. MimLine'ın pozitif/negatif kutupları ve "0"ın hem başlangıç hem de bitiş noktası olarak yerleştirilmesi, bu dinamik etkileşimin bir temsili olarak görülebilir.

### Çok Boyutluluk, Öz ve Analiz Düzeyleri

MimLine, "her katmanın farklı bir boyutu temsil ettiği, her boyutun kendi seviyelerini içerdiği" bir "boyutsallık" sunar. Bu, birkaç ontolojik kavramla örtüşmektedir:

*   **Hiyerarşik Ontoloji ve Mereoloji:** Varlık araştırması olan ontoloji, genellikle gerçekliğin nasıl yapılandığını inceler.
    *   Parçalar ve bütünler teorisi olan **Mereoloji**, doğrudan uygulanabilir. MimLine'ın "birinci derece özü (-2)", "nesnenin tüm içeriğinin toplamı" olarak tanımlanır ki bu açık bir mereolojik iddiadır. Sonraki "öz dereceleri" (örneğin, "fizik bağlamındaki özü" için -3), daha ileri, belki de daha spesifik, parça-bütün analizlerini veya soyutlama katmanlarını temsil eder.
    *   **Hiyerarşik Ontolojiler** (örneğin, gerçekliği cansız, biyolojik, psikolojik ve ruhsal seviyelere ayıran Nicolai Hartmann), gerçekliğin farklı katmanlardan oluştuğunu, üst seviyelerin alt seviyelere bağlı olduğunu öne sürer. MimLine'ın boyutlar içindeki "katmanları" ve "seviyeleri", merkezi sayısal nesnesinin böyle bir katmanlı analizini önerir. `[-3[0,1]]` örneği (-3'ün bir elmanın fiziksel bir boyutu olduğu ve 0 ile 1'in onun kütlesi ve hızı olduğu), özün belirli bir boyutu içinde hiyerarşik bir dökümü göstermektedir.
*   **Töz-Nitelik Ontolojisi:** Metafiziğin geleneksel bir görüşü, gerçekliği bağımsız olarak var olan tözlerden (şeyler) ve bu tözlerin niteliklerinden (özellikler veya vasıflar) oluşmuş olarak görür. MimLine'da, merkezi "1" ("elma"), töz olarak görülebilirken, "öz" ve "kapsam" boyutlarındaki değerler ve bunların içindeki seviyeler ("kütle" veya "hız" gibi), çeşitli kavramsal derinliklerde analiz edilen nitelikleri veya özellikleri olarak işlev görür.

### "0" ve "1"in Benzersiz Rolleri

*   **Sıfır (0) - Boşluk ve Ufuk:** MimLine'da "0", benzersiz bir şekilde "dizinin başında ve sonunda" konumlandırılmıştır.
    *   Tarihsel ve felsefi olarak sıfır (Sanskritçe *śūnya* - "boşluk", "ıssızlık"), sadece bir niceliği değil, aynı zamanda hiçlik, potansiyellik veya bir sınır kavramlarını da temsil etmiştir. MimLine'daki ikili yerleşimi, bir varlığın ("1") ortaya çıktığı kökeni ve geri dönebileceği veya sınırlandığı ufku veya farklılaşmamış durumu sembolize edebilir. Toplamsal etkisiz eleman (`x + 0 = x`) olarak, bir tarafsızlık noktası görevi görür.
    *   Antik Yunan felsefesinin "yokluk" ile ilgili zorluğu, sıfırın kavramsal derinliğini vurgular. MimLine, "0"ı temel bir yapısal unsur olarak benimser.
*   **Bir (1) - Birlik ve Monad:** "1", MimLine'da "merkezi olarak konumlandırılmıştır" ve analiz edilen belirli varlığı (örneğin, "bir elma") temsil eder.
    *   Matematiksel olarak "1", çarpımsal etkisiz elemandır (`1 * n = n`) ve diğerlerinin üretildiği birim olan ilk pozitif tam sayıdır.
    *   Felsefi olarak "1" (veya "Bir", Pisagorcu ve Yeni Platoncu düşüncede "Monad", örn. Plotinus) genellikle birliği, tüm varlığın kökenini veya kaynağını ya da temel bölünemez birimi sembolize eder. MimLine'ın "1"i, karmaşık "özü" ve "kapsamı" daha sonra dizi aracılığıyla detaylandırılan bu tanımlanmış, belirli bir varlıktır, odak noktasıdır.

### Potansiyel ve Ufuk

MimLine'ın yapısı, kavramsal olmakla birlikte, potansiyel uygulamaları olan yeni bir çerçeve sunar:

*   **Karmaşık Sistemlerin Modellenmesi:** İki kutuplu ve çok boyutlu doğası, varlıkların iç bileşenler (öz), dış ilişkiler (kapsam) ve çeşitli analitik detay seviyeleri ile tanımlandığı sistemleri modellemek için uyarlanabilir.
*   **Kavramsal Analiz:** Çerçeve, karmaşık kavramları kurucu parçalarına ve bağlamsal ilişkilerine ayırmak için bir araç olarak kullanılabilir, bilgi bilimindeki biçimsel ontolojik analize benzer şekilde.
*   **Alternatif Hesaplama Modelleri:** README kavramsal doğasına odaklanırken, yapılandırılmış diziler ve boyutsal parametreler, bu iki kutuplu ve çok seviyeli özellikleri doğal olarak yakalayan verileri temsil etmenin ve işlemenin yeni yollarına yol açabilecek hesaplama uygulaması olasılıklarına işaret etmektedir.
*   **Felsefi Keşif:** MimLine, nesnelerin doğası, özellikleri, içsel karmaşıklıkları ve daha geniş bağlamlarla ilişkileri hakkındaki eski felsefi soruları keşfetmek için yeni bir "dil" veya model olarak hizmet edebilir.

Bu matematiksel ve felsefi fikirleri bütünleştirerek MimLine, tanımlanmış varlıkların çok yönlü doğasını temsil etmenin ve anlamanın daha zengin, daha incelikli bir yolunu sunmayı amaçlamaktadır.
