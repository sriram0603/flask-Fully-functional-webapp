
from flask import render_template, request, Blueprint
from basic.models import Post
main= Blueprint('main', __name__)

@main.route("/")
def hello():
	page= request.args.get('page', 1,type=int)
	post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template("home.html",posts=post)



@main.route("/about")
def about():
	about="about"
	return render_template("about.html",title="About")

