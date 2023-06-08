from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.full_name


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return str(self.id)


class EventHistory(models.Model):
    id = models.AutoField(primary_key=True)
    subscription_id = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.type

class SendMessage(models.Model):
    body = models.TextField(255)

    def _str_(self):
        return self.body
