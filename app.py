from flask import Flask,render_template,request
from datetime import datetime

app=Flask(__name__)
@app.route("/")
def index():
    return "Welcome"

@app.route("/hello")
def hello():
    naam="Ujjwal"
    data=[["Student","Class","Grade"],
         ["Ram",9,9],
         ["Shyam",8,9],
         ["Ravi",9,7]]
    colors=["red","green","blue"]
    return render_template("tes.html",name=naam,now=datetime.now(),data=data,colors=colors)

@app.route("/form",methods=['GET','POST'])
def submit_data():
	if request.method=='GET':
		return render_template("form.html")
	else:
		name=request.form.get('name')
		clas=request.form.get('class')
		image=request.files.get('image')
		ext=image.filename.split('.')[-1]
		image.save("static/images/{}.{}".format(name,ext))
		print(request.form)
		return "Your name is {} and class is {}".format(name,clas)

if __name__=="__main__":
           app.run(port=8000,use_reloader=True,debug=True)