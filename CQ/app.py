from flask import Flask, render_template, request
from question_bank import question_list

app = Flask(__name__)



# View function for the index route
@app.get("/")
def index():
    return render_template("index.html")

# View function for the quiz route
@app.get("/quiz")
def quiz_page():
    return render_template("quiz.html", questions = question_list)

# View function for the submit action route
@app.post("/submit")
def submit_results():
    # Individual answers from from
    answer_1 = request.form[question_list[0]["text"]]
    answer_2 = request.form[question_list[1]["text"]]
    answer_3 = request.form[question_list[2]["text"]]
    answer_4 = request.form[question_list[3]["text"]]
    answer_5 = request.form[question_list[4]["text"]]
    answer_6 = request.form[question_list[5]["text"]]
    answer_7 = request.form[question_list[6]["text"]]
    answer_8 = request.form[question_list[7]["text"]]
    answer_9 = request.form[question_list[8]["text"]]
    answer_10 = request.form[question_list[9]["text"]]

    score = 0

    # Check if answers are correct and increase the score
    if answer_1 == question_list[0]["answer"]:
        score += 1
    
    if answer_2 == question_list[1]["answer"]:
        score += 1
    
    
    if answer_3 == question_list[2]["answer"]:
        score += 1
    
    if answer_4 == question_list[3]["answer"]:
        score += 1
    
    if answer_5 == question_list[4]["answer"]:
        score += 1
    
    if answer_6 == question_list[5]["answer"]:
        score += 1
    
    if answer_7 == question_list[6]["answer"]:
        score += 1
    
    if answer_8 == question_list[7]["answer"]:
        score += 1
    
    if answer_9 == question_list[8]["answer"]:
        score += 1
    
    if answer_10 == question_list[9]["answer"]:
        score += 1
    
    return render_template("results.html", score = score)
