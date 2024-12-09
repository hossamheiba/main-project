from django.contrib import admin
from .models import HomePgae

@admin.register(HomePgae)
class HomePgaeAdmin(admin.ModelAdmin):
    pass
    # list_display = ('facebook', 'instagram', 'linkedin', 'youtube', 'x')
    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False