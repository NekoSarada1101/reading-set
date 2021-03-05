from django.db import models


class User(models.Model):
    mail = models.CharField("メールアドレス", max_length=255)
    password = models.CharField("パスワード", max_length=255)
    name = models.CharField("ユーザー名", max_length=255, default="user")

    def __str__(self):
        return self.mail
