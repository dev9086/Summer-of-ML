from flask import Flask,render_template,request
from model import train_models

app = Flask(__name__)

cf_model,cc_model = train_models(r"C:\Users\KRISHNA\Downloads\final_cccf.csv")

@app.route("/",methods=["GET","POST"])
def home():
  result = None
  equation = None
  if request.method == "POST":
    rating = float(request.form["rating"])
    direction  = request.form["direction"]
    
    if direction=="cf_from_cc":
      predicted = cf_model[0] + cf_model[1] * rating
      equation = f"Codeforces = {cf_model[0]:.2f} + {cf_model[1]:.2f} * Codechef"
      result = f"Predicted CodeChef rating: {predicted:.0f}"
    else:
      predicted = cc_model[0] + cc_model[1] * rating
      equation = f"Codechef = {cc_model[0]:.2f} + {cc_model[1]:.2f} * Codeforces"
      result = f"Predicted CodeChef rating: {predicted:.0f}"
      
  
  return render_template("index.html",result = result,equation = equation)
  
if __name__ =="__main__":
  app.run(debug=True) 