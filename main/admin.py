from django.contrib import admin
from main.models import *
# Register your models here.


@admin.register(AboutUsModel)
class AboutUsAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

@admin.register(CateringModel)
class CateringAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

@admin.register(StandModel)
class StandAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(EventsModel)
admin.site.register(TagModel)
admin.site.register(EquipmentModel)
admin.site.register(ImagesModel)
# admin.site.register(FullPageModel)
admin.site.register(PortfolioModel)
admin.site.register(OtherModel)