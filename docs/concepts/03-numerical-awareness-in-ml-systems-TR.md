# ML Sistemlerinde Sayısal Farkındalık (Numerical Awareness)

## Bu kavram nedir?
Sayısal farkındalık, ML sistem kararlarını (durma, kıyas, eşik, kontrol) floating point gerçekliğine göre tasarlamaktır. Birçok üretim problemi “matematik yanlış” olduğu için değil, kırılgan karşılaştırmalar ve ölçek-duyarsız eşikler yüzünden çıkar.

## Temel ilke
**Hata büyüklüğü tek başına anlamlı değildir. Ne ile kıyasladığın önemlidir.**

## ML’de sayısal olarak nerelerde patlar?
Karar sınırları genelde “küçük fark” üzerinden kuruludur:
- Yakınsaklık kontrolü (loss iyileşmesi)
- Early stopping (val loss kıyasları)
- Gradient check (analitik vs sayısal gradient)
- Norm eşikleri (grad norm, param norm, update norm)

## Eşitlik tuzağı
Şunlardan kaçın:
- `loss_curr == loss_prev`
- `grad_norm == 0`

Çünkü float değerler yaklaşık temsil edilir; pratikte “aynı” olan iki değer bile `==` ile eşit çıkmayabilir.

Bunun yerine:
- `np.isclose(a, b, atol=..., rtol=...)`
- ölçek-duyarlı eşitsizlikler (`metric < threshold`) kullan.

## atol vs rtol (sezgi)
- **atol (mutlak tolerans):** “Kaç birim farka izin veriyorum?”
- **rtol (bağıl tolerans):** “Değerin büyüklüğüne göre yüzde kaç farka izin veriyorum?”

NumPy kuralı:
`|a - b| <= atol + rtol * |b|`

Pratik rehber:
- sıfıra yakın / küçük sayılar → atol kritik
- büyük ölçekli değerler → rtol kritik
- birçok ML kararı → ikisini birlikte kullan

## Ölçeğe göre tolerans (scale-relative)
Aynı mutlak delta farklı ölçeklerde bambaşka anlam taşır:
- loss ~ 1e6, delta = 0.1 → bağıl olarak çok küçük
- loss ~ 1e-3, delta = 0.1 → bağıl olarak devasa

Ölçek-duyarlı sinyal örneği:
- `delta / loss_prev < rtol`

## Norm tabanlı yakınsaklık (sistem mühendisi bakışı)
Sabit norm eşiği kırılgandır:
- `grad_norm < 1e-8` (model ölçeği/parametreleme değişince anlamsızlaşabilir)

Daha sağlam yaklaşım:
- `grad_norm / param_norm < rtol`

Bu, karar sınırını parametre ölçeğine bağlar ve stabiliteyi artırır.

## Bu repo’daki kanıtlar
- Lab notebook: `scripts/math/numerical_awareness_convergence_lab.ipynb`
- Proof: `proofs/02-math/2026-02-numerical-awareness-convergence-proof.md`
- Assets: `proofs/02-math/assets/numerical-awareness/`
- Roadmap: `roadmap\MASTER-ROADMAP.md`