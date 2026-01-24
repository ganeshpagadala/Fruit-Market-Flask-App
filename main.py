from flask import Flask, render_template, request, redirect
from database.utility import getFruits

app = Flask(__name__)


@app.route('/')
def search_fruit():
    return render_template('index.html')

# view all fruits 
@app.route('/fruits',methods=['GET','POST'])
def fruits():
    if request.method == 'POST':
        search_fruit = request.form['fruitname']
        # get fruit list based on search from db
        fruits = getFruits(fruitname = search_fruit)

    fruits = getFruits()
    #if request method is get
    return render_template('fruits.html',fruits=fruits)



# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/login', methods= ['GET','POST'])
# def login():
#     if request.method == 'POST':
#         #geting data from browser
#         pass
#         return render_template('login.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')


if __name__ == "__main__":
    app.run(debug = True, port = 5005)
