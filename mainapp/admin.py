from django.contrib import admin

from django_invisible_recaptcha_admin.admin import my_admin
from mainapp.models import ModelExample

from image_cropping import ImageCroppingMixin


class ModelExampleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


my_admin.register(ModelExample, ModelExampleAdmin)
