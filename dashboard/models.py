from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)

    # bytes
    addition_bytes = models.IntegerField(default=100)
    subtraction_bytes = models.IntegerField(default=100)
    algebra_bytes = models.IntegerField(default=100)
    multiplication_bytes = models.IntegerField(default=100)
    division_bytes = models.IntegerField(default=100)

    # Total Questions Done
    addition_questions = models.IntegerField(default=0)
    subtraction_questions = models.IntegerField(default=0)
    algebra_questions = models.IntegerField(default=0)
    multiplication_questions = models.IntegerField(default=0)
    division_questions = models.IntegerField(default=0)

    def __totalbytes__(self):
        return self.addition_bytes + self.subtraction_bytes + self.multiplication_bytes + self.division_bytes + self.algebra_bytes

    def __totalQuestions__(self):
        return self.addition_questions + self.subtraction_questions + self.multiplication_questions + self.division_questions + self.algebra_questions


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
