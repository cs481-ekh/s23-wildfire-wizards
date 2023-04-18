from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.urls import path
from django.http import HttpResponseRedirect
from FPA_FOD_PLUS.models import Data

class CsvUploadAdmin(admin.ModelAdmin):
    change_list_template = 'admin_panel/change_list.html'
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('csv_upload/', self.admin_site.admin_view(self.csv_upload_view), name='csv_upload'),
        ]
        return custom_urls + urls

    def csv_upload_view(self, request):
        return HttpResponseRedirect(reverse('csv_upload'))

    def csv_upload_button(self, obj):
        return format_html('<a class="button" href="{}">Upload CSV</a>', reverse('admin:csv_upload'))

    csv_upload_button.short_description = 'CSV Upload'
    csv_upload_button.allow_tags = True

    actions = [csv_upload_button]

admin.site.unregister(Data)
admin.site.register(Data, CsvUploadAdmin)

