from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.urls import reverse
from .views import csv_upload

from .models import Data

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    search_fields = ['FOD_ID',]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('csv_upload/', self.admin_site.admin_view(csv_upload), name='csv_upload'),
        ]
        return custom_urls + urls

    def csv_upload_button(self, obj):
        return format_html('<a class="button" href="{}">Upload CSV</a>', reverse('admin:csv_upload'))

    csv_upload_button.short_description = 'CSV Upload'
    csv_upload_button.allow_tags = True

    actions = [csv_upload_button]

admin.site.register(Data, DataAdmin)