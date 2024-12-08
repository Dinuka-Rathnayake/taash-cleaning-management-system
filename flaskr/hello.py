from flask import Flask
from flask import url_for
from flask import render_template

from livereload import Server



app = Flask(__name__)

@app.route('/')
def index():
  #return "Home Page"
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/hello')
def hello():
  return 'Hello Dinuka'

#using url for 
@app.route('/user/<username>')
def profile(username):
  return f'{username}\'s profile'

# run through liverload
if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()