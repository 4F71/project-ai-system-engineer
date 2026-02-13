# AI SYSTEM ENGINEER KANONU — MASTER ROADMAP (KİLİTLİ / NİHAİ)

## KANUN: TİKLEME KURALI
Her madde ancak **kanıtla** tiklenir.

Kanıt türleri:
- Dosya yolu (repo içinde)
- Çalışan komut çıktısı (terminal)
- Commit hash / PR linki
- Screenshot (gerekirse)
- Canlı demo linki (varsa)

Her madde için kanıt satırı:
- Kanıt: `<path | command output | commit>`

---

# I. AKİDE (ZİHİN, DİSİPLİN, SİSTEM)

## I.1 Öğrenme Sistemi (Repo Dinamiği)
- [ ] Repo mimarisi kilitli ve sade (klasörler sabit)
  - Kanıt:
- [ ] Haftalık sprint döngüsü kurulmuş (haftada 1 deliverable)
  - Kanıt:
- [x] Journal sistemi aktif (her hafta 1 dosya)
  - Kanıt:
        - proofs/03-ml/repeat-purchase-system.md 
        - docs/journal/2026-02-Week02.md
- [ ] Concepts sistemi aktif (her kavram dosyası TR+EN)
  - Kanıt: 
      - docs/concepts/00b-numerical-foundations-square-root-TR.md
      - docs/concepts/02-linear-algebra-norms.md
- [ ] Progress tracker (checklist) çalışıyor, kanıtsız tik yok
  - Kanıt:
- [ ] “Şişirme yasağı” uygulanıyor (gereksiz dosya/klasör yok)
  - Kanıt:

## I.2 İrade Disiplini (Çalışma Ritüeli)
- [ ] Günlük minimum ritüel tanımlandı ve uygulanıyor
  - [ ] 30 dk temel (math / cs)
  - [ ] 60–120 dk üretim (kod)
  - [ ] 10 dk yazı (journal / concept)
  - Kanıt:
- [ ] Haftalık ritüel tanımlandı ve uygulanıyor
  - [ ] 1 deliverable
  - [ ] 1 retrospektif güncellemesi (aylık)
  - Kanıt:

---

# II. BİLİMİN TEMELLERİ (CS FOUNDATIONS)

## II.1 Veri Yapıları
- [ ] Array / List
  - [ ] erişim / ekleme / silme karmaşıklığı
  - [ ] Python list davranışı (amortized)
  - Kanıt:
- [ ] Stack / Queue
  - [ ] kullanım alanları
  - [ ] thread-safe kuyruk kavramı
  - Kanıt:
- [ ] Hash Map
  - [ ] hashing / collision kavramı
  - [ ] Python dict içgörüsü (high-level)
  - Kanıt:
- [ ] Linked List (temel sezgi)
  - [ ] neden nadiren tercih edilir (cache locality)
  - Kanıt:
- [ ] Tree (Binary Tree, BST)
  - [ ] traversal (inorder/preorder/postorder)
  - Kanıt:
- [ ] Heap / Priority Queue
  - [ ] scheduling / top-k kullanım
  - Kanıt:
- [ ] Graph
  - [ ] BFS / DFS
  - [ ] shortest path sezgisi
  - Kanıt:

## II.2 Algoritmalar ve Karmaşıklık
- [ ] Big-O temeli
  - [ ] zaman / bellek trade-off
  - Kanıt:
- [ ] Sıralama algoritmaları (sezgi düzeyi)
  - [ ] quicksort / mergesort farkı
  - Kanıt:
- [ ] Arama (binary search)
  - [ ] sorted invariant
  - Kanıt:
- [ ] Dinamik programlama (başlangıç)
  - [ ] memoization vs tabulation
  - Kanıt:

## II.3 İşletim Sistemi (OS)
- [ ] Process vs Thread
  - [ ] context switch sezgisi
  - Kanıt:
- [ ] Memory
  - [ ] stack vs heap
  - [ ] paging/virtual memory sezgisi
  - Kanıt:
- [ ] File system temeli
  - [ ] inode sezgisi (yüksek seviye)
  - Kanıt:
- [ ] Scheduling kavramları (yüksek seviye)
  - Kanıt:

## II.4 Concurrency (Eşzamanlılık)
- [ ] Race condition nedir?
  - Kanıt:
- [ ] Lock / Mutex / Semaphore sezgisi
  - Kanıt:
- [ ] Producer–Consumer modeli
  - Kanıt:
- [ ] Async IO sezgisi (CPU-bound vs IO-bound)
  - Kanıt:

## II.5 Ağ (Networking)
- [ ] HTTP temel (request/response)
  - [ ] status codes
  - Kanıt:
- [ ] TCP/UDP sezgisi
  - Kanıt:
- [ ] DNS sezgisi
  - Kanıt:
- [ ] Load balancing sezgisi
  - Kanıt:

## II.6 Veritabanı Temeli
- [ ] Transaction nedir?
  - Kanıt:
- [ ] ACID sezgisi
  - Kanıt:
