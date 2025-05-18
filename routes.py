from flask import Blueprint, render_template, request
import sqlite3
import requests

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Fetch Weather Data
    api_key = "d4145b245aeb45b74dc840bca63c8f20"
    city = "London,UK"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if 'main' in data and 'weather' in data:
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    else:
        weather = {
            'city': city,
            'temperature': 'N/A',
            'description': 'Weather data not available'
        }

    # Fetch Quote of the Day
    quote_response = requests.get("https://zenquotes.io/api/random")
    quote_data = quote_response.json()

    if isinstance(quote_data, list) and 'q' in quote_data[0] and 'a' in quote_data[0]:
        quote = {
            'text': quote_data[0]['q'],
            'author': quote_data[0]['a']
        }
    else:
        quote = {
            'text': "No quote available right now. Try again later!",
            'author': ""
        }

    return render_template('index.html', weather=weather, quote=quote)


@main.route('/blogs')
def blogs():
    return render_template('blogs.html')

@main.route('/education')
def education():
    return render_template('education.html')

@main.route('/projects')
def projects():
    return render_template('projects.html')

@main.route('/resources')
def resources():
    return render_template('resources.html')

@main.route('/values')
def values():
    return render_template('values.html')

@main.route('/cookies')
def cookies():
    return render_template('cookies.html')

@main.route('/privacy')
def privacy():
    return render_template('privacy.html')

@main.route('/admin')
def admin():
    return render_template('admin.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form.get('message')   

        conn = sqlite3.connect('signup.db')
        cursor = conn.cursor()

   
        cursor.execute('INSERT INTO subscribers (name, email, message) VALUES (?, ?, ?)', (name, email, message))
        conn.commit()
        conn.close()

        return "Thank you for subscribing!"

    return render_template('signup.html')

@main.route('/subscribers', methods=['GET', 'POST'])
def view_subscribers():
    if request.method == 'GET':
        return render_template('admin_login.html')

    password = request.form.get('password')
    if password != 'ItIsBetterToGiveitago7':
        return render_template('admin_login.html', error="Incorrect password.")

    conn = sqlite3.connect('signup.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscribers")
    subscribers = cursor.fetchall()
    conn.close()

    return render_template('subscribers.html', subscribers=subscribers)
