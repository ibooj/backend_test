from django.contrib import admin

from sms_handler.models import ApiLog


class AdminApiLog(admin.ModelAdmin):
    list_display = ('created', 'msg')

    def __init__(self, model, admin_site):
        super(AdminApiLog, self).__init__(model, admin_site)
        self.list_display_links = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return not obj

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ApiLog, AdminApiLog)
