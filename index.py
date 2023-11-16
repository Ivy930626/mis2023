from flask import Flask,render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")

def index():
	X = "<h1>資管二A 411147013 謝棨亘</h1>"
	X += "<a href=/myself>關於我自己</a><br>"
	X += "<a href=/interest>興趣何倫碼測驗結果</a><br>"
	X += "<a href=/work>最有興趣的MIS相關工作</a><br>"
	X += "<a href=/about>未來規劃</a><br>"
	return X

@app.route("/myself")
def myself():
	return render_template("myself.html")
	
@app.route("/interest")
def interest():
	return render_template("interest.html")

@app.route("/work")
def work():
	now = datetime.now()
	return render_template("work.html")

@app.route("/about")
def about():
	return render_template("about.html")



#if __name__ == "__main__":
	#app.run()