from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethdView
from tumblood.models imprt Post, Comment

posts = Blueprint('posts',__name__,template_folder='template')


class ListView(methodView):
    def get(self):
        posts = posts.objects.all()
        return render_template('posts/list.html',posts=posts)

class DetailView(MethodView):
    def get(self,slug):
        post =Post.object.get_or_404(slug=slug)
        return render_template('posts/detail.html',post=post)

#registring the urls
posts.add_url_rule('/',view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>/',view_func=DetailView.as_view('detail'))
