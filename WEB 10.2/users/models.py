from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Додайте додаткові поля профілю, якщо потрібно

    def __str__(self):
        return self.user.username
