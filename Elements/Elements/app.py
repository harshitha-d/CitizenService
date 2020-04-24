from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.router()
def hello():
message = "hello"
return render_template('index.html', message)

if __name__=="__main__":
app.run(debug=True)
