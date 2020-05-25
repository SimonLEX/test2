from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''<!DOCTYPE HTML><html>
  <head>
    <title>Flask app</title>
  </head>
  <body>
    <h1>Hello Flask!</h1>
  </body>
</html>'''


if __name__=="__main__":
    app.run()