'''
Web applications
    - Flask
    - Jinja2
    - SQLAlchemy
'''

'''
1) Flask
    - framework de Python (lightweight) folosit pentru a construi site-uri/aplicatii web
    - ne ajuta cu urmatoarele functionalitati:
        a) sa legam URL-urile de continutul care trebuie afisat pe site
        b) sa colectam date dintr-un formular
        c) sa ne conectam la o baza de date
        d) sa generam pagini html pe baza datelor si template-urilor

    Instalare:
    pip install flask

    Concept cheie:
    route - reprezinta un URL care este legat de o functie in Python

    Exemplu aplicatie basic cu flask:
        from flask import Flask
        app = Flask(__name__) # initializeaza aplicatia

        @app.route("/") # cand cineva aceseaza root-ul URL-ului http://localhost:5000/ se va executa functia
        def home():
            return "Hello, Flask!"

        if __name__ == "__main__":
            app.run(debug=True) # ruleaza aplicatia in modul debug si o reinitializeaza automat cand modificam codul

    Template-uri HTML in Flask:
    - pentru a nu scrie codul nostru HTML in Python, Flask foloseste
      folderul "templates" pentru a tine fisierele HTML separat

    Exemplu:
        - cream folderul "templates/" in aceeasi locatie cu aplicatia noastra Flask
        - in interiorul ei ne definim primul fisier HTML -> index.html

            <h1>Hello, Flask!</h1>

        - in codul din aplicatia noastra Python il folsim in felul urmator:
            @app.route('/hello') # http://localhost:5000/hello
            def hello():
                return render_template('index.html')

    Gestionarea formularelor / Handling Forms:
    - putem primi ca si input date si sa gestionam informatia in functie de metoda (GET, POST, PUT ...)

    Exemplu:
        - form.html contine codul html pentru formularul nostru si metoda cu care transmite informatia
            <form method="POST">
                <input name="username" />
                <button type="submit">Go</button>
            </form>

        - in codul nostru python facem o ruta si o functie care vor gestiona formularul
            from flask import request

            @app.route("/form", methods=["GET", "POST"])
            def form():
                if request.method == "POST":
                    username = request.form["username"]
                    return f"Hello {username}"
                return render_template("form.html")
                                                                '''


'''
2) Jinja2
    - ne ajuta sa scriem cod asemanator cu Python in HTML

    Ne ofera urmatoarele posibilitati:
        - variabile: {{ name }}

        - if statements:
            {% if age > 18 %}
                <p>Adult</p>
            {% endif %}

        - bucle:
            {% for student in students %}
                <p> {{ student }} </p>
            {% endfor %}

        - filtre:
            {{ name|upper }} <!-- il scrie cu litere mari -->
'''


'''
3) SQLAlchemy
    - Biblioteca din Python care ne ajuta sa conectam aplicatioa noastra din Flask cu o baza de date
    - Nu face parte din pachetul de baza, asa ca trebuie instalata:
        pip install flask_sqlalchemy

    ORM = Object Relational Mapper => ne ajuta sa interactionam cu baze de date folosing obiecte
        - practic, vom avea un obiect care va fi mapat la tabela din baza noastra de date
            => pentru fiecare camp din tabela, vom avea un atribut in clasa noastra
            => pentru interactiunea cu baza de date (create, read, update, query) avem metode

    Avantaje:
        - conexiunea si salvarea modificarilor in baza de date sunt realizate de catre biblioteca
        - avem la dispozitie comenzile de baza pentru interactiunea cu baza de date si nu mai suntem
          nevoiti sa rulam manual comenzile SQL
        - totul este scris direct in Python

    Setup:
        from flask_sqlalchemy import SQLAlechemy

        app = Flask(__name__)
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///<nume_fisier>.db"
        db = SQLAlchemy(app)

    Definirea unui Model - o clasa care va deveni o tabela in baza de date

    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))
        grade = db.Column(db.Float)

    Crearea tabelei:

    with app.app_context():
        db.create_all()

    Metode de baza pentru interactiunea cu baza de date:
    - Adaugare element in baza de date:
    new_student = Student(name="Alice", grade=9.5)
    db.session.add(new_student)
    db.session.commit()

    - Interogare baza de date:
    students = Student.query.all() # returneaza toti studentii din baza de date

    - Update element in baza de date:
    student = Student.query.get(1) # returneaza studentul cu id-ul
    student.grade = 10
    db.session.commit()

    - Stergere element din baza de date:
    student = Student.query.get(1)
    db.session.delete(student)
    db.session.commit()

    - Pentru a face query-uri mai complexe, putem folosi metodele de filtrare:
    students = Student.query.filter(Student.grade > 9).all() # returneaza toti studentii cu nota mai mare de 9
    students = Student.query.filter(Student.name == "Ionescu").all() # returneaza studentii cu numele 'Ionescu'
    student = Student.query.filter(Student.name == "Ionescu").first() # returneaza primul student cu numele 'Ionescu'
'''


