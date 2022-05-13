from django.contrib import admin

from django.contrib import admin

from .models import Course, Avaliation

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'create', 'atualization', 'active')

@admin.register(Avaliation)
class AvaliationAdmin(admin.ModelAdmin):
    list_display = ('cource', 'name', 'email', 'avaliation', 'create', 'atualization', 'active')
