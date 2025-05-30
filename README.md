# 📘 AKILLI BELEDİYE ASİSTANI - PROJE TANITIMI

Bu proje, belediyeye gelen vatandaş şikayet ve taleplerini doğal dil işleme (NLP) teknikleriyle analiz ederek, uygun müdürlüğe otomatik yönlendirmeyi amaçlamaktadır. Model olarak Türkçe BERT (BERTurk) kullanılmıştır. Kullanıcı etkileşimi için Gradio tabanlı bir arayüz geliştirilmiştir.

## 👨‍💻 GELİŞTİREN

**Koray Filazoğlu**  
**Öğrenci No:** 222503304

## 📦 MODÜLER YAPI

- `data_utils.py` → Veriyi yükler, etiketleri işler  
- `model_utils.py` → Tokenizer, model ve Trainer kurulumları  
- `classify_utils.py` → Sınıflandırma ve kayıt işlemleri  
- `app.py` → Arayüz ve kullanıcı girişi / model yükleme  
- `kayitli_model/` → Eğitilmiş model klasörü (otomatik oluşturulur)  
- `guncellenmis_birlesik_belediye_verisi.csv` → Etiketli eğitim verisi  

## 🚀 KULLANIM ADIMLARI

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt

    Modeli eğitin (yalnızca ilk kullanım için):

        İsteğe bağlı olarak train_model.py dosyası oluşturulabilir.

        Alternatif olarak, app.py ilk çalıştırıldığında eğitimi otomatik başlatır.

    Eğitilmiş model mevcutsa yalnızca arayüzü başlatın:

python app.py

Tarayıcıdan aşağıdaki adrese gidin:

    http://127.0.0.1:7861

📤 VERİ GİRİŞİ

Kullanıcı arayüzünde Ad Soyad, Telefon Numarası ve Şikayet bilgileri girilerek işlem yapılır. Model, şikayeti analiz ederek en uygun müdürlüğe yönlendirir. Sonuç kullanıcıya gösterilir ve sistemde kayıt altına alınır.
📌 NOTLAR

    Arayüzde model eğitimi yapılmaz. Eğitilmiş modelin kayitli_model/ klasöründe bulunması gerekir.

    kayitli_model/ klasörü yoksa sistem çalışmaz ve hata verir.

