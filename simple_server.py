from flask import Flask
import webbrowser
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#https://auth0.com/blog/developing-restful-apis-with-python-and-flask/


@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/terry")
def hello_world2():
  return "goodbye!"
    

if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5001/')
    app.run(port=5001)