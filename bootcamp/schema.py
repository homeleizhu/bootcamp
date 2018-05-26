import graphene

from .feeds.schema import FeedQuery, CreateFeed
from .authentication.schema import UserQuery, CreateToken


class Query(FeedQuery, UserQuery, graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    create_feed = CreateFeed.Field()
    create_token = CreateToken.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
