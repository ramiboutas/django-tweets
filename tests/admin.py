from django.contrib import admin


from .models import DjangoNewsIssue
from .models import DjangoNewsIssueItem


admin.site.register(DjangoNewsIssueItem)


@admin.register(DjangoNewsIssue)
class DjangoNewsIssueAdmin(admin.ModelAdmin):
    list_display = ("__str__", "date", "url")
    list_filter = ("date",)
    readonly_fields = ("title", "date", "url")