- [ ] Index nedir? neden hızlandırır?
  - Kanıt:
- [ ] Isolation levels sezgisi
  - Kanıt:

---

# III. MATEMATİK KANUNU (ML İÇİN MATEMATİK)

## III.0 Numerical Foundations (Sayısal Akıcılık)

- [x] Square root computation
  - [x] perfect squares
  - [x] decimal → fraction dönüşümü
  - [x] √(a/b) kuralı
  - [x] ordering preservation (√a < √b)
  - Kanıt:
    - proofs/02-math/2026-02-square-root-proof.md

---

## III.1 Linear Algebra (ML Odak)

- [ ] Scalar / Vector / Matrix tanımı ve sezgisi
  - Kanıt:
- [ ] Vector operations
  - [ ] addition
  - [ ] scalar multiplication
  - Kanıt:
- [ ] Dot product
  - [ ] geometrik anlam (benzerlik)
  - [ ] cosine similarity bağlantısı
  - Kanıt:
- [x] Norms
  - [x] L1 norm
  - [x] L2 norm sezgisi
  - [x] unit vector kavramı
  - [x] L1 ≥ L2 gözlemi
  - Kanıt:
    - proofs/02-math/2026-02-linear-algebra-norms-proof.md
    - scripts/math/norm_demo.py
    - scripts/math/vector_plot_demo.py
    - scripts/math/norm_distance_demo.py
    - proofs/02-math/assets/vectors-demo.png
    - proofs/02-math/assets/l1-vs-l2-path.png
    
- [ ] Matrix multiplication
  - [ ] shape kuralları
  - [ ] linear layer bağlantısı
  - Kanıt:
- [ ] Eigen sezgisi
  - [ ] “önemli yönler” fikri
  - Kanıt:

---

## III.2 Probability & Statistics (ML Odak)

- [ ] Random variable
  - Kanıt:
- [ ] Distribution
  - [ ] normal
  - [ ] bernoulli
  - [ ] categorical
  - Kanıt:
- [ ] Expectation, variance
  - Kanıt:
- [ ] Sampling sezgisi
  - Kanıt:
- [ ] Bayes sezgisi (prior/posterior)
  - Kanıt:
- [ ] Likelihood vs probability
  - Kanıt:

---

## III.3 Calculus & Optimization (Yeterli Seviye)

- [ ] Derivative sezgisi (eğim)
  - Kanıt:
- [ ] Partial derivatives sezgisi
  - Kanıt:
- [ ] Gradient sezgisi
  - Kanıt:
- [ ] Chain rule (backprop’ın kalbi)
  - Kanıt:
- [ ] Gradient descent
  - [ ] learning rate etkisi
  - [ ] convergence sezgisi
  - Kanıt:

---

# IV. YAZILIM MÜHENDİSLİĞİ (PRODUCTION HABITS)

## IV.1 Git ve Akış

- [ ] Branching stratejisi (main/dev/feature)
  - Kanıt:
- [ ] Commit standardı (mesaj, küçük commit)
  - Kanıt:
- [ ] PR kültürü (self-review checklist)
  - Kanıt:

---

## IV.2 Kod Kalitesi

- [ ] Lint + format standardı (black/ruff vb.)
  - Kanıt:
- [ ] Type checking (mypy/pyright vb.)
  - Kanıt:
- [ ] Logging standardı (structured log sezgisi)
  - Kanıt:
- [ ] Error handling (fail fast, clear exceptions)
  - Kanıt:

---

## IV.3 Testing (Zorunlu)

- [ ] Unit test nedir? neyi ölçer?
  - Kanıt:
- [ ] Integration test nedir?
  - Kanıt:
- [ ] E2E test nedir?
  - Kanıt:
- [ ] Test yapısı (pytest)
  - Kanıt:
- [ ] Mocking sezgisi
  - Kanıt:

---

## IV.4 Paketleme ve Konfig

- [ ] pyproject / requirements disiplini
  - Kanıt:

- [ ] Config yönetimi (env + config file)
  - Kanıt:

- [ ] Secrets yönetimi (repo’ya secret koymama)
  - Kanıt:


---

# V. PYTHON SYSTEM ENGINEERING

## V.1 Temel Araçlar
- [ ] venv/poetry/uv gibi bir standardı seçip uygulama
  - Kanıt:
- [ ] CLI yazma (argparse/typer)
  - Kanıt:
- [ ] Profiling (time)
  - Kanıt:
- [ ] Profiling (memory)
  - Kanıt:

## V.2 Paralellik
- [ ] multiprocessing temel
  - Kanıt:
- [ ] queue tabanlı worker modeli
  - Kanıt:
- [ ] async (IO-bound pipeline örneği)
  - Kanıt:

## V.3 Performans Zihniyeti
- [ ] vectorization (NumPy) ile hızlandırma
  - Kanıt:
- [ ] bottleneck analizi (ölç → düzelt → tekrar ölç)
  - Kanıt:

---

# VI. DATA KANUNU (SQL + MODELLEME + PIPELINE)

