from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route("/")
def homepage():
    return "Welcome to the home page"

@app.route("/add",methods=['POST'])
def addition():
    if request.method=="POST":
        result=int(request.json['num1'])+int(request.json['num2'])
        return jsonify("the summation is {}".format(result))
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)