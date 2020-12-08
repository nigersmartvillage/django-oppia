
from django.contrib import admin

from av.models import UploadedMedia, UploadedMediaImage


class UploadedMediaAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'file',
                    'created_date',
                    'md5',
                    'length',
                    'title',
                    'organisation',
                    'license')


class UploadedMediaImageAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'image',
                    'uploaded_media',
                    'default_image',
                    'created_date')


admin.site.register(UploadedMedia, UploadedMediaAdmin)
admin.site.register(UploadedMediaImage, UploadedMediaImageAdmin)
