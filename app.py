from flask import Flask
app=Flask(__name__)
#Router 
@app.route("/")
def hello_world():
    return "Hello word"
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
