from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

@app.route('/student',methods=['GET','POST'])
def  student_page_response():
    if request.method == 'GET':
        return render_template('student.html')
    else:
        name = request.form["fname"]
        return render_template('greeting.html',name=name)
if __name__ == '__main__':
app.run(debug = True,port=5001)