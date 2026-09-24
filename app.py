
'''from flask import Flask

app = Flask(__name__)#app intialization

@app.route('/')
def vyshnavi():
    return 'Welcome back to bonda vlogs'


if __name__ == '__main__':
    app.run() 
'''

'''from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my Flask application'

@app.route('/admin')
def admin():
    return 'this is a admin'

@app.route('/student')
def student():
    return 'this is a student'

@app.route('/staff')
def staff():
    return 'this is staff'

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    elif name == 'student':
        return redirect(url_for('student'))
    elif name == 'staff':
        return redirect(url_for('staff'))
    else:
        return 'Invalid user'

if __name__ == '__main__':
    app.run(debug=True)

'''


'''from flask import  Flask
app = Flask(__name__)
@app.route("/hello")
def hello():
    return "Hello,Welcome to back to bonda vlogs"

@app.route("/")
def index():
    return "Namesthe nenu mee vyshnavi"

if __name__ =="__main__":
    app.run(debug=True)

'''

#runtime input 
'''
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def yshu(name):
    return 'Welcom back to bonda vlog my dear '+name

if __name__ == '__main__':
    app.run(debug = True)

'''


'''from flask import Flask
app = Flask(__name__)
@app.route('/hello/<int:sub>')
def vyshu(sub):
    return 'please subscribe=%d' % sub

if __name__ == '__main__':
    app.run(debug = True)'''

'''
from flask import Flask
app = Flask(__name__)

def yshu():
    return 'please subscribe'
app.add_url_rule('/yshu/','yshu',yshu)  #/yshu/     → URL path
#'yshu'     → endpoint name
#yshu       → function to execute

if __name__ == '__main__':
    app.run(debug = True)
    '''

'''
from flask import *
app = Flask(__name__)
@app.route('/')
def message():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug = True)
'''


from flask import *
app = Flask(__name__)
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name},POST request received"
    return render_template('base.html')
if __name__ == '__main__':
    app.run(debug = True) 
