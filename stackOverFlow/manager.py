from datetime import datetime
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    # def create_user(self, email, password, **extra_fields):
    #     if not email:
    #         raise ValueError("Email is Required")
        
    #     email = self.normalize_email(email)
    #     extra_fields.setdefault('is_active',True)
    #     user = self.model(email = email,**extra_fields)
    #     user.set_password(password)
    #     user.save(using = self.db)
    #     return user
    
    def create_superuser(self , email , password , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff if false')
        
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        return user
    
   