from flask import *
import db

app = Flask(__name__)

@app.route("/")
def index():
    returnrender_template("index.html")

@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        #ユーザー名が被ってなければ
        if db.get_user_by_name(username) == None:
            db.add_user(username, password)
            session["username"] = username
            return render_template("index.html", username = session["username"])
    return render_template("create.html")

@app.route("/tweet", method=["POST","GET"])
def tweet():
    if request.method == "POST":
        text = request.form["text"]
        db.add_tweet(0, text)
    tweets = db.get_all_tweets()
    return render_template("timeline.html", tweets = tweets)


app.secret_key = 'qawsedrftghujikolp'
    
if __name__ == "__main__":
    app.run(debug=True)
    