## VI.1 SQL Temelleri
- [ ] SELECT / WHERE / ORDER BY
  - Kanıt:
- [ ] JOIN (inner/left/right) sezgisi
  - Kanıt:
- [ ] GROUP BY / HAVING
  - Kanıt:
- [ ] Window functions (row_number, lag/lead)
  - Kanıt:
- [ ] CTE (WITH) kullanımı
  - Kanıt:
- [ ] Index sezgisi + query plan fikri
  - Kanıt:

## VI.2 Data Modeling (Somut)
- [ ] Entity & relationship düşüncesi
  - Kanıt:
- [ ] Normalization sezgisi (1NF/2NF/3NF)
  - Kanıt:
- [ ] Star schema sezgisi (facts/dimensions)
  - Kanıt:
- [ ] Time-series modeling sezgisi
  - Kanıt:

## VI.3 Data Quality
- [ ] Missing values stratejileri
  - Kanıt:
- [ ] Outlier stratejileri
  - Kanıt:
- [ ] Data validation (schema checks)
  - Kanıt:
- [ ] Data leakage kontrolleri
  - Kanıt:

## VI.4 Pipeline Orchestration (Kavram)
- [ ] Batch pipeline sezgisi
  - Kanıt:
- [ ] Streaming sezgisi
  - Kanıt:
- [ ] Orchestrator kavramı (Airflow/Prefect)
  - Kanıt:

---

# VI+ (EK) DATA PLATFORM KANUNU (GERÇEK DÜNYA DERİNLİĞİ)

## VI+.1 Batch Compute Motorları
- [ ] Pandas vs Polars vs Spark farkı (ne zaman hangisi?)
  - Kanıt:
- [ ] DuckDB ile yerel analitik (parquet + SQL)
  - Kanıt:
- [ ] Büyük veri işleme sezgisi (partition/scan/cost)
  - Kanıt:

## VI+.2 Lakehouse / Warehouse Sezgisi
- [ ] Parquet nedir? neden önemli?
  - Kanıt:
- [ ] Partitioning (tarih, kullanıcı, ülke) stratejileri
  - Kanıt:
- [ ] Compaction / small files problemi sezgisi
  - Kanıt:
- [ ] Table format sezgisi (Delta/Iceberg/Hudi kavram)
  - Kanıt:

## VI+.3 Orchestration Pratiği (DAG Gerçekleri)
- [ ] DAG nedir? task bağımlılıkları
  - Kanıt:
- [ ] Retry/backoff stratejileri
  - Kanıt:
- [ ] Backfill nedir? neden riskli?
  - Kanıt:
- [ ] Idempotency (aynı job’u tekrar çalıştırma güvenliği)
  - Kanıt:

## VI+.4 Streaming Pratiği (Kafka Zihniyeti)
- [ ] Topic/partition nedir?
  - Kanıt:
- [ ] Consumer group nedir?
  - Kanıt:
- [ ] Offset yönetimi (en az bir kez / en fazla bir kez sezgisi)
  - Kanıt:
- [ ] Exactly-once hedefinin pratik zorluğu (sezgi)
  - Kanıt:

## VI+.5 Feature Store (ML Sistemlerinin Sırrı)
- [ ] Offline vs online features nedir?
  - Kanıt:
- [ ] Point-in-time join nedir? (leakage önleme)
  - Kanıt:
- [ ] Feature freshness ve TTL sezgisi
  - Kanıt:
- [ ] Training-serving feature consistency kontrolü
  - Kanıt:

---

# VI++ (EK) LABELING & DATA GOVERNANCE KANUNU (ETİKET, KALİTE, BELGE)

## VI++.1 Labeling Stratejileri
- [ ] Label kaynakları: kullanıcı davranışı, manuel etiket, heuristic etiket
  - Kanıt:
- [ ] Manuel labeling süreci (basit workflow)
  - [ ] görev tanımı (guideline)
  - [ ] örnekler / edge-case listesi
  - Kanıt:
- [ ] Weak supervision sezgisi (heuristic/label model fikri)
  - Kanıt:

## VI++.2 Label Kalitesi
- [ ] Inter-annotator agreement sezgisi (uyuşma)
  - Kanıt:
- [ ] Gold set kavramı + kalite kontrol
  - Kanıt:
- [ ] Label noise ve model etkisi sezgisi
  - Kanıt:

## VI++.3 Dataset Dokümantasyonu
- [ ] Dataset datasheet şablonu (amaç, kaynak, kapsam, riskler)
  - Kanıt:
- [ ] Veri saklama/retention kararı (data policy ile uyum)
  - Kanıt:

---

# VII. MACHINE LEARNING KANUNU (CORE)

## VII.1 Temel Kavramlar
- [ ] Model nedir? parametre nedir?
  - Kanıt:
- [ ] Loss nedir? neyi optimize eder?
  - Kanıt:
- [x] Train/Val/Test ayrımı
  - Kanıt: proofs/03-ml/repeat-purchase-system.md
- [x] Overfitting / underfitting
  - Kanıt: proofs/03-ml/repeat-purchase-system.md
