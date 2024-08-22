from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from ..models.author import Author


authors_app = Blueprint("authors_app", __name__)

@authors_app.route("/authors/", endpoint='list')
def users_list():
    authors=Author.query.all()
    return render_template("authors/list.html", authors=authors)

# @users_app.route("/users/<int:user_id>/", endpoint='details')
# def user_details(user_id:int):
#     user=User.query.filter_by(id=user_id).one_or_none()
#     print(user)
#     if user is None:
#         raise NotFound(f'User #{user_id} doesn`t exist!')
#
#     return render_template("users/details.html", user=user)