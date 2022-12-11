from django.contrib import admin
from .models import *


class QuestionInline(admin.TabularInline):
    model = Question
    show_change_link = True


class ChoiceInline(admin.TabularInline):
    model = Choice


class TestAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline
    ]





admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)