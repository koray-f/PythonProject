# 📁 app.py
from data_utils import load_and_prepare_data
from model_utils import tokenize_data, setup_model_and_trainer
from classify_utils import classify_and_record
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import gradio as gr
import os

# 🔁 Modeli yeniden eğitmek yerine varsa yükle
model_path = "kayitli_model"

csv_path = "guncellenmis_birlesik_belediye_verisi.csv"
df, label_encoder = load_and_prepare_data(csv_path)

if os.path.exists(model_path):
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
else:
    model_name = "dbmdz/bert-base-turkish-cased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenized = tokenize_data(df, tokenizer)
    model, tokenizer, trainer = setup_model_and_trainer(tokenized, label_encoder, model_name)
    trainer.train()
    model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)

# 🎛 Arayüz
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Akıllı Belediye Asistanı")
    gr.Markdown("**Hazırlayan:** Koray Filazoğlu - 222503304  \nBu sistem vatandaşların mesajlarını **BERTurk** modeliyle eğitilmiş özel bir sınıflandırıcı ile analiz eder ve ilgili müdürlüğe yönlendirir.")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 👤 Vatandaş Bilgi Girişi")
            ad = gr.Textbox(label="Ad Soyad", placeholder="Adınızı ve soyadınızı girin")
            telefon = gr.Textbox(label="Telefon", placeholder="İletişim numaranız")
            mesaj = gr.Textbox(label="Talep / Şikayet", lines=4, placeholder="Şikayetinizi en fazla 200 karakterle yazınız.")
            gonder = gr.Button("Şikayeti Gönder")
            geri = gr.Textbox(label="📬 Geri Bildirim", lines=4, interactive=False)

        with gr.Column(scale=2):
            gr.Markdown("### 🏢 Müdürlük Tarafında Görüntüleme Paneli")
            tablo = gr.Dataframe(
                headers=["Ad Soyad", "Telefon", "Mesaj", "İletilen Müdürlük", "Zaman"],
                value=None,
                interactive=False
            )

    gonder.click(
        fn=lambda m, a, t: classify_and_record(m, a, t, model, tokenizer, label_encoder),
        inputs=[mesaj, ad, telefon],
        outputs=[geri, tablo]
    )

if __name__ == "__main__":
    demo.launch(server_port=7861)