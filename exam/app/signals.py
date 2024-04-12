# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import CustomUser, Student, Teacher
# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.status == CustomUser.Status.Student:
#             Student.objects.create(user=instance)
#         elif instance.status == CustomUser.Status.Teacher:
#             Teacher.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.status == CustomUser.Status.Student:
#         instance.students.save()
#     elif instance.status == CustomUser.Status.Teacher:
#         instance.teachers.save()
