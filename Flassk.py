from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"
@app. route ( '/')
def home():
    return 'Welcome to the Home Page!'
# Route 2: About Page
@app.route('/Page1')
def about():
    return render_template('home.html')
# Route 3: Contact Page
@app.route('/submit')
def contact():
    return 'Contact us at contact@example.com'

if __name__ =='__main__':
    app.run(debug=True)