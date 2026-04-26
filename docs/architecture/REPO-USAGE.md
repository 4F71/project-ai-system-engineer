<!-- File: private/REPO-USAGE.md -->
# REPO-USAGE (PRIVATE)
## “Ne eklersem neyi düzeltmeliyim?” Kullanım Kılavuzu

> Bu doküman **sadece benim için** yazılmıştır.  
> Amaç: Bu repoya yeni bir şey eklerken **neyi nereye koyacağımı**, **hangi standarda göre yazacağımı** ve **eklerken neleri düzeltmem gerektiğini** netleştirmek.  
> Bu repo bir “not deposu” değil; **kanıtlanabilir mühendislik ilerleme sistemi**.

---

## 0) Altın Kural
**README anlatır → Template şekil verir → İçerik kanıtlar.**  
Bu üçü birbirinin yerine geçmez.

---

## 1) Repo Katmanları (Kısa Harita)
- `docs/` → süreç + düşünce + karar + öğrenme (yazılı sistem)
- `projects/` → uçtan uca sistemler (entegre uygulama)
- `proofs/` → doğrulanabilir kanıtlar (odaklı çıktılar)
- `roadmap/` → plan (tek doğrusu `MASTER-ROADMAP.md`)
- `scenarios/` → problem çerçeveleme egzersizleri (kod şart değil)
- `scripts/` → yardımcı araçlar (destek)
- `resources/` → seçilmiş kaynak listeleri (girdi)
- `private/` → iç işleyiş, promptlar, düşünce logları (vitrine çıkmaz)

---

## 2) Dosya Ekleme Karar Ağacı
Yeni bir şey yazacağım. Nereye koyacağım?

### A) “Bu bir haftalık kayıt mı?”
- **Evet** → `docs/journal/YYYY-MM-WeekNN.md`

### B) “Bu bir öğrenme notu / kavram açıklaması mı?”
- **Evet** → `docs/concepts/NN-topic-name.md`

### C) “Bu, iddia ettiğim bir yetkinliğin kanıtı mı?”
- **Evet** → `proofs/<domain>/...`

### D) “Bu, çalışan bir sistem / entegrasyon / capstone mu?”
- **Evet** → `projects/<capstone>/...`

### E) “Bu bir problem senaryosu mu (çerçeveleme + tradeoff)?”
- **Evet** → `scenarios/<level>/scenario-XX-...md`

### F) “Bu bir yardımcı script mi?”
- **Evet** → `scripts/<scope>/...`

### G) “Bu dış kaynak listesi mi?”
- **Evet** → `resources/*.md`

### H) “Bu, tamamen kişisel çalışma düzenim mi?”
- **Evet** → `private/`

---

## 3) Template Kullanım Kuralları
Template’ler **minimal format** sağlar. Rehberlik README’dedir.

Kullanım eşlemesi:
- Journal → `docs/templates/journal-template.md`
- Concept → `docs/templates/concept-template.md`
- Retrospective → `docs/templates/retrospective-template.md`
- Proof → `docs/templates/proof-template.md`
- Scenario → `scenarios/_templates/scenario-template.md`

**Kural:** Template’in içine “nasıl yazılır” eklenmez.  
“Nasıl yazılır” README’de kalır.

---

## 4) İsimlendirme Standardı (Değişmez)
### Journal
- `docs/journal/YYYY-MM-WeekNN.md`
- Örn: `2026-02-Week02.md`

### Retrospective
- `docs/retrospectives/YYYY-MM-retro.md`
- Örn: `2026-02-retro.md`

### Concepts
- `docs/concepts/NN-topic-name.md`
- Örn: `01-linear-algebra-vectors.md`

### Scenarios
- `scenarios/<level>/scenario-XX-short-title.md`
- Örn: `scenario-01-churn-prediction.md`

### ADR (ileride)
- `docs/architecture/adr/YYYY-MM-DD-short-title.md`

---

## 5) “Ne eklersem neyi düzeltmeliyim?” — Zorunlu Kontrol Listeleri

### 5.1 Yeni bir Journal eklersem
**Ekle:**
- `docs/journal/YYYY-MM-WeekNN.md`

**Düzelt / Kontrol et:**
- Journal içinde geçen tüm linkler gerçek mi?
  - `projects/...`
  - `proofs/...`
  - `roadmap/...`
- “Bu hafta çıktı” dediğim şeyin en az biri şu olmalı:
  - bir proof dosyası
  - bir scenario dosyası
  - bir project güncellemesi
  - ya da net bir ADR / runbook

