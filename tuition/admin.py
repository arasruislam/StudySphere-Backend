from django.contrib import admin
from .models import Tuition, Application, Review
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@admin.register(Tuition)
class TuitionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "level",
        "subject",
        "availability",
        "created_at",
        "updated_at",
    )
    list_filter = ("level", "availability")
    search_fields = ("title", "description", "subject")
    list_editable = ("availability",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "tuition", "applied_at", "is_approved")
    list_filter = ("is_approved", "applied_at")
    search_fields = ("user__username", "tuition__title")
    list_editable = ("is_approved",)

    # def save_model(self, request,obj,form):
    #     if obj.is_approved == True:
    #         email_subject = "Confirm your email"
    #         email_body = render_to_string(
    #             "confirm_email.html", {"confirm_link": confirm_link}
    #         )
    #         email = EmailMultiAlternatives(email_subject, "", to=[obj.account.user.email])
    #         email.attach_alternative(email_body, "text/html")
    #         email.send()

    def save_model(self, request, obj, form, change):
        obj.save()

        if not change:
            email_subject = "Application received for tuition"
            email_body = render_to_string(
                "application_received_mail.html",
                {"user": obj.user, "tuition": obj.tuition},
            )
            from_email = "StudySphere Team <noreply@studysphere.com>"

            email = EmailMultiAlternatives(
                email_subject, "", from_email, to=[obj.user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()

        if obj.is_approved:
            email_subject = "Tuition has been approved."
            email_body = render_to_string(
                "tuition_approved_mail.html",
                {"user": obj.user, "tuition": obj.tuition},
            )

            from_email = "StudySphere Team <noreply@studysphere.com>"

            email = EmailMultiAlternatives(
                email_subject, "", from_email, to=[obj.user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewer", "tuition", "created", "rating")
    list_filter = ("rating", "created")
    search_fields = ("reviewer__username", "tuition__title", "body")
    readonly_fields = ("created",)
