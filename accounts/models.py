from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
# Create your models here.

sex = (
    ('Male', 'Male'), 
    ('Female', 'Female')
)
marital_status = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced')
)
academic_qualifications = (
    ('O Level', 'O Level'),
    ('BSC', 'BSC'),
    ('MSC', 'MSC'),
    ('PHD', 'PHD'),
)
session = (
    ('Morning (10am)', 'Morning (10am)'),
    ('Afternoon (10am)', 'Afternoon (10am)')
)
disability = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    sex = models.CharField(choices = sex, max_length = 12)
    Dob = models.DateField(default = timezone.now)
    place_of_birth = models.TextField()
    marital_status = models.CharField(choices = marital_status, max_length = 30)
    course = models.CharField(max_length = 250)
    contact_address = models.TextField()
    phone = models.CharField(max_length = 11)
    academic_qualifications = models.CharField(choices = academic_qualifications, max_length = 20)
    next_of_kin = models.CharField(max_length = 200)
    next_of_kin_phone = models.CharField(max_length = 11)
    session = models.CharField(choices = session, max_length = 40)
    disability = models.CharField(choices = disability, max_length = 5)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user) + ' profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)







