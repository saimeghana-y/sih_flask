from flask import Flask, render_template, request, url_for, Response ,jsonify

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def do_something(text1):
   return TextBlob(text1).sentiment.polarity

@app.route('/summarize', methods=['POST'])
def summarize():
    text1 = request.form['input-text']
    print(text1)
    combine = do_something(text1)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route("/audioSummary")
def audio_summary():
    pass

@app.route("/videoSummary")
def video_summary():
    pass

@app.route("/pdfSummary")
def pdf_summary():
    pass

@app.route("/articleSummary")
def article_summary():
    pass