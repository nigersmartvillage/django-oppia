
from django.contrib import admin
from oppia.models import Course, \
                         Section, \
                         Activity, \
                         Tracker, \
                         Media, \
                         Cohort, \
                         CoursePermissions
from oppia.models import Participant, Tag, CourseTag
from oppia.models import Badge, Award, Points, AwardCourse
from oppia.models import CourseCohort, CoursePublishingLog


class TrackerAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'submitted_date',
                    'tracker_date',
                    'time_taken',
                    'event',
                    'points',
                    'course',
                    'completed')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_lang',
                    'shortname',
                    'version',
                    'lastupdated_date',
                    'user',
                    'filename',
                    'is_draft',
                    'is_archived')
    search_fields = ['title', 'shortname', 'version', 'filename']

    def title_lang(self, obj):
        return obj.get_title()


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('cohort', 'user', 'role')


class ParticipantInline(admin.TabularInline):
    model = Participant


class CohortAdmin(admin.ModelAdmin):
    list_display = ('description', 'start_date', 'end_date')
    inlines = [
        ParticipantInline,
    ]


class CourseCohortAdmin(admin.ModelAdmin):
    list_display = ('course', 'cohort')


class BadgeAdmin(admin.ModelAdmin):
    list_display = ('description', 'points')


class PointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'course', 'points', 'date', 'description')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title_lang', 'section', 'type', 'digest')
    search_fields = ['title', 'type', 'digest']

    def title_lang(self, obj):
        return obj.get_title()


class AwardCourseAdmin(admin.ModelAdmin):
    list_display = ('award', 'course', 'course_version')


class AwardAdmin(admin.ModelAdmin):
    list_display = ('badge', 'user', 'description', 'award_date')


class CourseTagAdmin(admin.ModelAdmin):
    list_display = ('course', 'tag')


class CoursePublishingLogAdmin(admin.ModelAdmin):
    list_display = ('course',
                    'new_version',
                    'old_version',
                    'user',
                    'action',
                    'data')


class CoursePermissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'role')


class MediaAdmin(admin.ModelAdmin):
    list_display = ('course', 'digest', 'filename', 'download_url')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'order')
    search_fields = ['title']


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'created_date',
                    'created_by',
                    'description',
                    'order_priority',
                    'highlight')
    ordering = ['-order_priority', 'name']
    search_fields = ['name', 'description']


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(AwardCourse, AwardCourseAdmin)
admin.site.register(Cohort, CohortAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCohort, CourseCohortAdmin)
admin.site.register(CourseTag, CourseTagAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Points, PointsAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Tracker, TrackerAdmin)
admin.site.register(CoursePermissions, CoursePermissionsAdmin)
admin.site.register(CoursePublishingLog, CoursePublishingLogAdmin)
