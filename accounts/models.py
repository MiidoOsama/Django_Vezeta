from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_("الاسم"),max_length=500)
    who_i = models.TextField(_("من انا ") , max_length=50)
    price = models.IntegerField(_("سعر الكشف ") , blank=True, null=True)
    image = models.ImageField(_("الصورة الشخصية") , upload_to='profile' , blank=True , null=True)
    slug = models.SlugField(_("slug") , blank=True, null=True)
    subtitle = models.CharField(_("نبذة"), max_length=80)
    doctor = models.CharField(_("دكتور"), max_length=50)
    specialist_doctor = models.CharField(_("التخصص  "), max_length=80 ,default='' ,blank=True , null=True)
    address= models.CharField(_("المحافظة"), max_length=50)
    address_detail = models.CharField(_("العنوان "), max_length=80)
    waiting_time = models.IntegerField(_("مدة الانتظار") , blank=True , null= True)
    working_hours = models.IntegerField(_("ساعات العمل ") , blank=True , null=True)
    number_phone = models.CharField(_("رقم التليفون  ") , max_length=20)
    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

def created_profile (sender , **kwargs):
    Profile.objects.create(user=kwargs['instance'] )

post_save.connect(created_profile, sender=User)