- [ ] Bias–variance sezgisi
  - Kanıt:
- [x] Leakage örnekleri
  - Kanıt: proofs/03-ml/repeat-purchase-system.md

## VII.2 Klasik Modeller (Somut)
- [ ] Linear regression
  - Kanıt:
- [ ] Logistic regression
  - Kanıt:
- [ ] Decision tree
  - Kanıt:
- [ ] Random forest
  - Kanıt:
- [x] Gradient boosting sezgisi
  - Kanıt: proofs/03-ml/repeat-purchase-system.md

## VII.3 Metric Kanunu
- [ ] Regression metrics (MAE/MSE/RMSE/R2)
  - Kanıt:
- [x] Classification metrics (precision/recall/F1/ROC-AUC)
  - Kanıt: proofs/03-ml/repeat-purchase-system.md
- [x] Threshold seçimi sezgisi
  - Kanıt: proofs/03-ml/repeat-purchase-system.md

## VII.4 Error Analysis (Zorunlu)
- [x] Confusion matrix yorumlama
  - Kanıt: proofs/03-ml/repeat-purchase-system.md
- [x] Slices (alt gruplar) analizi
  - Kanıt: proofs/03-ml/repeat-purchase-system.md
- [ ] Ablation düşüncesi
  - Kanıt:

---

# VIII. DEEP LEARNING KANUNU (PYTORCH)

## VIII.1 Sinir Ağı Temeli
- [ ] Layer nedir?
  - Kanıt:
- [ ] Activation functions (relu/sigmoid/tanh sezgisi)
  - Kanıt:
- [ ] Backprop high-level anlayış
  - Kanıt:
- [ ] Optimizer nedir? (SGD/Adam sezgisi)
  - Kanıt:
- [ ] Learning rate / batch size etkisi
  - Kanıt:
- [ ] Regularization (dropout/weight decay sezgisi)
  - Kanıt:

## VIII.2 PyTorch Uygulama
- [ ] Dataset/DataLoader
  - Kanıt:
- [ ] Model tanımı (nn.Module)
  - Kanıt:
- [ ] Training loop (forward/backward/step)
  - Kanıt:
- [ ] Eval loop (no_grad, metrics)
  - Kanıt:
- [ ] Checkpoint save/load
  - Kanıt:
- [ ] GPU çalıştırma (cuda)
  - Kanıt:
- [ ] Mixed precision (amp) sezgisi
  - Kanıt:

---

# IX. TRAINING SYSTEMS (REPRODUCIBILITY)

## IX.1 Deney Takibi
- [ ] Experiment tracking standardı seçildi (MLflow/W&B)
  - Kanıt:
- [ ] Config standardı (yaml + env)
  - Kanıt:
- [ ] Seed + determinism farkındalığı
  - Kanıt:

## IX.2 Checkpoint ve Versiyon
- [ ] Model versiyonlama yaklaşımı
  - Kanıt:
- [ ] Dataset versiyonlama yaklaşımı
  - Kanıt:
- [ ] Training run raporu standardı
  - Kanıt:

---

# IX+ (EK) MLOPS LIFECYCLE KANUNU (REGISTRY + PROMOTION + LINEAGE)

## IX+.1 Model Registry
- [ ] Registry nedir? neden şart?
  - Kanıt:
- [ ] Stage kavramı (dev / staging / prod)
  - Kanıt:
- [ ] Model artifact + metadata standartları (config, metrics, dataset ref)
  - Kanıt:

## IX+.2 Promotion Politikası (Prod’a Çıkış)
- [ ] Promotion kriterleri tanımlandı (metrik eşikleri)
  - Kanıt:
- [ ] Gating: testler + eval suite geçmeden prod yok
  - Kanıt:
- [ ] Canary / shadow / rollout stratejileri (kurallı)
  - Kanıt:

## IX+.3 Rollback ve Governance
- [ ] Rollback tetikleyicileri tanımlandı (metric degrade, error spike)
  - Kanıt:
- [ ] Rollback prosedürü yazıldı (runbook)
  - Kanıt:
- [ ] Onay mekanizması (kim, neye göre?)
  - Kanıt:

## IX+.4 Lineage (Nereden geldi bu model?)
- [ ] Model ↔ dataset ↔ code ↔ config bağını yazma (lineage)
  - Kanıt:
- [ ] Reproducibility raporu: “aynı run nasıl tekrar edilir?”
  - Kanıt:

---

# X. INFERENCE & SERVING (ÜRETİM)

## X.1 Serving Temeli
- [ ] REST API (FastAPI) ile model serve
  - Kanıt:
- [ ] Request validation (schema)
  - Kanıt:
- [ ] Batch inference sezgisi
  - Kanıt:

## X.2 Performans
- [ ] Latency vs throughput ayrımı
  - Kanıt:
- [ ] Caching sezgisi
  - Kanıt:
- [ ] CPU vs GPU inference sezgisi
  - Kanıt:

## X.3 Model Packaging
- [ ] Model export (TorchScript/ONNX sezgisi)
  - Kanıt:
