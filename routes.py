from app import app
from flask import render_template, redirect, url_for, request, flash

messages = []

@app.route('/')     #пишу функцию для главной страницы
def main_page():
    return render_template('index.html')

@app.route('/about', methods=['GET','POST'])     #пишу функцию для главной страницы
def about():
    if request.method == 'POST':
        name = request.form['username']
        phone = request.form['phone']
        email = request.form['email']

        if not name:
            flash('Поле "Имя" обязательно!')
        elif not phone:
            flash('Поле "Телефон" обязательно!')
        else:
            messages.append({'username': name,
                             'email': email,
                             'phone': phone})
            return redirect(url_for('main_page'))
        print(name, phone, email)

    return render_template('about.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', user_messages=messages)