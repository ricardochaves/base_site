from django.db import models

from image_cropping import ImageRatioField

# Create your models here.


class ModelExample(models.Model):
    title = models.CharField(max_length=70, verbose_name='Title', default='', blank=True)
    image = models.ImageField(blank=True, upload_to='uploaded_images', verbose_name='Image')
    cropping = ImageRatioField('image', '430x360', verbose_name='Crop Image')
    active = models.BooleanField(verbose_name="Active", default=False)
