from django.db import models


class feedback(models.Model):
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.email
