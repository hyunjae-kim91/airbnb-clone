from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """Conversations Model Defintion"""

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for users in self.participants.all():
            usernames.append(users.username)
        return ", ".join(usernames)

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"


class Message(core_models.TimeStampedModel):

    """Message Model Definition"""

    messages = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    Conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says {self.messages}"
