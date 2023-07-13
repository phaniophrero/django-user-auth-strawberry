import datetime
import strawberry
from typing import List
from .models import Category, Keyword, Video, Section, Course


@strawberry.django.type(Category)
class CategoryType:
    name: str


@strawberry.django.type(Keyword)
class KeywordType:
    name: str


@strawberry.django.type(Course)
class CourseType:
    course_id: int
    name: str
    description: str
    keywords: List[str]
    video_trailer: str
    category: str
    price: int
    discount: int
    discounted_price: int
    new_price: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


@strawberry.django.type(Section)
class SectionType:
    name: str
    course: str


@strawberry.django.type(Video)
class VideoType:
    video_id: int
    slug: str
    title: str
    description: str
    duration: str
    video_width: str
    video_height: str
    video_file: str
    video_file_2k: str
    video_file_fullhd: str
    video_file_hd: str
    video_file_480: str
    video_file_360: str
    video_file_240: str
    video_file_144: str
    thumbnail_light: str
    thumbnail_dark: str
    course: str
    section: str
    category: str