- [ ] Quantization sezgisi (INT8/FP16)
  - Kanıt:

---

# X+ (EK) SERVICE ENGINEERING KANUNU (API GERÇEKLERİ)

## X+.1 API Contract & Versioning
- [ ] API contract nedir? (OpenAPI/Swagger sezgisi)
  - Kanıt:
- [ ] Versiyonlama stratejisi (v1/v2)
  - Kanıt:
- [ ] Breaking change nedir? nasıl yönetilir?
  - Kanıt:
- [ ] Backward compatibility kuralı
  - Kanıt:

## X+.2 Authn / Authz (Pratik Sezgi)
- [ ] Authentication vs authorization farkı
  - Kanıt:
- [ ] JWT sezgisi (token doğrulama akışı)
  - Kanıt:
- [ ] Role-based access control sezgisi
  - Kanıt:

## X+.3 Rate Limiting & Abuse Protection
- [ ] Rate limit neden gerekir?
  - Kanıt:
- [ ] Throttling sezgisi
  - Kanıt:
- [ ] Abuse / DoS farkındalığı (minimum)
  - Kanıt:

## X+.4 Reliability Patterns (Prod Kalıpları)
- [ ] Timeout kuralı (hangi katmanda?)
  - Kanıt:
- [ ] Retry/backoff stratejisi (ne zaman yapılmaz?)
  - Kanıt:
- [ ] Idempotency (aynı isteğin tekrar çalışması güvenliği)
  - Kanıt:
- [ ] Circuit breaker sezgisi
  - Kanıt:

---

# X++ (EK) MODEL OPTIMIZATION KANUNU (HIZ, BOYUT, MALİYET)

## X++.1 Distillation
- [ ] Distillation sezgisi (teacher → student)
  - Kanıt:
- [ ] Ne zaman mantıklı? (maliyet/latency)
  - Kanıt:

## X++.2 Pruning
- [ ] Pruning sezgisi (ağırlık/kanal budama)
  - Kanıt:
- [ ] Accuracy trade-off sezgisi
  - Kanıt:

## X++.3 Compilation & Accelerators
- [ ] ONNX Runtime sezgisi (deployment için)
  - Kanıt:
- [ ] TensorRT sezgisi (GPU inference hızlandırma)
  - Kanıt:

## X++.4 Batching Stratejileri
- [ ] Static batching vs dynamic batching sezgisi
  - Kanıt:
- [ ] Queue-based batching tasarımı sezgisi
  - Kanıt:

---

# XI. OBSERVABILITY & RELIABILITY (SRE FOR ML)

## XI.1 Observability
- [ ] Logging standardı (request id, structured logs)
  - Kanıt:
- [ ] Metrics (latency, error rate, throughput)
  - Kanıt:
- [ ] Tracing sezgisi
  - Kanıt:

## XI.2 SLO Disiplini
- [ ] SLI/SLO kavramları
  - Kanıt:
- [ ] Alerting sezgisi
  - Kanıt:
- [ ] Incident response akışı (runbook)
  - Kanıt:
- [ ] Postmortem şablonu
  - Kanıt:

---

# XI+ (EK) MODEL MONITORING KANUNU (ML’YE ÖZGÜ ÜRETİM GERÇEĞİ)

## XI+.1 Data Drift / Concept Drift
- [ ] Data drift nedir? nasıl yakalanır?
  - Kanıt:
- [ ] Concept drift nedir? neden daha tehlikeli?
  - Kanıt:
- [ ] Drift metrikleri sezgisi (PSI, KL, histogram compare)
  - Kanıt:

## XI+.2 Training-Serving Skew
- [ ] Training-serving skew nedir?
  - Kanıt:
- [ ] Feature pipeline parity (aynı transform garantisi)
  - Kanıt:

## XI+.3 Label Delay ve Feedback Loop
- [ ] Label delay nedir? üretimde etkisi
  - Kanıt:
- [ ] Feedback loop riski (model veriyi etkiler)
  - Kanıt:

## XI+.4 Model Regression Testing
- [ ] Offline eval suite standardı
  - Kanıt:
- [ ] Prod metrikleri ile offline metrik eşlemesi
  - Kanıt:
- [ ] Deployment sonrası “regression guard” kuralı
  - Kanıt:

---

# XI++ (EK) OBSERVABILITY STACK KANUNU (DÜZEN, STANDARD, RUNBOOK)

## XI++.1 Metric Standardı
- [ ] Metric isimlendirme standardı (naming)
  - Kanıt:
- [ ] Label/tag standardı (cardinality farkındalığı)
  - Kanıt:

## XI++.2 Dashboard Standardı
- [ ] “Golden signals” sezgisi (latency, traffic, errors, saturation)
  - Kanıt:
- [ ] p50/p95/p99 latency raporlama standardı
  - Kanıt:
- [ ] Error budget sezgisi (minimum)
  - Kanıt:

## XI++.3 Alert Policy
- [ ] Alert eşiği belirleme (false positive azaltma)
  - Kanıt:
