from import_export import resources
from import_export.admin import ImportExportModelAdmin
# from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin
from .models import TimePost, Client, Project


class TimePostResource(resources.ModelResource):

    class Meta:
        model = TimePost
        fields = (
            'user__username',
            'date', 'time_spent', 'notes',
            'expenses', 'expense_notes', 'miles', 
            'miles_notes','client__name', 'project__name',
            )
        # export_order = ('id', 'price', 'author', 'name')



# admin.site.register(TimePost)
@admin.register(TimePost)
# class TimePostAdmin(ImportExportActionModelAdmin):
class TimePostAdmin(ImportExportModelAdmin):

    resource_class = TimePostResource
    

admin.site.register(Client)
admin.site.register(Project)
