# Numerical Foundations — Karekök Hesaplama

## 1. Tanım

Bir sayının karekökü, karesi o sayıyı veren değerdir.

a² = x  
√x = a

---

## 2. Tam Kareleri Tanıma

Karekök hesaplamada ilk adım, tam kareleri bilmektir.

1² = 1  
2² = 4  
3² = 9  
4² = 16  
5² = 25  
6² = 36  
7² = 49  
8² = 64  
9² = 81  
10² = 100  
...  
19² = 361  
20² = 400  

Örnekler:

√361 = 19  
√324 = 18  
√9216 = 96  

---

### Tam Kareyi Hızlı Tespit Etme (Örnek: √361)

361 sayısı 1 ile biter. 1 ile biten kareler:

1² = 1  
9² = 81  

Son iki basamak çıkarıldığında geriye 3 kalır.

3’ü geçmeyen en büyük tam kare 1²’dir.

Bu nedenle ilk basamak 1 ile başlar.

Olası sonuçlar: 11 veya 19

Kontrol:

19² = 361  

Dolayısıyla √361 = 19

---

## 3. Ondalıklı Sayılarda Karekök

Temel kural:

√(a / b) = √a / √b

Yani karekök, kesrin hem payına hem paydasına ayrı ayrı uygulanır.

---

### Örnekler

0.25 = 25 / 100  
√0.25 = √25 / √100 = 5 / 10 = 0.5  

0.0004 = 4 / 10 000  
√0.0004 = √4 / √10 000 = 2 / 100 = 0.02  

1.21 = 121 / 100  
√1.21 = √121 / √100 = 11 / 10 = 1.1  

---

## 4. 10’un Kuvvetleri ve Kök

10² = 100  
10⁴ = 10 000  

Karekök alınca üs yarıya iner:

√(10⁴) = 10²  

Bu nedenle ondalıklı sayılarda virgül davranışı kesir mantığı ile anlaşılmalıdır.

---

## 5. Davranış Kuralları

- 0 < x < 1 ise:
  - x² < x
  - √x > x

- x > 1 ise:
  - x² > x
  - √x < x

---

## 6. Sayısal Sezgi

Pozitif sayılarda karekök sıralamayı korur:

a < b ise √a < √b

Bu özellik, yaklaşık hesaplama yaparken referans noktası sağlar.

---

## 7. ML Bağlantısı

Karekök hesaplama, özellikle L2 norm, Euclidean mesafe ve cosine similarity hesaplamalarında doğrudan kullanılır.

Bu nedenle sayısal doğruluk ve kök sezgisi, makine öğrenmesi sistemlerinde önemlidir.
