from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "title": "My First Blog Post",
        "subtitle": "This is the subtitle of my first blog post",
        "body": "This is the body of my first blog post. I am learning Flask and it is amazing!",
        "author": "Aryan",
        "date": "May 18, 2026"
    },
    {
        "id": 2,
        "title": "My Second Blog Post",
        "subtitle": "This is the subtitle of my second blog post",
        "body": "This is the body of my second blog post. Flask makes web development so easy!",
        "author": "Aryan",
        "date": "May 18, 2026"
    },
    {
        "id": 3,
        "title": "My Third Blog Post",
        "subtitle": "This is the subtitle of my third blog post",
        "body": "This is the body of my third blog post. I love Python and Flask!",
        "author": "Aryan",
        "date": "May 18, 2026"
    },
]

@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("index.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)