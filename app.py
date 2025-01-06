from flask import Flask, request, render_template, jsonify
from transformers import BertTokenizer, BertForQuestionAnswering
from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

app = Flask(__name__)

# Load the DistilBERT model and tokenizer
model_path = 'saved_qa_model_bert'
model = DistilBertForQuestionAnswering.from_pretrained(model_path)
tokenizer = DistilBertTokenizer.from_pretrained(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.json
    context = data.get('context')
    question = data.get('question')

    if not context or not question:
        return jsonify({'error': 'Context and question are required'}), 400

    inputs = tokenizer.encode_plus(question, context, return_tensors='pt')
    input_ids = inputs['input_ids'].tolist()[0]

    outputs = model(**inputs)
    answer_start_scores, answer_end_scores = outputs.start_logits, outputs.end_logits

    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1

    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end])
    )

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
