from sqlite3 import IntegrityError

from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user, login_user
from werkzeug.exceptions import NotFound

from ..models import Author, Tag
from ..models.article import Article
from ..forms.article import CreateArticleForm
from ..models.database import db

articles_app = Blueprint("articles_app", __name__)


@articles_app.route("/articles/", endpoint='list')
def article_list():
    articles=Article.query.all()
    for article in articles:
        print('article.author', article.author)
    return render_template("articles/list.html", articles=articles)

@articles_app.route("/articles/<int:article_id>/", endpoint='details')
def article_details(article_id:int):
    article=Article.query.filter_by(id=article_id).one_or_none()
    if article is None:
        raise NotFound(f'Article #{article_id} doesn`t exist!')

    return render_template("articles/details.html", article=article)

@articles_app.route("/articles/create", methods=['GET', 'POST'], endpoint='create')
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices=[(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if request.method == "POST" and form.validate_on_submit():
        if current_user.author:
            author=Author.query.filter_by(user_id=current_user.id).one_or_none()
            author_id=author.id
        else:
            author=Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            author_id = author.id
        article = Article(author_id=author_id, title=form.title.data.strip(), body=form.body.data)
        if form.tags.data:
            selected_tags=Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)
        db.session.add(article)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article"
        else:
            return redirect(url_for("articles_app.details", article_id=article.id))
    return render_template("articles/create.html", form=form, error=error)