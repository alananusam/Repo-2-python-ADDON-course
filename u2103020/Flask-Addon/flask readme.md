

Your directory structure for flask should be like:

      /app
          - app_runner.py
          /services
              - app.py 
          /templates
              - mainpage.html
          /static
              /styles
                  - mainpage.css

running flask app

      flask --app hello run
      
 if .py file contains main 
 
            if __name__ == '__main__':
                  app.run()
  then 
  
            python hello.py


## Flask HTTP methods, handle GET & POST requests


Different methods for retrieving data from a specified URL are defined in this protocol. The following table summarizes the different http methods:

 | Request |	Purpose |
 | :---:   | :---:    |
 | GET     |	The most common method. A GET message is send, and the server returns data |
 | POST	   |  Used to send HTML form data to the server. |The data received by the POST method is not cached by the server. |
 | HEAD	   |  Same as GET method, but no response body.|
 | PUT	   |  Replace all current representations of the target resource with uploaded content. |
 | DELETE	 |  Deletes all current representations of the target resource given by the URL. |
 
 
###  create home.html

      <html>
         <body>
            <form action = "/login" method = "post">
               <p>Enter Name:</p>
               <p><input type = "text" name = "nm" /></p>
               <p><input type = "submit" value = "submit" /></p>
            </form>   
         </body>
      </html>

### create file hello.py 

            from flask import Flask, redirect, url_for, request,render_template
            app = Flask(__name__)

            @app.route('/')
            def home():
                return render_template('home.html')

            @app.route('/success/<name>')
            def success(name):
                return 'welcome %s' % name

            @app.route('/login',methods = ['POST', 'GET'])
            def login():
                if request.method == 'POST':
                    user = request.form['nm']
                    return redirect(url_for('success',name = user))

                return redirect(url_for('success',name = user))

            if __name__ == '__main__':
                app.run(debug = True)

## how to render HTML templates?
     
### Step 1:

First, create a new folder in the project directory called templates. Create a new file in the templates folder naming “home.html”.
     
      from flask import Flask, render_template
      app = Flask(__name__)

      @app.route('/')
      def home():
         return render_template('home.html')
      if __name__ == '__main__':
         app.run()
 
 
 ##  Step 2
 
 render css/js in html
 
      <link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/mainpage.css') }}">
      
 optional setting path
 
        TEMPLATE_DIR = os.path.abspath('../templates')
        STATIC_DIR = os.path.abspath('../static')

        # app = Flask(__name__) # to make the app run without any
        app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
