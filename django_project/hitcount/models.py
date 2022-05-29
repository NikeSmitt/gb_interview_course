from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class HitCount(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='hit_count')
    url = models.CharField(max_length=500)
    count = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.user} : {self.url}'
    
    class Meta:
        unique_together = ('user', 'url')
