from django.contrib import admin
from .models import Priority, Category, Task, Note, Subtask


class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Priority, PriorityAdmin)
admin.site.register(Category, CategoryAdmin)

def mark_as_completed(modeladmin, request, queryset):
    queryset.update(status="Completed")


mark_as_completed.short_description = "Mark selected tasks as completed"

def mark_as_pending(modeladmin, request, queryset):
    queryset.update(status="Pending")


mark_as_pending.short_description = "Mark selected tasks as pending"


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "category", "priority", "deadline")
    list_filter = ("status", "category", "priority")
    search_fields = ("title", "description")
    ordering = ("deadline",)    
    date_hierarchy = "deadline"
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("category", "priority")
    list_per_page = 10
    actions = ("mark_as_completed", "mark_as_in_progress","mark_as_pending")

    fieldsets = (
        ("Task Information", {
            "fields": ("title", "description", "status")
        }),
        ("Task Details", {
            "fields": ("category", "priority", "deadline")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )


admin.site.register(Task, TaskAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_display = ("task", "content", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("content",)
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Note, NoteAdmin)

class SubtaskAdmin(admin.ModelAdmin):
    list_display = ("title", "parent_task_name", "status", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title",)
    readonly_fields = ("created_at", "updated_at")

    def parent_task_name(self, obj):
        return obj.parent_task.title

    parent_task_name.short_description = "Parent Task Name"


admin.site.register(Subtask, SubtaskAdmin)