import graphene
from graphene_django import DjangoObjectType
from graphene_django.fields import DjangoConnectionField

from .models import Feed


class FeedObject(DjangoObjectType):
    class Meta:
        model = Feed
        interfaces = [graphene.Node]


class FeedQuery(graphene.ObjectType):
    feed = graphene.Node.Field(FeedObject)
    feeds = DjangoConnectionField(FeedObject, first=graphene.Int(default_value=5))

    def resolve_feeds(self, info, **kwargs):
        return Feed.objects.select_related(
            'user', 'user__profile'
        ).prefetch_related('feed_set').filter(parent=None)


class FeedInput(graphene.InputObjectType):
    post = graphene.String(required=True)


class CreateFeed(graphene.Mutation):
    class Arguments:
        feed = FeedInput(required=True)

    ok = graphene.Boolean()
    feed = graphene.Field(lambda: FeedObject)

    @staticmethod
    def mutate(root, info, feed):
        feed = Feed.objects.create(user=info.context.user, post=feed.post)
        return CreateFeed(feed=feed, ok=True)
