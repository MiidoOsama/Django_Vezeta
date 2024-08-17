from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.

TYPE_OF_PERSON = (
    ('M', "Male"),
    ('F', "Female")
)


class Profile(models.Model):
    DOCTOR_IN = (
        ('جلدية' , "جلدية"),
        ('أسنان' , "أسنان"),
        ('نفسي' , "نفسي"),
        ('أطفال حديثي الولادة' , "أطفال حديثي الولادة"),
        ('مخ و أعصاب' , "مخ و أعصاب"),
        ('عظام' , "عظام"),
        ('نساء و توليد' , "نساء و توليد"),
        ('أنف وأذن و حنجرة' , "أنف وأذن و حنجرة"),
        ('قلب و أوعيه دموية' , "قلب و أوعيه دموية"),
        ('أمراض دم' , "أمراض دم"),
        ('أورام' , "أورام"),
        ('باطنة' , "باطنة"),
        ('تخسيس و تغذية' , "تخسيس و تغذية"),
        ('جراحة أطفال' , "جراحة أطفال"),
        ('جراحة أورام' , "جراحة أورام"),
        ('جراحة أوعيه دموية' , "جراحة أوعيه دموية"),
        ('جراحة تجميل' , "جراحة تجميل"),
        ('جراحة سمنة ومناظير' , "جراحة سمنة ومناظير")
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_("الاسم"),max_length=80)
    surname = models.CharField(_("اللقب"),max_length=50)
    who_i = models.TextField(_("من انا ") , max_length=50)
    price = models.IntegerField(_("سعر الكشف ") , blank=True, null=True)
    image = models.ImageField(_("الصورة الشخصية") , upload_to='profile' , blank=True , null=True)
    slug = models.SlugField(_("slug") , blank=True, null=True)
    subtitle = models.CharField(_("نبذة"), max_length=80)
    doctor = models.CharField(_("دكتور"), max_length=50 , choices=DOCTOR_IN)
    specialist_doctor = models.CharField(_("التخصص  "), max_length=80 ,default='' ,blank=True , null=True)
    address= models.CharField(_("المحافظة"), max_length=50)
    address_detail = models.CharField(_("العنوان "), max_length=80)
    waiting_time = models.IntegerField(_("مدة الانتظار") , blank=True , null= True)
    working_hours = models.IntegerField(_("ساعات العمل ") , blank=True , null=True)
    number_phone = models.CharField(_("رقم التليفون  ") , max_length=20)
    facebook = models.CharField(max_length=100, blank=True , null=True)
    twitter = models.CharField(max_length=100, blank=True , null=True)
    google = models.CharField(max_length=100, blank=True , null=True)
    joined = models.DateTimeField(_("وقت الانضمام ") , auto_now_add=True , blank=True , null=True)
    sex = models.CharField(_("النوع"), choices=TYPE_OF_PERSON , max_length=50)





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

# def created_profile (sender , **kwargs):
#     Profile.objects.create(user=kwargs['instance'] )


@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
post_save.connect(created_profile, sender=User)