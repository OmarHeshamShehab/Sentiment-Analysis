# app.py
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open("model/sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)


def analyze_sentiment(text):
    # Use the model to predict the sentiment of the input text
    prediction = model.predict([text])[0]
    return "Positive" if prediction == 1 else "Negative"


@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = ""
    if request.method == "POST":
        user_text = request.form["text"]
        sentiment = analyze_sentiment(user_text)
    return render_template("index.html", sentiment=sentiment)


if __name__ == "__main__":
    app.run(debug=True)
