from flask import Flask , render_template, request, jsonify
from chat import get_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.get("/predict")
def index_get():
    return render_template("base.html")
    
@app.post("/predict") 
def predict():
    text=request.get_json().get("message")
    #TODO check if text is valid
    response =get_response(text)
    messege={"answer": response}
    return jsonify(messege)



if __name__=="__main__":
    app.run(debug=True)    