import datetime
import strawberry
from strawberry.file_uploads import Upload
from typing import List
from .types import CategoryType, KeywordType,VideoType, SectionType, CourseType
from .models import Category, Keyword, Video, Section, Course



@strawberry.type
class Query:
    @strawberry.field
    def categories(self) -> List[CategoryType]:
        return Category.objects.all()
    
    @strawberry.field
    def category(self, pk: int) -> CategoryType:
        if pk == pk:
            category = Category.objects.get(pk=pk)
            return category

    
    @strawberry.field
    def keywords(self) -> List[KeywordType]:
        return Keyword.objects.all()
    

    @strawberry.field
    def keyword(self, pk: int) -> KeywordType:
        if pk == pk:
            keyword = Keyword.objects.get(pk=pk)
            return keyword
    

    @strawberry.field
    def courses(self) -> List[CourseType]:
        return Course.objects.all()

    @strawberry.field
    def course(self, course_id: int) -> CourseType:
        if course_id == course_id:
            course = Course.objects.get(course_id=course_id)
            return course


    @strawberry.field
    def sections(self) -> List[SectionType]:
        return Section.objects.all()
    
    @strawberry.field
    def section(self, pk: int) -> SectionType:
        if pk == pk:
            section = Section.objects.get(pk=pk)
            return section
        

    @strawberry.field
    def videos(self, category: str = None) -> List[VideoType]:
        if category:
            videos = Video.objects.filter(category=category)
            return videos
        return Video.objects.all()

    @strawberry.field
    def video(self, slug: str) -> VideoType:
        # videos_category = Video.objects.filter(category=category)
        # if category:
        if slug == slug:
            video = Video.objects.get(slug=slug)
            return video

    @strawberry.field
    def video_by_id(self, video_id: int) -> VideoType:
        if video_id == video_id:
            video = Video.objects.get(pk=video_id)
            video_id = video.video_id
            return video


@strawberry.type
class Mutation:
    @strawberry.field
    def create_category(self, name: str) -> CategoryType:
        category = Category(name=name)
        category.save()
        return category
    

    @strawberry.field
    def create_keyword(self, name: str) -> KeywordType:
        keyword = Keyword(name=name)
        keyword.save()
        return keyword


    @strawberry.field
    def create_course(self, name: str, description: str, keywords: float, video_trailer: str, category: str, price: int, discount: int, discounted_price: int, new_price: int, created_at: datetime.datetime, updated_at: datetime.datetime) -> CourseType:
        course = Course(name=name, description=description, keywords=keywords, video_trailer=video_trailer, category=category, price=price, discount=discount, discounted_price=discounted_price, new_price=new_price, created_at=created_at, updated_at=updated_at)
        course.save()
        return course
    

    @strawberry.field
    def create_section(self, name: str, course: str) -> SectionType:
        section = Section(name=name, course=course)
        section.save()
        return section


    @strawberry.field
    def create_video(self, slug: str, title: str, description: str, video_file: Upload, video_file_2k: str, video_file_fullhd: str, video_file_hd: str, video_file_480: str, video_file_360: str, video_file_240: str, video_file_144: str, duration: str, video_width: str, video_height: str, thumbnail_light: str, thumbnail_dark: str, course: str, section: str, category: str) -> VideoType:

        video = Video(slug=slug, title=title, description=description,
                      video_file=video_file, video_file_2k=video_file_2k, video_file_fullhd=video_file_fullhd, video_file_hd=video_file_hd, video_file_480=video_file_480, video_file_360=video_file_360, video_file_240=video_file_240, video_file_144=video_file_144,
                      duration=duration,
                      video_width=video_width,
                      video_height=video_height,
                      thumbnail_light=thumbnail_light,
                      thumbnail_dark=thumbnail_dark,
                      course=course,
                      section=section,
                      category=category)
        
        video.save()
        return video



    @strawberry.field
    def update_video(self, video_id: int, slug: str, title: str, description: str, video_file: str, thumbnail_light: str, thumbnail_dark: str, category: str) -> VideoType:
        video = Video.objects.get(video_id=video_id)
        video.slug = slug
        video.title = title
        video.description = description
        video.video_file = video_file
        thumbnail_light=thumbnail_light
        thumbnail_dark=thumbnail_dark
        video.category = category
        video.save()
        return video
    
    @strawberry.field
    def update_is_video_completed(self, video_id: int, is_completed: bool) -> VideoType:
        video = Video.objects.get(video_id=video_id)
        video.is_completed = is_completed
        video.save()
        return video


    @strawberry.field
    def delete_video(self, video_id: int) -> bool:
        video = Video.objects.get(video_id=video_id)
        video.delete
        return True


# schema = strawberry.Schema(query=Query, mutation=Mutation)
