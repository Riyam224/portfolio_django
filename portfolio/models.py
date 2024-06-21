from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Post(models.Model):
    title  =  models.CharField(_("title"), max_length=250)
    image  = models.ImageField(_("image"), upload_to='images')
    created_by  = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at "),  auto_now_add=True) 

    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title
