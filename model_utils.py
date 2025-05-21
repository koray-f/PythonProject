# 📁 model_utils.py
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

def tokenize_data(df, tokenizer, max_len=96):
    dataset = Dataset.from_pandas(df[["text", "labels"]])

    def tokenize(batch):
        return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=max_len)

    tokenized = dataset.map(tokenize, batched=True)
    tokenized.set_format("torch", columns=["input_ids", "token_type_ids", "attention_mask", "labels"])
    return tokenized

def setup_model_and_trainer(tokenized, label_encoder, model_name="dbmdz/bert-base-turkish-cased"):
    split = tokenized.train_test_split(test_size=0.1, seed=42)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(label_encoder.classes_))
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    training_args = TrainingArguments(
        output_dir="./results",
        logging_dir="./logs",
        eval_strategy="steps",
        save_strategy="steps",
        eval_steps=200,
        save_steps=200,
        logging_steps=200,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        num_train_epochs=3,
        learning_rate=2e-5,
        warmup_ratio=0.1,
        weight_decay=0.01,
        save_total_limit=1,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        report_to="none"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=split["train"],
        eval_dataset=split["test"]
    )

    return model, tokenizer, trainer