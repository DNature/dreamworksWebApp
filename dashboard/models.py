from django.db import models

# Create your models here.

course_type = (
    ('PDF', 'PDF'),
    ('Video', 'Video'),
)

# course category
class Course_Category(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Categories'


    def __str__(self):
       return self.name


# course materials
class Course_Materials(models.Model):
    title = models.CharField(max_length = 100)
    category = models.ForeignKey(Course_Category, on_delete = models.CASCADE, related_name='category')
    course_type = models.CharField(max_length = 10, choices =course_type)
    download_link = models.URLField()
    latest = models.BooleanField(default=False)

    class Meta:
        ordering = ['-title']
        verbose_name = 'Course Material'
        verbose_name_plural = 'Course Materials'

    def __str__(self):
        return self.title


