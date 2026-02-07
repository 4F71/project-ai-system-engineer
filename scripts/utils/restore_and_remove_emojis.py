import re

# Original content with proper formatting - restore from backup first
original_content = """#  ML Engineer Roadmap Projesi - Detaylı Geliştirme Planı

##  Genel Bilgiler

**Proje Adı:** Senior ML Engineer Roadmap  
**Hedef:** Açık kaynak, senaryo bazlı, production-focused ML roadmap  
**Tahmini Süre:** 3-4 hafta  
**Repo Lokasyonu:** `C:\\Users\\yedis\\Desktop\\yehu\\Github Repo\\ml-engineer-roadmap`

---

## Aşama 1: Araştırma & Planlama (3-4 gün)

### 1.1 Industry Araştırması - Senior ML Engineer Requirements

**Amaç:** Gerçek dünyada ne aranıyor, hangi beceriler critical?

**Yapılacaklar:**
- [ ] LinkedIn'de "Senior ML Engineer" araması (50+ ilan)
  - Google, Meta, Amazon, Microsoft, Anthropic, OpenAI
  - Türkiye'deki tech companies (Getir, Trendyol, Hepsiburada)
  - Startup'lar vs corporate farkları
  
- [ ] Job posting'lerden veri toplama:
  - Required skills (must-have)
  - Preferred skills (nice-to-have)
  - Experience years
  - Tech stack (frameworks, tools, cloud providers)
  - Soft skills
  
- [ ] Kategorilere ayırma:
  - **Core ML:** (örn: model training, evaluation, feature engineering)
  - **Deep Learning:** (örn: PyTorch, Transformers, fine-tuning)
  - **MLOps:** (örn: Docker, Kubernetes, CI/CD, monitoring)
  - **Programming:** (örn: Python, SQL, distributed computing)
  - **Cloud & Infra:** (örn: AWS/GCP/Azure, S3, databases)
  - **Soft Skills:** (örn: communication, mentoring, system design)

**Çıktı Formatı:**

# Industry Requirements Analysis

## Top 30 Technical Skills (sıklık sırasına göre)
1. Python (appeared in 98% of postings)
2. PyTorch/TensorFlow (85%)
3. ...

## Tech Stack Breakdown
### Frameworks
- PyTorch: 65%
- TensorFlow: 45%
- ...

### Cloud Providers
- AWS: 70%
- GCP: 40%
- ...

## Experience Level Mapping
- Junior (0-2 years): X becerilere sahip
- Mid (2-4 years): Y becerilere sahip
- Senior (4+ years): Z becerilere sahip

## Salary Insights (opsiyonel)
- US: $150k-$250k
- EU: €80k-€120k
- Turkey: ₺...
```

**Tamamlanma Kriteri:**
- [ ] En az 50 job posting analiz edildi
- [ ] Top 30 skill listesi çıkarıldı
- [ ] Tech stack breakdown yapıldı
- [ ] `research/industry-requirements.md` oluşturuldu

**Tahmini Süre:** 1-2 gün

---

### 1.2 Existing Roadmaps Analizi

**Amaç:** Tekrardan kaçınalım, farkımızı ortaya koyalım

**Yapılacaklar:**
- [ ] GitHub'da ML roadmap araştırması:
```
  Aranacak: "machine learning roadmap", "ml engineer roadmap", 
             "mlops roadmap", "ai engineer roadmap"
  Sıralama: Stars (en popülerler)
```
  
- [ ] Top 5-7 roadmap'i incele:
  - Repo URL'leri
  - Star/fork sayıları
  - İçerik formatı (text, diagram, interactive?)
  - Güçlü yanları
  - Zayıf yanları
  - Ne eksik?

**Analiz Soruları:**
- Hangileri sadece teori listelemiş?
- Hangileri proje bazlı?
- Hangileri production/MLOps'u iyi kapsamış?
- Türkçe kaynak var mı?
- Beginner vs Senior ayrımı var mı?
- Güncel mi? (2023-2024 tools'ları içeriyor mu?)

**Çıktı Formatı:**

# Competitor Analysis

## Analyzed Roadmaps

### 1. [Roadmap Name](URL) 45k
**Güçlü yanları:**
- Görsel olarak çok iyi
- ...

**Zayıf yanları:**
- Sadece konu listesi, nasıl öğrenileceği yok
- ...

**Bizde olacak ama onda yok:**
- Senaryo bazlı öğrenme
- ...

---

### 2. [Next Roadmap]...

## Fark Yaratan Özelliklerimiz
1. Senaryo bazlı (gerçek dünya problemleri)
2. Actionable (checkbox + süre + kaynak)
3. Production-focused (sadece model değil deployment)
4. Turkish NLP examples
5. ...
```

**Tamamlanma Kriteri:**
- [ ] 5-7 roadmap detaylı analiz edildi
- [ ] Competitive advantages net belirlendi
- [ ] `research/competitor-analysis.md` oluşturuldu

**Tahmini Süre:** 0.5-1 gün

---

### 1.3 Öğrenme Kaynakları Küratörlüğü

**Amaç:** Her beceri için en iyi ücretsiz/uygun fiyatlı kaynakları bul

**Yapılacaklar:**
- [ ] **Kitaplar:**
  - Beginner: Hands-on ML (Géron), Python for Data Analysis
  - Intermediate: Deep Learning Book (Goodfellow)
  - Advanced: Designing ML Systems (Chip Huyen)
  
- [ ] **Kurslar:**
  - Coursera: Andrew Ng ML, Deep Learning Specialization
  - Fast.ai: Practical Deep Learning
  - Ücretsiz kaynaklar öncelikli
  
- [ ] **Papers:**
  - Foundational: Attention Is All You Need, BERT, GPT
  - MLOps: Hidden Technical Debt in ML Systems
  
- [ ] **Blogs/Tutorials:**
  - Distill.pub
  - Jay Alammar
  - Made With ML
  
- [ ] **Practice Platforms:**
  - Kaggle
  - HuggingFace Tutorials
  - Papers With Code

**Çıktı Formatı:**
```markdown
# books.md

## Beginner Level
- [ ] **Hands-on Machine Learning** (Aurélien Géron)
  - Konular: Classical ML, basic deep learning
  - Zorluk: Beginner
  - Süre: 4-6 hafta
  - Link: [O'Reilly]

## Intermediate Level
...

---

# courses.md

## Fundamentals
- [ ] **Machine Learning Specialization** (Andrew Ng)
  - Platform: Coursera
  - Ücretsiz mi: Yes (audit mode)
  - Süre: 3 ay
  - Covers: Supervised/Unsupervised learning, neural networks
```

**Tamamlanma Kriteri:**
- [ ] Her kategori için 3-5 kaynak seçildi
- [ ] Kaynaklar beginner/intermediate/advanced'e ayrıldı
- [ ] `resources/*.md` dosyaları oluşturuldu

**Tahmini Süre:** 1 gün

---

### 1.4 Skill Matrix Oluşturma

**Amaç:** Her seviye için hangi becerilere sahip olunmalı?

**Yapılacaklar:**
- [ ] Industry research'ten gelen skilleri levellara böl
- [ ] Her skill için:
  - Hangi level'da öğrenilmeli?
  - Önkoşulları neler?
  - Nasıl test edilir? (mini proje)

**Çıktı Formatı:**
```markdown
# Skill Matrix

## Junior ML Engineer (0-2 years)
### Must Have:
- Python fundamentals
- Pandas, NumPy
- Scikit-learn
- Basic model training & evaluation
- Git basics

### Nice to Have:
- Basic SQL
- Jupyter notebooks
- Simple deployment (Streamlit)

## Mid-level ML Engineer (2-4 years)
### Must Have:
- All Junior skills +
- PyTorch/TensorFlow
- Feature engineering at scale
- Model optimization
- Docker
- Basic MLOps

## Senior ML Engineer (4+ years)
### Must Have:
- All Mid-level skills +
- System design for ML
- Production deployment & monitoring
- A/B testing
- Team mentoring
- Multiple domains (NLP/CV/Rec)
```

**Tamamlanma Kriteri:**
- [ ] 3 level için skill breakdown yapıldı
- [ ] `research/skill-matrix.md` oluşturuldu

**Tahmini Süre:** 0.5 gün

---

## Aşama 2: İçerik Taslağı (2-3 gün)

### 2.1 Roadmap Kategorilerini Detaylandır

**Amaç:** Her roadmap dosyası için iskelet oluştur

**Yapılacaklar:**

**Her dosya için template:**
```markdown
# [Category Name]

## Bu Kategoride Neler Var?
Kısa açıklama (2-3 cümle)

## Bu Kategoriyi Tamamladığında:
- Yapabilecekleriniz
- Oluşturabileceğiniz projeler
- Geçebileceğiniz interview türleri

## Alt Başlıklar

### [Subtopic 1]
- [ ] Skill 1 - Beginner - 1-2 hafta
  - Açıklama: ...
  - Kaynak: [Link]
  - Mini proje: ...
  
- [ ] Skill 2 - Intermediate - 2-3 hafta
  - ...

### [Subtopic 2]
...

## Pro Tips
- Sık yapılan hatalar
- Nasıl daha hızlı öğrenilir
- Interview için önemli noktalar

## İleri Seviye (Opsiyonel)
Senior+ için deep dive konular
```

**Her dosya için ana başlıkları belirle:**

**01-foundations.md:**
- Python Programming
- Data Structures & Algorithms
- Git & Version Control
- Linux/Command Line
- SQL Basics

**02-ml-fundamentals.md:**
- Classical ML Algorithms
- Feature Engineering
- Model Evaluation & Selection
- Hyperparameter Tuning
- ML Pipelines

**03-deep-learning.md:**
- Neural Network Fundamentals
- PyTorch/TensorFlow
- CNNs, RNNs, Transformers
- Transfer Learning
- Fine-tuning LLMs

**04-mlops-production.md:**
- Docker & Containerization
- Model Deployment (FastAPI, Flask)
- Cloud Platforms (AWS/GCP/Azure)
- Monitoring & Logging
- CI/CD for ML
- A/B Testing

**05-specialized-domains.md:**
- NLP (Turkish NLP özel vurgu)
- Computer Vision
- Recommender Systems
- Reinforcement Learning (opsiyonel)

**06-soft-skills.md:**
- System Design for ML
- Technical Communication
- Code Review & Best Practices
- Mentoring & Leadership
- Stakeholder Management

**Tamamlanma Kriteri:**
- [ ] 6 dosya için ana başlıklar belirlendi
- [ ] Her başlık için 5-10 skill listelendi
- [ ] Roadmap dosyalarının iskeletleri oluşturuldu

**Tahmini Süre:** 1-2 gün

---

### 2.2 Senaryo Listesi & Mapping

**Amaç:** Hangi senaryolar hangi becerileri öğretiyor?

**Yapılacaklar:**

**Senaryo Brainstorming:**

**Beginner (5 senaryo):**
1. E-ticaret müşteri churn prediction
2. House price prediction API
3. Email spam classifier
4. Product recommendation (basit)
5. Sentiment analysis (İngilizce)

**Intermediate (5 senaryo):**
1. Turkish NER for news articles
2. Multi-class image classifier (custom dataset)
3. Recommendation system with collaborative filtering
4. Time series forecasting (sales/stock)
5. Chatbot with RAG (basit)

**Advanced (5 senaryo):**
1. Production LLM fine-tuning & deployment
2. Distributed training (multi-GPU)
3. Real-time fraud detection system
4. A/B testing framework for models
5. End-to-end ML platform (mini MLOps)

**Her senaryo için mapping:**
```markdown
# Senaryo Mapping

## Beginner-01: E-ticaret Churn Prediction

### Required Skills:
- Python basics
- Pandas, NumPy
- Scikit-learn (Logistic Regression, Random Forest)
- Feature engineering (basic)
- Imbalanced data handling
- Model evaluation (precision, recall, F1)
- FastAPI (basit deployment)
- Git workflow

### Learning Path:
1. Foundations: Python, Pandas (01-foundations.md)
2. ML Fundamentals: Classification, evaluation (02-ml-fundamentals.md)
3. Deployment: FastAPI basics (04-mlops-production.md)

### Estimated Time: 2-3 hafta
### Difficulty: Beginner
```

**Tamamlanma Kriteri:**
- [ ] 15 senaryo fikri oluşturuldu
- [ ] Her senaryo için required skills map edildi
- [ ] `scenarios/scenario-mapping.md` oluşturuldu

**Tahmini Süre:** 1 gün

---

## Aşama 3: İçerik Yazımı (1.5-2 hafta)

### 3.1 Roadmap Dosyaları (öncelik sırasına göre)

**Yazım Sırası & Mantığı:**

**Önce:** `01-foundations.md`  
**Neden:** Herkes buradan başlar, Sarman'ın mevcut seviyesini base alabiliriz

**Sonra:** `02-ml-fundamentals.md`  
**Neden:** ML'in temelleri, senaryolar için gerekli

**Sonra:** `03-deep-learning.md`  
**Neden:** Modern ML için kritik

**Sonra:** `04-mlops-production.md`  
**Neden:** Senior level için must-have, fark yaratan kısım

**Sonra:** `05-specialized-domains.md`  
**Neden:** Seçmeli, kişiye özel

**Son:** `06-soft-skills.md`  
**Neden:** Teknik beceriler tamamlandıktan sonra

**Her dosya yazarken:**
```markdown
Checklist:
- [ ] Giriş paragrafı yazdım
- [ ] Alt başlıkları detaylandırdım
- [ ] Her skill için:
  - [ ] Checkbox ekledim
  - [ ] Zorluk seviyesi (Beginner/Intermediate/Advanced)
  - [ ] Tahmini süre
  - [ ] Kısa açıklama (ne için kullanılır)
  - [ ] En az 1 kaynak linki
  - [ ] Mini proje önerisi
- [ ] Pro tips ekledim
- [ ] Common mistakes bölümü ekledim
- [ ] Sarman'ın deneyimlerinden örnekler ekledim
```

**Her Dosya için Tamamlanma Kriteri:**
- [ ] 20-30 checkbox item var
- [ ] Her item için kaynak var
- [ ] En az 2-3 mini proje önerisi var
- [ ] Gerçekçi süre tahminleri yapıldı

**Tahmini Süre:** 
- Her dosya: 1.5-2 gün
- Toplam: 9-12 gün

---

### 3.2 Senaryo Dosyaları

**Template:**
```markdown
# Senaryo: [Başlık]

## Durum Analizi
[2-3 paragraf - Gerçekçi bir hikaye. Şirket, problem, beklentiler]

## Business Gereksinimleri
- Metric 1 (örn: Accuracy >85%)
- Metric 2 (örn: Inference time <100ms)
- Metric 3 (örn: Explainability)

## Teknik Gereksinimler
- Python 3.8+
- Libraries: ...
- Infrastructure: ...

## Bu Senaryoda Kullanacağın Beceriler
- [ ] Skill 1 (from roadmap X.Y)
- [ ] Skill 2 (from roadmap X.Z)
...

## Zorluk Seviyesi: [Beginner/Intermediate/Advanced]
**Tahmini Süre:** X hafta  
**Önkoşullar:** ...

## Adım Adım Çözüm Yolu

### Faz 1: Veri Analizi & Problem Tanımı (X gün)
- [ ] Task 1
- [ ] Task 2
...

### Faz 2: Feature Engineering (X gün)
...

### Faz 3: Model Development
...

### Faz 4: Deployment
...

## Yaygın Hatalar
1. **Data Leakage:** ...
2. **Overfitting:** ...

## Nasıl Test Edeceksin?
- Unit tests
- Integration tests
- Performance benchmarks

## Sonuç & Çıktılar
- [ ] GitHub repo
- [ ] README with results
- [ ] Deployed API (opsiyonel)
- [ ] Blog post (opsiyonel)

## Nasıl Geliştirebilirsin? (V2)
- Advanced feature 1
- Advanced feature 2
...

## Portföy İçin
Bu projeyi CV/portfolio'na nasıl eklersin, nelere dikkat et

## Ek Kaynaklar
- Tutorial 1
- Paper 1
- Similar project examples
```

**Yazım Öncelikleri:**
1. **Beginner-01 (Churn Prediction)** - En temel, herkes için
2. **Intermediate-01 (Turkish NER)** - Sarman'ın uzmanlık alanı
3. **Advanced-01 (Production LLM)** - Trend, senior level
4. Diğerleri...

**Her Senaryo için Tamamlanma Kriteri:**
- [ ] Gerçekçi business case yazdık
- [ ] Step-by-step solution var
- [ ] Common pitfalls belirtildi
- [ ] Roadmap'teki becerilere link verildi
- [ ] Test kriterleri belirtildi

**Tahmini Süre:** 
- Her senaryo: 0.5-1 gün
- İlk 6 senaryo: 3-5 gün

---

### 3.3 Destek Dosyaları

#### `README.md` - Ana Tanıtım

**İçerik:**
```markdown
# Senior ML Engineer Roadmap

[Badge: License] [Badge: Stars] [Badge: PRs Welcome]

> Sıfırdan Senior ML Engineer olmak için **actionable, senaryo bazlı** roadmap.

## Neden Bu Roadmap Farklı?

| Diğer Roadmaps | Bu Roadmap |
|----------------|------------|
| Sadece konu listesi | Senaryo bazlı öğrenme |
| "PyTorch öğren" gibi genel | "Production'da LLM fine-tune et" gibi spesifik |
| Süre tahmini yok | Her skill için gerçekçi süre |
| Nasıl test edeceğin belirsiz | Her seviye için mini projeler |

## İstatistikler

- **150+ Beceri** detaylı açıklamalarla
- **15+ Gerçek Dünya Senaryosu**
- **100+ Küratörlenmiş Kaynak**
- **Tahmini Süre:** 12-18 ay (haftada 15-20 saat)

## Roadmap Kategorileri

[Diagram/Flow]

## Nasıl Başlayacaksın?

1. **Seviyeni Belirle:** [Self-assessment quiz linki]
2. **Rotanı Çiz:** Hangi kategorilerden başlayacaksın?
3. **İlk Senaryonu Seç:** Beginner? → Churn Prediction
4. **Takip Et:** `progress-tracker.md` kullan
5. **Paylaş:** Portfolio projelerini oluştur

## Örnek Senaryolar

### Beginner
- E-ticaret Churn Prediction
- House Price API
...

### Intermediate
- Turkish Named Entity Recognition
- Multi-class Image Classifier
...

### Advanced
- Production LLM Fine-tuning
- Distributed Training
...

## Kaynaklar

[Books] [Courses] [Papers] [Tools]

## Katkıda Bulun

Contributions are welcome! Bkz: [CONTRIBUTING.md]

## License

MIT License - bkz: [LICENSE]

## Acknowledgments

- Kendi ML journey'mden öğrendiklerim
- Harika açık kaynak topluluğu
...

## Star History

[Star history chart]
```

**Tamamlanma Kriteri:**
- [ ] Açıklayıcı ve çekici giriş
- [ ] Farkımızı vurgulayan tablo
- [ ] Kullanım talimatları
- [ ] Senaryo örnekleri
- [ ] Contribution guidelines

**Tahmini Süre:** 1 gün

---

#### `progress-tracker.md` - İlerleme Takip Template
```markdown
# İlerleme Takibim

## Hedefim
[Senior ML Engineer olmak / Belirli bir role başvurmak / vb.]

**Başlangıç:** [Tarih]  
**Hedef Tamamlanma:** [Tarih]  
**Haftada Ayıracağım Süre:** [X saat]

---

## Genel İlerleme

**Toplam Beceri:** 150  
**Tamamlanan:** 0 / 150  
**İlerleme:** Progress 0%

---

## Kategori Bazlı İlerleme

### 01 - Foundations
**Tamamlanan:** 0/25  
**Durum:** Başlamadı / Devam Ediyor / Tamamlandı

### 02 - ML Fundamentals
**Tamamlanan:** 0/30  
**Durum:** Başlamadı

...

---

## Tamamlanan Senaryolar

- [ ] Beginner-01: Churn Prediction
  - Başlangıç: [Tarih]
  - Bitiş: [Tarih]
  - GitHub: [Link]
  - Not: ...

---

## Haftalık Loglar

### Hafta 1 (Tarih)
**Çalışılan Süre:** X saat  
**Tamamlanan:**
- [ ] Skill 1
- [ ] Skill 2

**Notlar:**
...

**Gelecek Hafta:**
...

---

### Hafta 2 (Tarih)
...
```

**Tahmini Süre:** 0.5 gün

---

#### `CONTRIBUTING.md`
```markdown
# Katkıda Bulunma Rehberi

Bu roadmap açık kaynak bir proje! Katkılarınız çok değerli.

## Nasıl Katkıda Bulunabilirsin?

### 1. Yeni Kaynak Öner
Harika bir kurs/kitap/tutorial buldun mu? 

### 2. Senaryo Ekle
Gerçek dünyadan senaryolar ekle

### 3. Hata Düzelt
Typo, broken link, outdated info

### 4. Deneyimini Paylaş
"Bu skill'i öğrenirken şunu yaptım" gibi

## PR Süreci

1. Fork the repo
2. Create a branch (`feature/new-scenario`)
3. Make changes
4. Test (linklerin çalıştığından emin ol)
5. Commit (`git commit -m 'Add Turkish NER scenario'`)
6. Push & create PR

## PR Checklist

- [ ] Markdown formatı doğru
- [ ] Linkler çalışıyor
- [ ] Yeni içerik roadmap stiline uygun
- [ ] Türkçe karakter problemi yok

## Code of Conduct

Be respectful, inclusive, constructive.
```

**Tahmini Süre:** 0.5 gün

---

## Aşama 4: Görsel & Polish (2-3 gün)

### 4.1 Roadmap Diagram

**Amaç:** Görsel flow chart

**Tool:** Excalidraw / Mermaid

**İçerik:**
```
Foundations → ML Fundamentals → Deep Learning
                                      ↓
              MLOps ← ← ← ← ← ← ← ← ← 
                ↓
           Specialized Domains
                ↓
           Soft Skills
```

**Tahmini Süre:** 0.5 gün

---

### 4.2 Badges & Visuals

- [ ] License badge
- [ ] GitHub stars badge
- [ ] Contributions welcome badge
- [ ] Progress bar görselleri
- [ ] Skill level icons standardize

**Tahmini Süre:** 0.5 gün

---

### 4.3 README Polish

- [ ] TOC ekle (table of contents)
- [ ] Screenshots ekle (roadmap dosyalarından)
- [ ] Demo GIF (progress tracker kullanımı)
- [ ] "Star if useful" çağrısı

**Tahmini Süre:** 0.5 gün

---

## Aşama 5: Açık Kaynak Hazırlık & Release (1 gün)

### 5.1 Repository Setup

**Checklist:**
- [ ] LICENSE (MIT)
- [ ] .gitignore (Python, IDE, OS files)
- [ ] CODE_OF_CONDUCT.md
- [ ] CONTRIBUTING.md
- [ ] Issue templates:
  - Bug report
  - Feature request
  - New resource suggestion
- [ ] PR template

**Tahmini Süre:** 0.5 gün

---

### 5.2 İlk Release (v0.1.0)

**Pre-release Checklist:**
- [ ] Tüm linkler çalışıyor
- [ ] Typo kontrolü
- [ ] README net ve çekici
- [ ] En az 3 senaryo tamamlandı
- [ ] Resources populated

**Release Notes:**
```markdown
# v0.1.0 - Initial Release

## İlk Versiyon

### İçerik:
- 6 roadmap kategorisi (150+ skill)
- 6 senaryo (2 beginner, 2 intermediate, 2 advanced)
- 50+ kaynak
- Progress tracker template

### Gelecek Versiyonlarda:
- [ ] Daha fazla senaryo
- [ ] Video tutorials
- [ ] Interactive quizzes
...
```

**GitHub Topics:**
- machine-learning
- roadmap
- mlops
- deep-learning
- python
- career-development
- learning-path

**Tahmini Süre:** 0.5 gün

---

## İş Bölümü

### Claude (Ben):
- Industry research & analiz
- Technical içerik yazımı (roadmap dosyaları)
- Senaryo yazımı (detaylı step-by-step)
- Kaynak küratörlüğü
- Template'ler oluşturma
- Markdown formatting

### Sarman (Sen):
- Proje yönetimi & koordinasyon
- Bu roadmap dosyasını update etme
- Araştırma sonuçlarını review
- Türkçe içerik review (doğallık)
- Kendi deneyimlerini ekleme
- GitHub repo setup & management
- Git operations (commit, push, PR)
- Release management

---

## Detaylı Zaman Çizelgesi

### Hafta 1: Araştırma
- **Gün 1-2:** Industry research (1.1)
- **Gün 2:** Competitor analysis (1.2)
- **Gün 3:** Kaynak araştırma (1.3)
- **Gün 3:** Skill matrix (1.4)

### Hafta 2: Taslak & İlk İçerik
- **Gün 1-2:** Roadmap taslakları (2.1)
- **Gün 2:** Senaryo mapping (2.2)
- **Gün 3-4:** `01-foundations.md` yazımı (3.1)

### Hafta 3: Ana İçerik
- **Gün 1-2:** `02-ml-fundamentals.md` (3.1)
- **Gün 3-4:** `03-deep-learning.md` (3.1)
- **Gün 5:** İlk senaryo (Churn Prediction)

### Hafta 4: Tamamlama & Release
- **Gün 1-2:** `04-mlops-production.md` (3.1)
- **Gün 3:** Destek dosyaları (README, vb.) (3.3)
- **Gün 4:** Polish & görsel (4.x)
- **Gün 5:** Repository setup & release (5.x)

---

## Günlük Kontrol Listesi

Her gün sonunda:
- [ ] Bugün ne tamamlandı?
- [ ] Hangi dosyalar güncellendi?
- [ ] Blocker var mı?
- [ ] Yarın ne yapılacak?
- [ ] Git commit yapıldı mı?

---

## Başarı Kriterleri (Proje Tamamlanma)

- [ ] 6 roadmap dosyası tamamlandı (her biri 20+ item)
- [ ] En az 6 senaryo yazıldı (2 beginner, 2 intermediate, 2 advanced)
- [ ] 50+ kaynak küratörlendi
- [ ] README profesyonel ve çekici
- [ ] Tüm linkler çalışıyor
- [ ] GitHub repo public ve düzenli
- [ ] v0.1.0 release yapıldı
- [ ] İlk 10 star!

---

## Notlar & Kararlar

### Kararlaştırılanlar:
- Açık kaynak (MIT License)
- Senaryo bazlı yaklaşım
- Türkçe NLP'ye özel vurgu
- Production/MLOps ağırlıklı

### Açık Sorular:
- [ ] İnteraktif quiz ekleyelim mi? (v2)
- [ ] Video tutorials? (v2)
- [ ] Discord/community? (v2)

---

## İlgili Dökümanlar

Oluşturulacak research dosyaları:
- `research/industry-requirements.md`
- `research/competitor-analysis.md`
- `research/skill-matrix.md`

---

**Son Güncelleme:** [Tarih]  
**Versiyon:** 1.0  
**Status:** In Progress"""

# Remove emojis function
def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002500-\U00002BEF"  # chinese char
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\ufe0f"  # dingbats
        "\u3030"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', text)

# Write the restored content without emojis
cleaned_content = remove_emojis(original_content)
with open('docs/project_roadmap.md', 'w', encoding='utf-8') as f:
    f.write(cleaned_content)

print("Dosya başarıyla geri yüklendi ve emojiler silindi!")
