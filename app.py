from flask import Flask, render_template, redirect, url_for
import requests


app = Flask(__name__)

# Функция для получения случайной цитаты
def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        response.raise_for_status()
        data = response.json()
        return data["content"], data["author"]
    except requests.exceptions.RequestException as e:
        return "Не удалось загрузить цитату.", None

# Маршрут главной страницы
@app.route('/')
def index():
    quote, author = get_random_quote()
    return render_template('index.html', quote=quote, author=author)

# Обновление цитаты
@app.route('/new_quote')
def new_quote():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
