from django.db import models
from django.db.models import signals
from django.urls import reverse
# from .tasks import task_video_duration


class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(
        ("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(
        ("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    def __str__(self):
        return self.name
    

class Bookmark(models.Model):
    bookmark_id=models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    time_of_bookmark= models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(
        ("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    course_id = models.AutoField(primary_key=True, editable=False)
    # slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    keywords = models.ManyToManyField(Keyword)
    video_trailer = models.FileField(upload_to='trailer/', blank=False, null=False)
    # sections = models.ForeignKey(Section, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Category")
    price= models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    discounted_price = models.IntegerField(null=True)
    new_price = models.IntegerField(null=True)
    created_at = models.DateTimeField(
        ("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    @property
    def discounted_price(self):
        return ((self.price) * (self.discount) / 100)
    
    @property
    def new_price(self):
        return (self.price) - (self.discounted_price)

    def __str__(self):
        return self.name
    


class Section(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    # videos = models.ForeignKey('Video', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Course")
    created_at = models.DateTimeField(
        ("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    def __str__(self):
        return self.name
    


class Video(models.Model):
    video_id = models.AutoField(primary_key=True, editable=False)
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    keywords = models.ManyToManyField(Keyword)
    video_width = models.CharField(max_length=150,editable=False, null=True)
    video_height = models.CharField(max_length=150,editable=False, null=True)
    duration = models.CharField(max_length=150,editable=False, null=True)
    thumbnail_light = models.ImageField(upload_to ='thumbnails/thumbnails_light/',blank=True, null=True)
    thumbnail_dark = models.ImageField(upload_to='thumbnails/thumbnails_dark/', blank=True, null=True)
    video_file = models.FileField(null=False, blank=False)
    video_file_2k = models.FileField(upload_to='videos/mp4_resized_2k/', null=True, blank=True)
    video_file_fullhd = models.FileField(upload_to='videos/mp4_resized_fullhd/',null=True, blank=True)
    video_file_hd = models.FileField(upload_to='videos/mp4_resized_hd/', null=True, blank=True)
    video_file_480 = models.FileField(upload_to='videos/mp4_resized_480p/', null=True, blank=True)
    video_file_360 = models.FileField(upload_to='videos/mp4_resized_360p/', null=True, blank=True)
    video_file_240 = models.FileField(upload_to='videos/mp4_resized_240p/', null=True, blank=True)
    video_file_144 = models.FileField(upload_to='videos/mp4_resized_144p/',null=True, blank=True)
    # subtitle=models.FileField(upload_to="subtitles/", null=True, blank=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Course")
    section = models.ForeignKey(Section, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Lesson Section")
    category = models.ManyToManyField(Category)
    # is_active = models.BooleanField(
    #     verbose_name=_("Video visibility"),
    #     help_text=_("Change video visibility"),
    #     default=True,
    # )
    bookmarks = models.ForeignKey(Bookmark, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Bookmarks")
    is_completed = models.BooleanField(default=False, verbose_name="Is Completed")
    created_at = models.DateTimeField(
        ("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = ("Video")
        verbose_name_plural = ("Videos")

    def get_absolute_url(self):
        return reverse("store:video_detail", args=[self.slug])

    def __str__(self):
        return self.title




# def video_post_save(sender, instance, signal, *args, **kwargs):
#     if not instance.duration:
#         from .tasks import task_video_duration, task_video_dimensions, task_video_encoding_2k, task_video_encoding_1080p, task_video_encoding_720p, task_video_encoding_480p, task_video_encoding_360p, task_video_encoding_240p

#         task_video_dimensions.delay(instance.pk)
#         task_video_duration.delay(instance.pk)
#         task_video_encoding_2k.delay(instance.pk)
#         task_video_encoding_1080p.delay(instance.pk)
#         task_video_encoding_720p.delay(instance.pk)
#         task_video_encoding_480p.delay(instance.pk)
#         task_video_encoding_360p.delay(instance.pk)
#         task_video_encoding_240p.delay(instance.pk)

# signals.post_save.connect(video_post_save, sender=Video)