import graphene

from .models import User
from .types import UserType
from .mutations import CreateAccountMutation, LoginMutation
from .queries import resolve_user, resolve_users


class Query(object):
    users = graphene.List(UserType, page=graphene.Int(), resolver=resolve_users)
    user = graphene.Field(
        UserType, id=graphene.Int(required=True), resolver=resolve_user
    )


class Mutation(object):
    create_account = CreateAccountMutation.Field()
    login = LoginMutation.Field()
