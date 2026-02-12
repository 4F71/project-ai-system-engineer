# Linear Algebra — Norms (L1 vs L2)

## L1 Norm

Bir vektördeki bileşenlerin mutlak değerlerinin toplamıdır.

Formül:

||v||₁ = |x₁| + |x₂| + ... + |xₙ|

Burada |x| mutlak değeri temsil eder (negatif ise pozitif yapılır).

- Kare alınmaz.
- Karekök alınmaz.
- Geometrik olarak Manhattan (grid) mesafesidir.

---

## L2 Norm

Pisagor’un genelleştirilmiş halidir.

a² + b² = c² bağıntısının n-boyutlu uzaya genişletilmesidir.

Formül:

||v||₂ = √(x₁² + x₂² + ... + xₙ²)

- Geometrik olarak düz çizgi (Euclidean) mesafesidir.

---

## Kök Davranışları

- 0 < x < 1 ise:
  - x² < x
  - √x > x  
  (Kare almak küçültür, kök almak büyütür.)

- x > 1 ise:
  - x² > x
  - √x < x  
  (Kare almak büyütür, kök almak küçültür.)

---

## ML Bağlantısı

- L2 norm, cosine similarity hesaplamasında kullanılır.
- L1 norm, sparsity ve L1 regularization ile ilişkilidir.
- ||v||₂ = 1 olan vektöre birim vektör denir ve normalizasyon için temel kavramdır.
