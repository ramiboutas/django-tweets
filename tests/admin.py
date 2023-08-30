from django.contrib import admin


from .models import DjangoNewsIssue
from .models import DjangoNewsIssueItem


admin.site.register(DjangoNewsIssue)
admin.site.register(DjangoNewsIssueItem)
