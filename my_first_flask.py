from flask import Flask, request, jsonify, render_template

# Создаем приложение
app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    # Исправлено на index.html, так как он лежит в папке templates
    return render_template('index.html', prediction_text="")

# Логика обработки формы
@app.route('/predict', methods=['GET','POST'])
def predict():
    # Получаем текст из поля с именем 'description'
    # ВНИМАНИЕ: в нашем красивом HTML поле называлось 'content'. 
    # Нужно либо в HTML сменить name="content" на name="description", 
    # либо здесь изменить на request.form.get('content')
    a_description = request.form.get('description') 
    return render_template('index.html', prediction_text=a_description)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
