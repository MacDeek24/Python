from flask import Flask, render_template, redirect, url_for,request
from post import Post
import smtplib
import requests
import os

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/1ac01907ebe604250043").json()

OWN_EMAIL = os.environ.get("email")
OWN_PASSWORD = os.environ.get("pass")


post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)



@app.route('/')
def default_route():
    return redirect(url_for('get_all_posts'))

@app.route('/home')
def get_all_posts():
    return render_template("index.html", all_posts=posts )

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact" , methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_no = request.form["phoneno"] 
        message = request.form["msg"]
        send_email(name, email, phone_no, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)



if __name__ == "__main__":
    app.run(debug=True)