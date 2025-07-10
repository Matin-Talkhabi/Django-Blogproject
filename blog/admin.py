from django.contrib import admin
from . import models

class FilterByTitle(admin.SimpleListFilter):
    title = 'title'
    parameter_name = 'title'
    def lookups(self, request, model_admin):
        return (
            ('django' , 'جنگو'),
            ('python' , 'پایتون'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())

# class CommentInline(admin.StackedInline):
#     model = models.Comment


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'published' , 'return_img']
    list_filter = ['status', 'published', FilterByTitle]
    list_editable = ['published']
    search_fields = ('title', 'body')
    # inlines = [CommentInline]


# Register your models here.
# admin.site.register(models.Post)
admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)
