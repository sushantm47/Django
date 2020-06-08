from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the Train admin area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('train name', {'fields': ['question_text']}), ('source', {'fields': ['source']}), ('destination', {'fields': ['destination']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
