from flask import Blueprint
from strawberry.flask.views import GraphQLView
from app.schema import schema

graphql_bp = Blueprint("graphql", __name__)

graphql_bp.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema)
)
