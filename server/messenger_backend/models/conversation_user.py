from django.db import models

from . import utils
from .user import User
from .conversation import Conversation


class ConversationUser(utils.CustomModel):
    unread = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(
        User,
		on_delete=models.CASCADE,
		db_column="userId",
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        db_column="conversationId",
    )