from django.contrib import admin
from .models import Tuition, Application, Review, Subject
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Register your models here.
class TuitionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "tuition_class",
        "availability",
        "medium",
        "student_gender",
        "instructor_gender",
        "number_of_students",
        "salary",
    )
    list_filter = (
        "tuition_class",
        "availability",
        "medium",
        "student_gender",
        "instructor_gender",
    )
    search_fields = (
        "title",
        "description",
    )

    def save_model(self, request, obj, form, change):
        obj.save()

        if not change:
            email_subject = "Tuition Added Successfully"
            email_body = render_to_string(
                "tuition_added_email.html",
                {
                    "instructor": obj.instructor,
                    "tuition": obj,
                },
            )

            from_email = "StudySphere Team <noreply@studysphere.com>"

            email = EmailMultiAlternatives(
                email_subject,
                "",
                from_email,
                to=[obj.instructor.user.email],
            )
            email.attach_alternative(email_body, "text/html")
            email.send()


class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "tuition",
        "applied_at",
        "is_approved",
    )
    list_filter = (
        "is_approved",
        "applied_at",
    )
    search_fields = (
        "student__username",
        "tuition__title",
    )
    list_editable = ("is_approved",)

    def save_model(self, request, obj, form, change):
        obj.save()

        if not change:
            email_subject = "Application received for tuition"
            email_body = render_to_string(
                "application_received_mail.html",
                {
                    "user": obj.student,
                    "tuition": obj.tuition,
                },
            )
            from_email = "StudySphere Team <noreply@studysphere.com>"

            email = EmailMultiAlternatives(
                email_subject,
                "",
                from_email,
                to=[obj.student.user.email],
            )
            email.attach_alternative(email_body, "text/html")
            email.send()

        if obj.is_approved:
            email_subject = "Tuition has been approved."
            email_body = render_to_string(
                "tuition_approved_mail.html",
                {
                    "user": obj.student,
                    "tuition": obj.tuition,
                },
            )

            from_email = "StudySphere Team <noreply@studysphere.com>"

            email = EmailMultiAlternatives(
                email_subject,
                "",
                from_email,
                to=[obj.student.email],
            )
            email.attach_alternative(email_body, "text/html")
            email.send()


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "reviewer",
        "tuition",
        "created",
        "rating",
    )
    list_filter = (
        "rating",
        "created",
    )
    search_fields = (
        "reviewer__username",
        "tuition__title",
        "body",
    )
    readonly_fields = ("created",)

    def save_model(self, request, obj, form, change):
        obj.save()

        if not change:
            email_subject = "Thank you for your review"
            email_body = render_to_string(
                "review_thank_you_mail.html",
                {
                    "user": obj.reviewer,
                    "tuition": obj.tuition,
                    "review": obj.body,
                },
            )

            from_email = "StudySphere Team <noreply@example.com>"

            email = EmailMultiAlternatives(
                email_subject,
                "",
                from_email,
                to=[obj.reviewer.user.email],
            )
            email.attach_alternative(email_body, "text/html")
            email.send()


class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


admin.site.register(Tuition, TuitionAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Subject, SubjectAdmin)
