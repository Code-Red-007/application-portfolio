from flask import Flask, render_template
from app.routes import main  

app = Flask(__name__)
app.register_blueprint(main)   

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

