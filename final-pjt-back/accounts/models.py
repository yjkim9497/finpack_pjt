from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=255, unique=True, null=False)
    email = models.EmailField(db_index=True, unique=True, null=False)
    age = models.TextField(default='',null=False)
    asset = models.TextField(default='')
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = [
        # 'username',
        'email',
        'age'
    ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username

# class UserManager(BaseUserManager):
#     # 일반 user 생성
#     def create_user(self, email, username, age, asset, password=None):
#         if not email:
#             raise ValueError('must have user email')
#         if not age:
#             raise ValueError('must have user age')
#         if not username:
#             raise ValueError('must have user name')
#         user = self.model(
#             email = self.normalize_email(email),
#             username = username,
#             age = age,
#             asset = asset
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     # 관리자 user 생성
#     def create_superuser(self, email, username, age, asset, password=None):
#         user = self.create_user(
#             email,
#             password = password,
#             username=username,
#             age=age,
#             asset=asset
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
#     email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
#     age = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
#     asset = models.EmailField(default='', max_length=100, null=True, blank=True, unique=False)
    
#     # User 모델의 필수 field
#     is_active = models.BooleanField(default=True)    
#     is_admin = models.BooleanField(default=False)
    
#     # 헬퍼 클래스 사용
#     objects = UserManager()

#     # 사용자의 username field는 nickname으로 설정
#     USERNAME_FIELD = 'username'
#     # 필수로 작성해야하는 field
#     REQUIRED_FIELDS = ['email', 'password', 'age']

#     def __str__(self):
#         return self.username
