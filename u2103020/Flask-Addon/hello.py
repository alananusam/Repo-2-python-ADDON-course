from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

#base root 
@app.route('/')
def hello_world():
   return 'Hello World'

#path or url hello
@app.route('/hello')
def hello():
    return 'Hello World-path hello'
#url with name as argument to get function
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
# url with datatype int
@app.route('/post/<username>/<int:post_id>')
def show_post(username,post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
# adding more than one path
@app.route('/greeting')
@app.route('/greeting/<name>')
def hello_greeting(name=None):
    return render_template('greeting.html', name=name)

@app.route('/new')
def hello_new():
    return render_template('index.html') 

from flask import request

@app.route('/student',methods=['GET','POST'])
def  student_page_response():
    if request.method == 'GET':
        return render_template('student.html')
    else:
        name = request.form["fname"]
        return render_template('welcome.html',name=name)
if __name__ == '__main__':
    app.run(debug = True)
    

