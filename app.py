from flask import Flask, render_template
from data import Articles
from data import Warmane
app = Flask(__name__)
app.debug=True

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/warmane')
def warmane():
    return render_template('warmane.html', data = Warmane())
    #return render_template('warmane.html', data = Warmane(), name = Guildname())


@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)


if __name__ == '__main__':
    #Guildname()
    app.run()