- [ ] Alert fatigue nedir? nasıl önlenir?
  - Kanıt:

## XI++.4 Runbook Standardı
- [ ] Runbook şablonu (semptom → kontrol → çözüm → doğrulama)
  - Kanıt:
- [ ] Incident sonrası postmortem disiplini
  - Kanıt:

---

# XI+++ (EK) ONLINE EVAL / A-B TEST KANUNU (ÜRÜN GERÇEĞİ)

## XI+++.1 A/B Test Sezgisi
- [ ] Randomization nedir? neden şart?
  - Kanıt:
- [ ] Sample size sezgisi (güç / süre / trafik)
  - Kanıt:
- [ ] Guardrail metrikleri (error rate, latency, abuse)
  - Kanıt:

## XI+++.2 Feature Flags / Rollout Control
- [ ] Feature flag sezgisi
  - Kanıt:
- [ ] Rollout aşamaları (0%→1%→10%→50%→100%)
  - Kanıt:
- [ ] Rollback trigger kuralı (online degrade)
  - Kanıt:

---

# XII. CLOUD & INFRA (MINIMUM VIABLE)

## XII.1 Linux
- [ ] shell temeli
  - Kanıt:
- [ ] process izle (top/ps)
  - Kanıt:
- [ ] disk/network debug sezgisi
  - Kanıt:

## XII.2 Docker
- [ ] Dockerfile yazma
  - Kanıt:
- [ ] container run + volume + env
  - Kanıt:
- [ ] image tag/version disiplini
  - Kanıt:

## XII.3 Kubernetes (Sezgi → Pratik)
- [ ] Deployment/Service sezgisi
  - Kanıt:
- [ ] Scaling sezgisi
  - Kanıt:

## XII.4 CI/CD
- [ ] test pipeline (lint/test)
  - Kanıt:
- [ ] build + deploy pipeline sezgisi
  - Kanıt:

---

# XII+ (EK) CLOUD DERİNLİK KANUNU (IAM + VPC + STORAGE + QUEUE)

## XII+.1 IAM (Least Privilege)
- [ ] IAM nedir? policy nedir?
  - Kanıt:
- [ ] Least privilege pratik kural seti
  - Kanıt:
- [ ] Service account / role sezgisi
  - Kanıt:

## XII+.2 VPC / Network Güvenliği
- [ ] VPC/subnet nedir?
  - Kanıt:
- [ ] Security group / firewall sezgisi
  - Kanıt:
- [ ] Public vs private subnet sezgisi
  - Kanıt:

## XII+.3 Object Storage (S3 Benzeri)
- [ ] Object storage nedir? neden ML’de merkez?
  - Kanıt:
- [ ] Lifecycle policy (retention, tiering) sezgisi
  - Kanıt:
- [ ] Cost awareness (read/write, egress sezgisi)
  - Kanıt:

## XII+.4 Queue + Async Job Patterns
- [ ] Queue nedir? ne zaman gerekir?
  - Kanıt:
- [ ] Producer/consumer job modeli (retry + DLQ sezgisi)
  - Kanıt:
- [ ] Idempotent job tasarımı (yeniden çalışma güvenliği)
  - Kanıt:

---

# XII++ (EK) IaC KANUNU (INFRASTRUCTURE AS CODE)

## XII++.1 IaC Temeli
- [ ] IaC nedir? neden şart?
  - Kanıt:
- [ ] Terraform sezgisi (resource, state, plan/apply)
  - Kanıt:

## XII++.2 Infra Plan Dokümanı
- [ ] Network planı (VPC/subnet/ingress)
  - Kanıt:
- [ ] Storage planı (object store + lifecycle)
  - Kanıt:
- [ ] Compute planı (CPU/GPU, autoscaling sezgisi)
  - Kanıt:

---

# XIII. SECURITY & PRIVACY (ZORUNLU MINIMUM)

- [ ] Secrets management (env/secret store)
  - Kanıt:
- [ ] Authn/Authz sezgisi
  - Kanıt:
- [ ] Least privilege düşüncesi
  - Kanıt:
- [ ] PII farkındalığı + veri saklama ilkesi
  - Kanıt:

---

# XIII+ (EK) SECURITY PRATİKLERİ KANUNU (THREAT MODEL + ROTATION + SBOM + LOG HIJYENİ)

## XIII+.1 Threat Modeling (Basit Şablon)
- [ ] Varlıklar: veri, model, anahtarlar, kullanıcılar
  - Kanıt:
- [ ] Tehditler: sızma, manipülasyon, prompt injection, data poisoning sezgisi
  - Kanıt:
- [ ] Mitigation: auth, rate limit, validation, audit logging
  - Kanıt:

## XIII+.2 Secrets Rotation
- [ ] Rotation neden gerekli?
  - Kanıt:
- [ ] Rotation planı (kim, ne sıklık, nasıl revoke?)
  - Kanıt:

## XIII+.3 Supply Chain / Dependency Risk
- [ ] Dependency pinning disiplini
  - Kanıt:
