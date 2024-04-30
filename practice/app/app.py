from flask import Flask, render_template, request

app = Flask(__name__)

# Sample Q&A data
qa_data = {
    "What is your name?": "My name is ChatGPT.",
    "What is 2 + 2?": "The result of 2 + 2 is 4.",
    "Who is the president of the United States?": "I'm sorry, I'm not updated with current events."
}

@app.route('/')
def index():
    return render_template('index.html', qa_data=qa_data)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    answer = qa_data.get(question, "Sorry, I don't know the answer to that question.")
    return render_template('index.html', question=question, answer=answer, qa_data=qa_data)

if __name__ == '__main__':
    app.run(debug=True)
