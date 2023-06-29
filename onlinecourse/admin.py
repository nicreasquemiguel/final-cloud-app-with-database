from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 4


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'is_correct')

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']


# <HINT> Register Question and Choice models here
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
#cadmin.site.register()

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
