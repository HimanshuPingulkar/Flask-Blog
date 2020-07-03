from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Himanshu Pingulkar',
        'title': 'Flask Tutorial',
        'content': 'In depth tutorial',
        'date_posted': '3 July, 2020'
    },
    {
        'author': 'Anonymous',
        'title': 'Flask Tutorial',
        'content': 'In depth tutorial',
        'date_posted': '3 July, 2025'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    # name = request.args.get("name", "World")
    # return f'<h1>Hello, {escape(name)}!</h1><hr>'
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    # return '<h1>About Page</h1>'
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)