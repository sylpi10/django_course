from django.db import models


class Device(models.Model):
    OS_ANDROID = 'android'
    OS_IOS = 'ios'

    OS_CHOICES = (
        (OS_ANDROID , 'android'),
        (OS_IOS, 'ios')
    )

    FORM_FACTOR_PHONE = 'phone'
    FORM_FACTOR_TABLET = 'tablet'

    FORM_FACTOR_CHOICES = (
        (FORM_FACTOR_PHONE, 'phone'),
        (FORM_FACTOR_TABLET, 'tablet')
    )

    os = models.CharField(max_length=20, choices=OS_CHOICES, default=OS_ANDROID)
    form_factor = models.CharField(max_length=20, choices=FORM_FACTOR_CHOICES,default=FORM_FACTOR_PHONE)

    model = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return '{pk} - {os} {form_factor} {model} ({created_at} {enable} {description})'\
            .format(pk=self.pk,
                    os = self.get_os_display(),
                    form_factor = self.get_form_factor_display(),
                    model = self.model,
                    created_at=self.created_at,
                    enable=self.enable,
                    description=self.description
                    )