**Kalite eşiği:**
- “Ne yaptım?” → somut
- “Ne öğrendim?” → spesifik
- “Kanıt” → dosya yolu ile

---

### 5.2 Yeni bir Concept eklersem
**Ekle:**
- `docs/concepts/NN-...md`

**Düzelt / Kontrol et:**
- Concept’in sonunda şu bağlantılardan en az biri olmalı:
  - ilgili `proofs/...`
  - ilgili `projects/...`
- Eğer concept bir roadmap maddesini kapatıyorsa:
  - roadmap’te sadece “okudum” diye değil,
  - “kanıtım var” diye işaretlenmeli (kanıt: proof veya proje linki)

**Kalite eşiği:**
- tanım + sezgi + mini örnek + hata noktası + bağlantı

---

### 5.3 Yeni bir Proof eklersem
**Ekle:**
- `proofs/<domain>/...md`

**Düzelt / Kontrol et:**
- Proof bir “iddia” içeriyor mu?
- İddia kanıtlanıyor mu?
  - ölçüm / sonuç / demo / karşılaştırma / çıktı
- Proof dosyasında:
  - varsayımlar
  - sınırlar
  - tekrar üretim yolu (gerekirse script linki)
- Eğer proof bir project’ten türediyse:
  - project README’den bu proof’a link ver (kopyalama yok, link var)

**Kalite eşiği:**
- “Sadece yazı” yetmez → bir kanıt izi olmalı (çıktı, metrik, örnek, karşılaştırma).

---

### 5.4 Yeni bir Project günceller / eklersen
**Ekle:**
- `projects/<capstone>/...`

**Düzelt / Kontrol et:**
- Proje README’si güncel mi?
  - sınırlar
  - input/output
  - değerlendirme
  - ilgili proof’lar
- Proje içinde “artifact” dosyaları varsa (async interview gibi):
  - bunlar proof değil → README’de açıkça etiketle
- Proje büyüdükçe:
  - `docs/architecture` tarafına ADR/C4 eklemek mantıklı mı?

**Kalite eşiği:**
- “Çalışan sistem” anlatısı → net sınırlar + değerlendirme + linkler.

---

### 5.5 Yeni bir Scenario eklersen
**Ekle:**
- `scenarios/<level>/scenario-XX-...md`

**Düzelt / Kontrol et:**
- Senaryoda:
  - hedef
  - varsayımlar
  - kısıtlar
  - ölçüt / başarı tanımı
  - riskler / failure mode
- Eğer senaryo bir proof’a dönüşürse:
  - `proofs/...` içine taşıma değil,
  - proof oluşturup scenario’dan proof’a link koy

**Kalite eşiği:**
- Kod şart değil; **mühendislik düşüncesi** şart.

---

### 5.6 Yeni bir Script eklersen
**Ekle:**
- `scripts/<scope>/...`

**Düzelt / Kontrol et:**
- Script başına kısa header:
  - ne yapar
  - giriş/çıkış
  - varsayım
- Script bir proof/proje için yazıldıysa:
  - ilgili dosyadan script’e link ver

**Kalite eşiği:**
- küçük, odaklı, tekrar kullanılabilir.

---

## 6) Commit Disiplini (Özet)
Bu repo commit’leri **hikâye** anlatır.

**Kural: Bir commit = tek mantıksal adım.**  
Karıştırma örnekleri (yasak):
- README düzeni + yeni proof aynı commit ❌
- Journal + büyük refactor aynı commit ❌

### İdeal commit ayrımları
- “README sistemi” → tek commit
- “WeekNN journal” → tek commit
- “Yeni proof” → tek commit
- “Proje milestone” → tek commit
- “Refactor/cleanup” → tek commit

**Commit mesajları için standart:** `private/prompts/commit-standard.md`

---

## 7) Haftalık Çalışma Rutini (Pratik Sistem)
> Amaç: Roadmap → Output → Proof → Journal döngüsünü kilitlemek

### Her hafta minimum:
1) 1 Journal (`docs/journal/...`)
2) 1 Proof **veya** 1 Scenario
3) Roadmap’te en az 1 madde “kanıt linki” ile güncelle

### Ay sonu:
- 1 Retrospective (`docs/retrospectives/...`)

---

## 8) En Sık Hatalar (Kendime Uyarı)
- “Öğrendim” deyip kanıt linki vermemek
- Proof yerine uzun anlatı yazmak
- Project’i proof gibi anlatmak
- Her şeyi tek commit’e yığmak
- Template’i rehber haline getirmek (yasak)

---

## 9) Hızlı Komutlar (PowerShell)
### Durum kontrol
```powershell
git status
git diff
git diff --cached
