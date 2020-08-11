from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/trably/blog/blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Database %r>' % self.id

@app.route('/')
def index():
    return render_template("root.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/pinguin')
def pinguin():
    return render_template("pinguin.html")

@app.route('/create-article',methods=['POST','GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        article = Database(title = title, intro=intro, text=text)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return "АШЫБКА "+ e.__class__
    else:
        return render_template("create-article.html")


if __name__ == "__main__":
    app.run(debug=True)