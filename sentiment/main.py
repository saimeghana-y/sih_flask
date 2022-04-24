from flask import Flask, request, render_template,jsonify
from textblob import TextBlob

app = Flask(__name__)
def do_something(text1):
   return TextBlob(text1).sentiment.polarity
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    combine = do_something(text1)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)