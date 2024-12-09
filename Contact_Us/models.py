from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe


class Image_Banner(models.Model):
    image_banner = models.ImageField(
        _("image banner"),
        upload_to='aldawaa_departments/image_banner/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )


    def __str__(self):
        return "Image Banner Contact Us"
    
    class Meta:
        verbose_name = _("Contact Info")
        verbose_name_plural = _("Contact Info")

    def image_tag(self):
        if self.image_banner:
            return mark_safe(f'<img src="{self.image_banner.url}" width="50" height="50" style="border-radius: 10%; border: solid 1px #fcc00c;"/>')
        return "No Image"
    image_tag.short_description = 'Image Banner Contact Us'

class ContactInfo(models.Model):
    Image_Banner = models.ForeignKey(
        Image_Banner, 
        on_delete=models.CASCADE
    )
    
    card_title = models.CharField(
        _('card title'),
        max_length=30,
        help_text=mark_safe('Maximum 30 characters<br>mandatory')
    )
    
    card_email = models.EmailField(
        _('card email'),
        help_text="optional",
        blank=True,
        null=True
    )
    
    card_phone = models.IntegerField(
        _('card phone'),
        help_text="optional",
        blank=True,
        null=True
    )
    
    pragraph_link = models.CharField(
        _('pragraph link'),
        help_text="optional",
        max_length=225,
        blank=True,
        null=True
    )
    
    link_pragraph = models.URLField(
        _('link pragraph'),
        help_text="optional",
        blank=True,
        null=True
    )
    
    address_title = models.CharField(
        _('address title'),
        help_text="optional",
        max_length=225,
        blank=True,
        null=True
    )
    
    address_link = models.URLField(
        _('address link'),
        help_text="optional",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Contact Info")
        verbose_name_plural = _("Contact Info")
        
    def __str__(self):
        return self.card_title


class ContactFormSubmission(models.Model):
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('email'))
    phone = models.IntegerField(_('phone'), blank=True)
    message = models.TextField(_('message'))
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Contact message")
        verbose_name_plural = _("Contact message")
        
    def __str__(self):
        return self.name
