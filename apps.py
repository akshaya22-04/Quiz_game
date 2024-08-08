from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

quiz_questions =[
    {
        "question" : " Which of the following is used for single line comment in python?",
        "options" : ["#", "/", "\\", "*"],
        "answer" : "#"
    },
    {
        "question" : "how many types of inheritance in python ?",
        "options" : ["Two", "three", "Four", "five"],
        "answer" : "Five"
    },
    {
        "question" : "which one of the following is a variable in python ?",
        "options" : ["for", "while", "Bool", "a"],
        "answer" : "a"
    },
    {
        "question" : "print(2 ** 3 ** 2)",
        "options" : ["64", "512", "8", "16"],
        "answer" : "512"
    },
    {
        "question" :"which of the following is not a python data type?",
        "options" : ["List", "Tuple", "Array", "Dictionary"],
        "answer" : "Array"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answers = request.form
        score = 0
        for i, question in enumerate(quiz_questions):
            if question['answer'] == answers.get(f'question-{i}'):
                score += 1
        return redirect(url_for('result', score=score))
    return render_template('quiz.html', questions=quiz_questions, enumerate = enumerate)

@app.route('/result')
def result():
    score = request.args.get('score', 0, type=int)
    return render_template('result.html', score=score, total=len(quiz_questions))

if __name__ == '__main__':
    app.run(debug=True)
