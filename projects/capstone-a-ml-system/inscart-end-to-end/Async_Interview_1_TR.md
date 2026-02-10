**Aşağıdaki cevaplar, e-ticaret senaryosunda tekrar satın alma davranışını tahmin etmeye yönelik uçtan uca bir ML sistemi üzerinden hazırlanmıştır.Bu çalışma, yalnızca model performansını değil; veri akışı, validasyon stratejisi ve iş bağlamı ile birlikte bir ML sisteminin uçtan uca nasıl ele alınabileceğini göstermek amacıyla tasarlanmıştır.**  
**Projenin tamamı, veri akışı ve deney detayları aşağıdaki repoda yer almaktadır:**  
`https://github.com/4F71/instacart-next-product-recommendation`

## SORU

### KISA:/

Yakın zamanda uçtan uca geliştirdiğin bir AI sistemini anlat.  
Problem tanımı, sistem mimarisi, teknik kararların ve kabul ettiğin bir trade-off’a odaklan.

### UZUN:/

Yakın zamanda uçtan uca geliştirdiğin bir AI sistemini anlat.

Lütfen özellikle şunlara odaklan:
- Problem tanımı: Ne çözdün ve neden önemliydi?
- Sistem mimarisi: Ana bileşenler ve veri akışı (yüksek seviyede)
- Teknik kararlar:
  - Model seçimi
  - RAG / retrieval yaklaşımı
  - Agent kullanımı (varsa)
  - Değerlendirme veya doğrulama yöntemi
- Bir trade-off veya kısıt: Bilinçli olarak kabul ettiğin bir sınırlama ve gerekçesi

Okuyucunun senior bir AI engineer olduğunu varsay.  
Cevabı yapılandırılmış, net ve savunulabilir tut.

---

## CEVAP

### UZUN:/

3.4 milyon satırlık bir transactional veri seti üzerinde, müşterilerin **tekrar satın alma davranışını** tahmin eden uçtan uca bir makine öğrenmesi sistemi geliştirdim.

Bu projedeki temel hedefim, hakim olduğum bir domain üzerinde büyük ölçekli ve üretim odaklı bir ML problemine ne kadar etkili şekilde yaklaşabildiğimi değerlendirmekti. İş perspektifinden bakıldığında sistem; tekrar satın alma olasılığı yüksek kullanıcıları tespit ederek stok planlaması ve kişiselleştirme süreçlerini desteklemeyi amaçladı.

Çalışmaya detaylı bir **keşifsel veri analizi (EDA)** süreciyle başladım. Kullanıcı satın alma desenleri, ürün popülerliği ve zamansal davranışlar üzerine elde ettiğim içgörüler, feature engineering kararlarının doğrudan belirleyicisi oldu ve sistemin bel kemiğini oluşturdu.

Modelleme aşamasına geçmeden önce bir baseline benchmark oluşturdum ve veri setinin büyüklüğü ile tabular yapısı nedeniyle **LightGBM** modelini tercih ettim. Bu kararda eğitim hızı, bellek verimliliği ve büyük ölçekli tabular verilerdeki dayanıklılık temel kriterlerdi.

Final model **0.78 F1 skoru** ve **0.91 recall** değerine ulaştı. Recall metriğini önceliklendirdim çünkü tekrar satın alma potansiyeli olan kullanıcıları kaçırmanın maliyeti, false positive üretmekten daha yüksekti. Model performansını user-based GroupKFold ile oluşturulan validation split’leri üzerinde değerlendirdim ve sonuçları yalnızca metriklere göre değil, iş hedefleri bağlamında yorumladım.

Bilinçli olarak kabul ettiğim trade-off ise kapsamlı bir threshold optimizasyonu yapmamaktı. Varsayılan threshold, recall odaklı iş gereksinimlerini zaten karşıladığı için ek optimizasyonun getireceği karmaşıklığın, mevcut iş hedefleri için anlamlı bir fayda üretmeyeceğini değerlendirdim.

---

### KISA:/

3.4 milyon satırlık bir veri seti üzerinde, tekrar satın alma davranışını tahmin eden uçtan uca bir ML sistemi geliştirdim. EDA odaklı feature engineering kullandım ve ölçeklenebilirliği nedeniyle LightGBM tercih ettim. Model 0.78 F1 ve 0.91 recall değerlerine ulaştı ve recall odaklı iş hedefleriyle uyumlu çalıştı. Azalan getiri nedeniyle threshold optimizasyonunu bilinçli olarak sınırlı tuttum.

---

### Sistem Mimarisi (Üst Seviye)

- Veri kaynağı → işlem bazlı satın alma tabloları
- Yükleme & bellek yönetimi → batch yükleme + optimizasyon
- Analiz → EDA ile feature kararları
- Özellik üretimi → batch çalışan feature pipeline
- Model eğitimi → LightGBM (Optuna ile tuning)
- Doğrulama → GroupKFold + leakage kontrolleri
- Çıktı → tekrar satın alma olasılık skorları

> Pipeline’ın detaylı teknik akışı ve deney sonuçları aşağıdaki dokümanda yer almaktadır: 
> [https://github.com/4F71/instacart-next-product-recommendation/blob/main/docs/final_report.md](https://github.com/4F71/instacart-next-product-recommendation/blob/main/docs/final_report.md)

---

## Açıklayıcı / Derinlik Soruları

- EDA sürecinde en etkili bulduğun içgörüler nelerdi ve bunlar feature tasarımını nasıl etkiledi?
- Tekrar satın alma davranışını nasıl tanımladın ve etiketledin?
- Veri sızıntısı (data leakage) riskiyle karşılaştın mı, nasıl önledin?


>Kullanıcı davranışlarına dayalı içgörüleri `Orders` tablosu üzerinden elde ettim. Alışverişlerin gün içinde yoğunlaştığı saatler, haftanın hangi günlerinde daha sık sipariş verildiği ve ayın belirli günlerinde sipariş hacminin artması gibi gözlemler, EDA sürecinde en belirgin sinyalleri verdi. Bu analizler sonucunda, zamansal davranışı yansıtan feature’ların modele daha fazla katkı sağlayacağını gördüm.

>Ürün ve departman bazlı analizlerde, kullanıcıların alışverişlerinin belirli ürün grupları etrafında tekrarlandığını fark ettim. Özellikle `Aisle` ve `Department` tablolarını incelediğimde, temel gıda ağırlıklı alışveriş yapan kullanıcıların tekrar satın almaya daha yatkın olduğunu gördüm. Bu nedenle kategori bazlı feature engineering yaparak modelin daha kontrollü ve anlamlı öğrenmesini hedefledim.

>Feature importance grafiğini incelediğimde, “kullanıcı sipariş sayısı” gibi değişkenlerin diğer tüm feature’ların önüne geçtiğini fark ettim. Detaylı analiz yaptığımda bunun, eğitim setinde hedef siparişin de bu sayıya dahil edilmesinden kaynaklandığını gördüm. Bu durumun veri sızıntısına yol açabileceğini fark ederek, hedefle doğrudan ilişkili veya geleceği ifşa eden bu tür feature’ları eğitim setinden çıkardım.

---

## Modelleme & Karar Soruları

- LightGBM dışında hangi modelleri değerlendirdin ve neden eledin?
- Class imbalance var mıydı? Varsa bunu nasıl ele aldın?
- Bu problemde hangi iş senaryosunda precision, recall’dan daha önemli olurdu?

> LightGBM’i seçmeden önce Logistic Regression ve XGBoost modellerini benchmark testlerine dahil ettim. Veri setinin yaklaşık 3.4 milyon satırdan oluşması nedeniyle model seçiminde hız ve bellek verimliliği önemliydi. Benchmark sonuçlarında LightGBM’in hem eğitim süresi hem de performans açısından daha dengeli bir sonuç verdiğini gördüm ve bu nedenle final model olarak tercih ettim.

>Sınıf dağılımı yaklaşık %60–%40 oranındaydı. Bu dağılım hafif dengesiz olmakla birlikte aşırı bir class imbalance durumu olmadığı için agresif sampling yöntemlerine başvurmadım. Bunun yerine modelin doğal ayrım gücünü koruyarak threshold ve metrik bazlı değerlendirme yapmayı daha sağlıklı buldum.

>E-ticaret senaryosunda, müşterinin satın alacağı ürünü tahmin edememek doğrudan satış kaybı anlamına geliyor. Bu nedenle yanlış negatiflerin maliyeti, yanlış pozitiflere göre daha yüksekti. Bu projede recall’ı önceliklendirdim. Ancak kampanya maliyetlerinin yüksek olduğu veya kullanıcıyı gereksiz bildirimlerle rahatsız etmenin riskli olduğu senaryolarda precision’ın daha kritik hâle geleceğini düşünüyorum.
---

## Değerlendirme & Metrik Soruları

- F1 ve recall dışında hangi metrikleri takip ettin?
- Validation setini nasıl ayırdın? (zaman bazlı vs rastgele)
- %91 recall elde ederken false positive’lerin maliyetini nasıl değerlendirdin?

>F1 ve recall metriklerinin yanında precision ve ROC-AUC değerlerini de takip ettim. F1 skoru modelin genel dengesini görmek için, ROC-AUC ise pozitif ve negatif sınıfları ayırt etme gücünü anlamak için referans oldu. Bu metrikleri birlikte değerlendirerek tek bir metriğe körü körüne bağlı kalmamaya çalıştım.

>Validasyon stratejisi olarak random split yerine user-based GroupKFold kullandım. EDA sürecinde kullanıcıların %60’a varan sadakat oranına ve 7–30 günlük düzenli alışveriş döngülerine sahip olduğunu görmüştüm. Aynı kullanıcının siparişlerini hem eğitim hem test setine koymak, modelin kullanıcı davranışını ezberlemesine yol açacaktı. Kullanıcı bazlı ayrım ile modelin, daha önce hiç görmediği kullanıcılar üzerindeki performansını daha gerçekçi şekilde ölçtüm.

>%91 recall elde ederken false positive’lerin maliyetini özellikle iş tarafında değerlendirdim. Bu senaryoda yanlış bir ürünü önermek, potansiyel bir satışı tamamen kaçırmaktan daha düşük maliyetliydi. Precision değerini kabul edilebilir bir seviyede tutarak, yüksek recall’ın iş açısından anlamlı bir denge sunduğunu gördüm.


---

## Trade-off & Production Soruları

- Bu sistemi production ortamına alacak olsan ilk olarak neyi değiştirirdin?
- Zamanla oluşabilecek data drift veya concept drift’i nasıl tespit ederdin?
- Gerçek zamanlı inference için hangi feature’lar riskli olurdu ve neden?

>Bu sistemi production ortamına alacak olsaydım, ilk olarak feature üretim sürecini netleştirirdim. Eğitim sırasında batch olarak hesaplanan bazı feature’ların, inference anında aynı şekilde üretilemeyeceğini biliyorum. Bu nedenle modelden önce, hangi feature’ların gerçekten production ortamında güvenli ve sürdürülebilir olduğunu belirlemeyi önceliklendirirdim.

>Zamanla oluşabilecek data veya concept drift’i tespit etmek için, model performansını tek başına izlemektense giriş verilerinin dağılımını takip etmeyi tercih ederdim. Özellikle kullanıcı davranışlarını temsil eden temel feature’ların zaman içindeki dağılım değişimleri, model daha bozulmadan önce erken sinyal verebilir. Bu noktada basit istatistiksel kontroller bile ilk aşama için yeterli olurdu.

>Gerçek zamanlı inference senaryosunda, geçmişe dayalı agregasyonlar ve uzun zaman pencereleri kullanan feature’ların riskli olacağını düşünüyorum. Bu tür feature’lar hem gecikmeye neden olur hem de veri tutarlılığı sorunları yaratabilir. Bu nedenle production’da daha kısa zaman pencereli, hesaplanması hızlı ve gecikmeye duyarlı olmayan feature’lara yönelirdim.

---

## Sistem Düşüncesi Soruları

- Bu sistem batch çalışmadan near-real-time bir yapıya geçse mimari nasıl değişirdi?
- Model çıktıları downstream sistemler tarafından nasıl tüketilirdi?
- Sence bu sistemin en kırılgan noktası neresiydi?

>Bu sistem batch çalışmadan near-real-time bir yapıya geçse, mimaride en büyük değişiklik feature üretim katmanında olurdu. Eğitim sırasında batch olarak hesaplanan feature’ların, inference anında daha küçük ve hızlı hesaplanabilir parçalara ayrılması gerekirdi. Modelden çok, veri akışının ve feature tutarlılığının yeniden tasarlanması öncelik olurdu.

>Model çıktılarının downstream sistemler tarafından skor bazlı tüketileceğini düşünüyorum. Bu skorlar doğrudan karar vermek yerine, kampanya tetikleme, sıralama veya önceliklendirme gibi sistemlere girdi olarak kullanılabilirdi. Böylece model tek başına karar veren bir yapı değil, karar destekleyici bir bileşen olurdu.

>Bu sistemin en kırılgan noktası, kullanıcı davranışına dayalı feature’ların zamanla anlamını kaybetme riskiydi. Alışveriş alışkanlıkları değiştiğinde veya kampanya davranışları sistemi etkilediğinde, model performansı fark edilmeden düşebilirdi. Bu nedenle davranış temelli feature’ların sürekli izlenmesi gerektiğini düşünüyorum.

---

## Refleksiyon Soruları

- Bugün yeniden yapsan hangi kararı farklı alırdın?
- Bu proje ML problemlerine yaklaşımını nasıl değiştirdi?
- Bu sistem hangi koşullar altında yanlış veya yanıltıcı çıktılar üretebilir?

>Bugün yeniden yapsaydım, feature setini daha erken sadeleştirirdim. Başta daha fazla feature denedim, ancak sonrasında bunların bir kısmının modele gerçek bir katkı sağlamadığını gördüm. Daha erken bir aşamada sadeleşmek, hem geliştirme süresini hem de riskleri azaltabilirdi.

>Bu proje, ML problemlerine yaklaşımımı daha sistem odaklı hale getirdi. Model performansının tek başına yeterli olmadığını, validation stratejisi, veri sızıntısı ve iş bağlamı gibi unsurların en az model kadar kritik olduğunu daha net gördüm.

>Bu sistem, kullanıcı davranışlarının ani şekilde değiştiği veya geçmiş verinin geleceği temsil etmediği koşullarda yanıltıcı çıktılar üretebilir. Özellikle kampanya yoğunluğu, sezon etkileri veya veri toplama süreçlerindeki değişiklikler, modelin öğrendiği ilişkileri geçersiz kılabilir.