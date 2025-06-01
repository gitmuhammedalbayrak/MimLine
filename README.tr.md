# MimLine

MimLine, "0"ın dizinin başında ve sonunda yer aldığı, "1"in ise merkezde bulunduğu çift kutuplu ve çok boyutlu bir sayı dizisi örneğidir. Bu dizide "1" merkezi bir konumda olup, pozitif komşusu "2", negatif komşusu ise "-2"dir. "-1" sayısı dizide bulunmaz ancak kavramsal olarak dikey bir alt uzayda konumlanır: unutmayın, bu tamamen kavramsaldır.

Negatif uzay, bir sayısal nesnenin özünü veya içsel içeriğini temsil ederken, pozitif uzay kapsamını veya onu çevreleyen unsurları temsil eder. Kapsam ve özde, her katman farklı bir boyutu, her boyut da kendi seviyelerini içerir.

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

- `name`: Örneklemin adını temsil eder.
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

MimLine sınıfının doğru çalışmasını doğrulamak için testler oluşturulmuştur. Aşağıdaki kod örneği, 5000 test çalıştıracak olan MimLineTest sınıfını içerir:

```python
import random

class MimLineTest:
    def __init__(self):
        self.tests = 5000  # Test sayısı

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