# from flask import Flask, request, render_template, redirect, url_for
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return '''
#     <h1>Hello, Flask!</h1>
#     <h2>Habar n-am</h2>'''


# @app.route('/hello') # http://localhost:5000/hello
# def hello():
#     return render_template('index.html')


# @app.route('/home')
# def home_page():
#     return render_template('index_header_body.html')


# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         prenume = request.form.get('prenume', '')
#         nume = request.form.get('nume', '')
#         varsta = request.form.get('varsta', '')
#         print(f'Prenume: {prenume}, Nume: {nume}, Varsta: {varsta}')
#         return redirect(url_for('form'))
#     return (render_template('index_form.html'))


# @app.route('/form/return_home', methods=['GET', 'POST'])
# def form_return_home():
#     if request.method == 'POST':
#         prenume = request.form.get('prenume', '')
#         nume = request.form.get('nume', '')
#         varsta = request.form.get('varsta', '')
#         print(f'Prenume: {prenume}, Nume: {nume}, Varsta: {varsta}')
#         return redirect(url_for('welcome'))
#     return (render_template('index_form_return_home.html'))


# @app.route('/welcome')
# def welcome():
#     return render_template('welcome.html')


# ### Jinja starts here
# @app.route('/hello/<name>')
# def hello_name(name):
#     return render_template('index_name.html', name=name)


# @app.route('/hello/<name>/<age>') # /hello/Daniel-Neamtiu/35 -> name = Daniel-Neamtiu / age = 35
# def hello_name_age(name, age):
#     firstname = name.split('-')[0]
#     lastname = name.split('-')[1]
#     return render_template('index_name_age.html', firstname=firstname, lastname=lastname, age=age)

# from flask import session
# app.config['SECRET_KEY'] = 'dev-scret-key'


# @app.route('/jinja_form', methods=['GET', 'POST'])
# def jinja_form():
#     if request.method == 'POST':
#         session['last_form_data'] = {
#             'prenume': request.form.get('prenume', ''),
#             'nume': request.form.get('nume', ''),
#             'varsta': request.form.get('varsta', '')
#         }
#         return redirect(url_for('jinja_form'))

#     submitted_data = session.pop('last_form_data', None)
#     return render_template('jinja_form.html', submitted_data=submitted_data)


# @app.route('/jinja_for')
# def jinja_for():
#     my_list = ['Daniel', 'Mariana', 'Ionel']
#     return render_template('jinja_for.html', names=my_list)


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
db = SQLAlchemy(app)


class Student(db.Model):
    cnp = db.Column(db.String(13), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    students = db.session.query(Student).all()
    return render_template('home_sql_alchemy.html', students=students)


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        cnp = request.form.get('cnp')
        name = request.form.get('name')
        grade = request.form.get('grade')
        new_student = Student(cnp=cnp, name=name, grade=grade)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add_sql_alchemy.html')


@app.route('/update', methods=["GET", "POST"])
def update():
    if request.method == "POST":
        cnp = request.form.get('cnp')
        grade = request.form.get('grade')
        student = db.session.query(Student).get(cnp)
        student.grade = grade
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_sql_alchemy.html')


@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        cnp = request.form.get('cnp')
        student = db.session.query(Student).get(cnp)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('delete_sql_alchemy.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
