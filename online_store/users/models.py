from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


def user_directory_path(instance, file_name):
    return f'users/{instance.user.username}/avatar/{file_name}'


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_directory_path, verbose_name='avatar', blank=True, null=True)
    phone = models.CharField(max_length=12, verbose_name='phone')
    balance = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='balance', default=0)
    username = models.CharField(max_length=10, verbose_name='username')

    def __str__(self):
        return self.user.username

    def image_tag(self):
        if self.avatar:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.avatar.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Avatar'

    def restore_email(self):
        pass

    class Meta:
        verbose_name = 'profile user'
        verbose_name_plural = 'profiles users'