- [ ] SBOM sezgisi (en azından kavram)
  - Kanıt:
- [ ] Vulnerability scanning sezgisi
  - Kanıt:

## XIII+.4 PII Redaction & Log Hijyeni
- [ ] Log’larda PII yasak kuralı
  - Kanıt:
- [ ] Redaction stratejileri (hash/mask)
  - Kanıt:
- [ ] Data retention (ne kadar saklanır?) kararı
  - Kanıt:

---

# XIII++ (EK) RESPONSIBLE AI / MODEL RISK KANUNU (ÜRETİMDE RİSK)

## XIII++.1 Bias / Fairness
- [ ] Bias nedir? nereden gelir?
  - Kanıt:
- [ ] Slice-based fairness kontrolü (alt gruplar)
  - Kanıt:
- [ ] Fairness trade-off sezgisi (accuracy vs fairness)
  - Kanıt:

## XIII++.2 Data Poisoning & Adversarial Risk (Sezgi)
- [ ] Data poisoning sezgisi (training set manipülasyonu)
  - Kanıt:
- [ ] Threat model ile bağ kurma
  - Kanıt:

## XIII++.3 Misuse Risk & Mitigation
- [ ] Model misuse senaryoları listesi
  - Kanıt:
- [ ] Mitigation listesi (rate limit, auth, logging, filtering)
  - Kanıt:

---

# XII+++ (EK) DISTRIBUTED SYSTEMS KANUNU (CONSISTENCY, FAILURE, DESIGN)

## XII+++.1 Consistency Temelleri
- [ ] CAP sezgisi (consistency/availability/partition tolerance)
  - Kanıt:
- [ ] Eventual consistency nedir? pratik etkisi
  - Kanıt:

## XII+++.2 Failure Gerçekleri
- [ ] Partial failure sezgisi (ağın/servisin “yarı çalışması”)
  - Kanıt:
- [ ] Timeouts neden “default” olmalı?
  - Kanıt:
- [ ] Retries neden bazen felaket?
  - Kanıt:

## XII+++.3 Idempotency + Dedup
- [ ] Idempotency key tasarımı (API/Job)
  - Kanıt:
- [ ] Deduplication sezgisi (at-least-once dünyası)
  - Kanıt:

---

# X+++ (EK) CACHING KANUNU (PERFORMANS VE MALİYET)

## X+++.1 Cache Temeli
- [ ] Cache key tasarımı (stability, collisions farkındalığı)
  - Kanıt:
- [ ] TTL stratejisi (data freshness)
  - Kanıt:
- [ ] Invalidation neden zordur? (sezgi)
  - Kanıt:

## X+++.2 Cache Riskleri
- [ ] Cache stampede/avalanche sezgisi
  - Kanıt:
- [ ] Warmup/prefill stratejisi
  - Kanıt:

---

# XII++++ (EK) COST / FINOPS KANUNU (DGX VE CLOUD GERÇEĞİ)

## XII++++.1 Cost Model
- [ ] Compute maliyeti (CPU/GPU saat) sezgisi
  - Kanıt:
- [ ] Storage maliyeti (object store + lifecycle) sezgisi
  - Kanıt:
- [ ] Network egress maliyeti sezgisi
  - Kanıt:

## XII++++.2 Optimization Döngüsü
- [ ] Ölç → optimize et → tekrar ölç (latency/throughput/cost)
  - Kanıt:
- [ ] Capacity planning sezgisi (trafik artışı senaryosu)
  - Kanıt:

---

# XIII+++ (EK) PRIVACY / COMPLIANCE KANUNU (UYUM VE İZ)

## XIII+++.1 Access & Audit
- [ ] Data access logging sezgisi (kim neye erişti?)
  - Kanıt:
- [ ] Least privilege + audit bağlantısı
  - Kanıt:

## XIII+++.2 Retention & Deletion
- [ ] Retention policy uygulama stratejisi
  - Kanıt:
- [ ] Data deletion/forget request sezgisi
  - Kanıt:

---

# IV+ (EK) ARCHITECTURE & DOCS KANUNU (MİMARİ KANIT)

## IV+.1 Sistem Diyagramı
- [ ] Basit C4: Context + Container diagram
  - Kanıt:

## IV+.2 ADR (Decision Record)
- [ ] ADR şablonu ile en az 3 karar kaydı
  - Kanıt:

## IV+.3 Operasyon Dokümanı
- [ ] Runbook şablonu + 3 senaryo (deploy, rollback, incident)
  - Kanıt:


---

# XIV. GPU & SCALING (DGX YOLU)

## XIV.1 GPU Temeli
- [ ] VRAM nedir? neden biter?
  - Kanıt:
- [ ] batch size ve memory ilişkisi
  - Kanıt:
- [ ] fp16/bf16 sezgisi
  - Kanıt:

## XIV.2 Distributed Training (Kavram)
- [ ] Data parallelism sezgisi
  - Kanıt:
- [ ] Gradient accumulation sezgisi
  - Kanıt:
