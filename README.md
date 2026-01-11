# 🔐 MyCryptoRNG – Linear Congruential Random Number Generator

Bu proje, kriptografi dersi için hazırlanmış **basit ve analiz edilebilir** bir rastgele sayı üreteci (RNG) uygulamasıdır.  
Gerçek kriptografik sistemlerde kullanılmak üzere tasarlanmamıştır; eğitim ve çözümleme (attack) pratikleri için uygundur.

---

## 📌 Projenin Amacı

- Lineer Kongruans Üreteci (LCG) mantığını öğrenmek
- Kendi RNG algoritmamızı tasarlamak ve uygulamak
- Sınavda başkalarının RNG çıktılarından algoritma parametrelerini çözebilmek
- Kriptografik güvenlik ile pseudo-random kavramlarını ayırmayı öğrenmek

---

## 📌 Kullanılan Algoritma: LCG

Kullandığım rastgele sayı üretme algoritması **Linear Congruential Generator**'dır.  
Formülü:

\[
X_{n+1} = (a \cdot X_n + c) \mod m
\]

Bu formülde:

- \( X_n \) : n. sıradaki sayı  
- \( a \) : çarpan (multiplier)  
- \( c \) : eklenen sabit değer (increment)  
- \( m \) : mod değeri  
- \( X_0 \) : başlangıç değeri (seed)

---

## 📌 Parametrelerim

Projede kullanılan parametreler:

| Parametre | Değer |
|----------|-------|
| m        | 2147483647 (2³¹ − 1, büyük bir asal) |
| a        | 1103515245 |
| c        | 12345 |
| seed     | Kullanıcı tarafından belirlenir |

---

## 📌 Kod Yapısı

`rng.py` içinde RNG sınıfı bulunur:

```python
class MyCryptoRNG:
    def __init__(self, seed: int):
        self.m = 2147483647
        self.a = 1103515245
        self.c = 12345
        self.state = seed

    def next_int(self) -> int:
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def next_float(self) -> float:
        return self.next_int() / self.m
