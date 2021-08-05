import graphene
from rooms import schema as rooms_schema
from users import schema as user_schema


class Query(user_schema.Query, rooms_schema.Query, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
