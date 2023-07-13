import strawberry
from typing import List
from .models import CustomUser
import datetime

@strawberry.django.type(CustomUser)
class CustomUserType:
    id: int
    email: str
    first_name: str
    last_name: str
    profile_image: str
    date_of_birth: str
    phone: str
    country: str
    city: str
    zip_code: str
    is_active: bool
    is_admin: bool
    is_staff: bool
    is_superuser: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_login: datetime.datetime

