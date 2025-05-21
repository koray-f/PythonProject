# 📁 classify_utils.py
import torch
import pandas as pd
from datetime import datetime

iletim_kayitlari = []

def classify_and_record(message, ad, telefon, model, tokenizer, label_encoder):
    if len(message) > 200:
        return "⚠️ Lütfen mesajınızı 200 karakteri geçmeyecek şekilde yazınız.", pd.DataFrame(iletim_kayitlari)

    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    inputs = tokenizer(message, return_tensors="pt", truncation=True, padding=True, max_length=96)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()
    label_raw = label_encoder.inverse_transform([pred])[0]
    iletim_kayitlari.append({
        "Ad Soyad": ad,
        "Telefon": telefon,
        "Mesaj": message,
        "İletilen Müdürlük": label_raw,
        "Zaman": now
    })
    sonuc = f"📨 Sayın {ad}, şikayetiniz **{label_raw}** birimine iletilmiştir.\n🕒 Gönderim Zamanı: {now}"
    return sonuc, pd.DataFrame(iletim_kayitlari)