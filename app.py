from flask import Flask,request,redirect
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.String(200),nullable=False)

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        inputTitle = request.form['taskTitle']
        inputContent = request.form['taskContent']

        db.session.add(Todo(title=inputTitle,content=inputContent))
        db.session.commit()
        return redirect('/')
    else:
        todos = Todo.query.all()
        return render_template('index.html',todos=todos)

@app.route("/delete/<int:id>")
def delete(id):
    db.session.delete(Todo.query.get_or_404(id))
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
