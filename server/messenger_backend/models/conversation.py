from django.db import models
from django.db.models import Q, Count

from . import utils
from .user import User


class Conversation(utils.CustomModel):

    users = models.ManyToManyField(User, through="ConversationUser")
    createdAt = models.DateTimeField(auto_now_add=True, db_index=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # find conversation given an array of user ids
    def find_conversation(userIds):
        # return conversation or None if it doesn't exist
        try:
            # first query only conversations with userIds in the array
            query = Q()
            for user in userIds:
                query &= Q(users__in=userIds)
            filter = Conversation.objects.filter(query)
            # then only get the one with the same number of users
            return filter.annotate(count=Count("users")).get(count=len(userIds))
        except Conversation.DoesNotExist:
            return None
