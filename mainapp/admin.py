from django.contrib import admin
from image_cropping import ImageCroppingMixin
from mainapp.models import ModelExample


class ModelExampleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(ModelExample, ModelExampleAdmin)
