# 🧠 Fine-Tuning BERT for Question Answering (SQuAD v2.0)

This project focuses on building a **Question Answering System** by fine-tuning **BERT** and **BiDAF** models on the **SQuAD v2.0** dataset. After evaluating both models, **BERT** emerged as the superior model for answering complex questions with contextual accuracy.

---

## 🌟 Key Features
- **Dataset**: Leveraged **SQuAD v2.0** for training, which includes answerable and unanswerable questions.
- **Model Comparison**: Fine-tuned and evaluated **BERT Base** and **BiDAF**.
- **Deployment**: Deployed the fine-tuned BERT model locally using **Flask**.

---

## 🌐 Demo
Here’s a snapshot of the deployed web application:

<img width="1440" alt="Screenshot 2025-01-06 at 9 34 17 PM" src="https://github.com/user-attachments/assets/412c3b61-f0dc-45d0-aae9-492ede26887e" />


---

## 🔄 Workflow
1. **Data Preprocessing**:
   - Cleaned the dataset to remove inconsistencies.
   - Tokenized text using BERT with `[CLS]` and `[SEP]` tokens.
2. **Model Training**:
   - Fine-tuned both **BERT Base** and **BiDAF** using optimal configurations.
3. **Evaluation**:
   - Compared the performance of both models.
4. **Deployment**:
   - Deployed the fine-tuned **BERT model** as a local web service.

---

## 📈 Results Summary
- **BERT Base**:
  - Achieved higher accuracy and better handling of unanswerable questions.
- **BiDAF**:
  - Competitive but limited by its architecture compared to BERT's transformer-based design.

💡 **Conclusion**: **BERT Base** is the preferred model for question-answering tasks.

---

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/question-answering-system.git
   cd question-answering-system

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Flask app:
   python app.py

4. Open your browser and access the local application
5. The best Model weights are saved in my drive please access the link here and move the weigths to /Project/.
