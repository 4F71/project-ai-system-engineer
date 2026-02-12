# Numerical Foundations — Square Root Computation

## 1. Definition

The square root of a number is the value whose square equals that number.

a² = x  
√x = a

---

## 2. Recognizing Perfect Squares

The first step in square root computation is knowing perfect squares.

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

Examples:

√361 = 19  
√324 = 18  
√9216 = 96  

### Fast Perfect Square Detection (Example: √361)

361 ends with the digit 1. Squares ending with 1 are:

1² = 1  
9² = 81  

Removing the last two digits leaves 3.

The largest perfect square less than or equal to 3 is 1².

Therefore, the first digit is 1.

Possible results: 11 or 19.

Check:

19² = 361

Thus, √361 = 19.

---

## 3. Square Roots of Decimal Numbers

Fundamental rule:

√(a / b) = √a / √b

The square root is applied separately to numerator and denominator.

---

### Examples

0.25 = 25 / 100  
√0.25 = √25 / √100 = 5 / 10 = 0.5  

0.0004 = 4 / 10 000  
√0.0004 = √4 / √10 000 = 2 / 100 = 0.02  

1.21 = 121 / 100  
√1.21 = √121 / √100 = 11 / 10 = 1.1  

---

## 4. Powers of 10 and Square Roots

10² = 100  
10⁴ = 10 000  

When taking the square root, the exponent is halved:

√(10⁴) = 10²  

This explains decimal behavior through fraction logic.

---

## 5. Behavior Rules

- If 0 < x < 1:
  - x² < x
  - √x > x

- If x > 1:
  - x² > x
  - √x < x

---

## 6. Numerical Intuition

For positive numbers, square roots preserve ordering:

If a < b, then √a < √b.

This provides a reference point for approximate reasoning.

---

## 7. ML Connection

Square root computation is directly used in L2 norm, Euclidean distance, and cosine similarity calculations.

Therefore, numerical precision and root intuition are important in machine learning systems.
