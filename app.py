from flask import Flask,render_template,request

import ML_MODEL as m

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def ML_MODEL():
    mks = None 
    if request.method=="POST":
        hrs=int(request.form["hrs"])
        marks_pred=m.marks_prediction(hrs)
        mks=marks_pred
        
    return render_template("index.html",my_marks=mks)




# @app.route("/submit",methods=['POST'])
# def submit():
#     #html->python
#     if request.method=="POST":
#         name=request.form["username"]
    
#     #python ->html
#     return render_template("submit.html",n=name)


if __name__=="__main__":
    app.run(debug=True)