- [ ] Checkpoint sharding sezgisi
  - Kanıt:
- [ ] IO bottleneck sezgisi
  - Kanıt:

---

# XIV+ (EK) DGX-READY DISTRIBUTED KANUNU (DDP + NCCL + PROFILING + STATE)

## XIV+.1 DDP Pratiği
- [ ] world_size / rank kavramları
  - Kanıt:
- [ ] torchrun ile çoklu süreç başlatma sezgisi
  - Kanıt:
- [ ] DDP’de sampler ve data sharding sezgisi
  - Kanıt:

## XIV+.2 NCCL ve İletişim Maliyeti
- [ ] all-reduce nedir? neden darboğaz olur?
  - Kanıt:
- [ ] compute vs communication trade-off sezgisi
  - Kanıt:

## XIV+.3 GPU Profiling (Minimum)
- [ ] nvidia-smi ile temel gözlem (mem/util/temps)
  - Kanıt:
- [ ] torch profiler sezgisi (CPU vs CUDA time)
  - Kanıt:
- [ ] Bottleneck: data loader mı model mi? ayırabilme
  - Kanıt:

## XIV+.4 Checkpoint Gerçekleri (Optimizer State)
- [ ] Optimizer state maliyeti sezgisi (Adam vb.)
  - Kanıt:
- [ ] Checkpoint boyutu ve IO maliyeti
  - Kanıt:
- [ ] Checkpoint sıklığı trade-off (güvenlik vs hız)
  - Kanıt:

---

# XV. LLM SYSTEMS (MODERN AI SYSTEM ENGINEER)

## XV.1 Embeddings
- [ ] embedding nedir?
  - Kanıt:
- [ ] cosine similarity ile bağlantı
  - Kanıt:

## XV.2 Vector Store (Kavram → Pratik)
- [ ] indexing sezgisi
  - Kanıt:
- [ ] recall/precision trade-off sezgisi
  - Kanıt:

## XV.3 RAG Pipeline
- [ ] chunking stratejileri
  - Kanıt:
- [ ] retrieval + rerank sezgisi
  - Kanıt:
- [ ] RAG eval harness (offline)
  - Kanıt:

## XV.4 Guardrails & Safety (Ürün Seviyesi)
- [ ] prompt injection sezgisi
  - Kanıt:
- [ ] content filtering sezgisi
  - Kanıt:
- [ ] logging + auditing sezgisi
  - Kanıt:

---

# XV+ (EK) LLM OPS & EVAL KANUNU (PROMPTOPS + EVAL + SERVING)

## XV+.1 PromptOps (Versiyonlama)
- [ ] Prompt versioning standardı (değişiklik kaydı)
  - Kanıt:
- [ ] Prompt change review kuralı (riskli değişiklikte gating)
  - Kanıt:

## XV+.2 LLM Güvenlik Testleri
- [ ] Prompt injection test seti oluşturma
  - Kanıt:
- [ ] Jailbreak denemeleri için “regression suite” sezgisi
  - Kanıt:

## XV+.3 LLM Eval Metrikleri (Task Bazlı)
- [ ] Faithfulness/groundedness sezgisi
  - Kanıt:
- [ ] Hallucination risk ölçümü (pratik sezgi)
  - Kanıt:
- [ ] Offline eval → online metrik eşlemesi
  - Kanıt:

## XV+.4 LLM Serving Sezgisi
- [ ] Token throughput vs latency sezgisi
  - Kanıt:
- [ ] vLLM/Triton gibi serving kavramları (yüksek seviye)
  - Kanıt:
- [ ] Semantic cache sezgisi (ne zaman işe yarar?)
  - Kanıt:

---

# XVI. KAPANIŞ İMTİHANI (CAPSTONE PROOFS)

## XVI.1 Capstone A — End-to-End ML System
- [ ] Dataset oluşturuldu
  - Kanıt:
- [x] Training pipeline çalışıyor
  - Kanıt: proofs/03-ml/repeat-purchase-system.md
- [x] Evaluation pipeline çalışıyor
  - Kanıt: proofs/03-ml/repeat-purchase-system.md
- [x] Serving (API) çalışıyor
  - Kanıt: proofs/03-ml/repeat-purchase-system.md
- [ ] Observability (metrics/logging) var
  - Kanıt:
- [ ] Reproducible runs (seed, config, tracking)
  - Kanıt:

## XVI.2 Capstone B — LLM System (RAG + Eval)
- [ ] Ingestion pipeline
  - Kanıt:
- [ ] Retrieval pipeline
  - Kanıt:
- [ ] Evaluation harness
  - Kanıt:
- [ ] Guardrails minimum
  - Kanıt:
- [ ] Deploy + monitor
  - Kanıt:

## XVI.3 DGX Hazırlık Mührü
- [ ] Multi-GPU planı yazıldı (DDP + checkpoints + IO)
  - Kanıt:
- [ ] Maliyet/performans hesabı yapıldı (temel)
  - Kanıt:
- [ ] Scaling riskleri listelendi (bottleneck planı)
  - Kanıt:
