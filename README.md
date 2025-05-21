📘 AKILLI BELEDİYE ASİSTANI - PROJE TANITIMI

Bu proje, belediyeye gelen vatandaş şikayet ve taleplerini doğal dil işleme (NLP) teknikleriyle analiz eder ve doğru müdürlüğe otomatik olarak yönlendirir. Model olarak Türkçe BERT (BERTurk) kullanılmıştır. Arayüz Gradio ile oluşturulmuştur.

👨‍💻 GELİŞTİREN:
Koray Filazoğlu - 222503304

📦 MODÜLER YAPI:
- data_utils.py        → Veriyi yükler, etiketleri işler
- model_utils.py       → Tokenizer, model, trainer kurulumları
- classify_utils.py    → Sınıflandırma ve kayıt işlemleri
- app.py               → Arayüz ve kullanıcı girişi / model yükleme
- kayitli_model/       → Eğitilmiş model klasörü (otomatik oluşturulur)
- guncellenmis_birlesik_belediye_verisi.csv → Etiketli eğitim verisi

🚀 KULLANIM ADIMLARI:

1. GEREKLİ KÜTÜPHANELERİ YÜKLE:
   pip install -r requirements.txt

2. MODELİ EĞİT (bir kez):
   - train_model.py (isteğe bağlı olarak hazırlanabilir)
   - veya app.py ilk kez çalıştırıldığında eğitimi otomatik yapar

3. KAYITLI MODEL VARSA SADECE ARAYÜZÜ BAŞLAT:
   python app.py

4. Arayüz açıldığında `http://127.0.0.1:7861` adresine gidin.

📤 VERİ GİRİŞİ:
Kullanıcı Adı, Telefon ve Şikayet girilerek şikayet ilgili müdürlüğe yönlendirilir. Sonuç arayüzde gösterilir ve kayıt paneline eklenir.

📌 NOT:
- Arayüzde model eğitimi yapılmaz. Eğitilmiş model `kayitli_model/` içinde yer almalıdır.
- `kayitli_model` klasörü yoksa sistem hata verir.


