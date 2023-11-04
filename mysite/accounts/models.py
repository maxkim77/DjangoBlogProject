from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()

#User 모델확장 - UserProfile
#일대일관계 UserProfile 모델의 user 필드는 models.OneToOneField(User,on_delete=models.CASCADE)를 사용
#User 모델과 일대일 관계형성
#시그널:
#@receiver(post_save, sender=User) 데코레이터와 연결된 함수 'created_or_update_profile'는 'User'모델의 인스턴스가 저장 될때 마다 실행
#if created: User 인스턴스가 생성될때 UserProfile 인스턴스 생성
#User 객체가 업데이트 될때마다 User Porfile 정보 업데이트