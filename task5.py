from flask import Flask, request

app = Flask(__name__)


# @app.route('/')
# @app.route('/index')
# def index():
#     return "Привет, Яндекс!"
#
#
# @app.route('/list_prof/<list>')
# def form_sample(list):
#     return render_template('/static/profession.html', list=list)


# @app.route('/sample_file_upload', methods=['POST', 'GET'])
# def sample_file_upload():
#     if request.method == 'GET':
#         return f'''<!doctype html>
#                         <html lang="en">
#                           <head>
#                             <meta charset="utf-8">
#                             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#                              <link rel="stylesheet"
#                              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
#                              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
#                              crossorigin="anonymous">
#                             <title>Пример загрузки файла</title>
#                           </head>
#                           <body>
#                             <h1>Загрузим файл</h1>
#                             <form method="post" enctype="multipart/form-data">
#                                <div class="form-group">
#                                     <label for="photo">Выберите файл</label>
#                                     <input type="file" class="form-control-file" id="photo" name="file">
#                                 </div>
#                                 <button type="submit" class="btn btn-primary">Отправить</button>
#                             </form>
#                           </body>
#                         </html>'''
#     elif request.method == 'POST':
#         f = request.files['file']
#         print(f.read())
#         return "Форма отправлена"


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h3 align="center">на участие в миссии</h3>
                            <div>
                                <form method="post" enctype="multipart/form-data">
                                <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Общее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        {''.join(map(lambda x: f'<div class="form-check"><input class="form-check-input" type="checkbox" value="{x[1]}" name="profession" id="{x[0]}"><label class="form-check-label" for="{x[0]}">{x[1]}</label></div>', ((0, 'пилот'), (1, 'метеоролог'), (2, 'врач'), (3, 'инженер-исследователь'), (4, 'инженер-строитель'), (5, 'инженер по радиационной защите'), (6, 'инженер по жизнеобеспечению'), (7, 'экзобиолог'))))}
                                     <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите фото</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['sex'])
        print(request.form['accept'])
        f = request.files['file']
        print(f.read())
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
