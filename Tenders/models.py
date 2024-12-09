from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe


class Image_Banner_Tender(models.Model):
    image_banner_tender = models.ImageField(
        _("Image Banner Tender"),
        upload_to='tenders/image_banner_tender/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )

    def __str__(self):
        return "Tenders"
    
    def image_tag(self):
        if self.image_banner_tender:
            return mark_safe(
                f'<img src="{self.image_banner_tender.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #fcc00c;"/>'
            )
        return "No Image"
    
    image_tag.short_description = 'Image Banner Tender'
    
    class Meta:
        verbose_name = _("Tenders")
        verbose_name_plural = _("Tenders")


class TenderCategory(models.Model):
    image_banner = models.ForeignKey(
        Image_Banner_Tender,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    tender_title = models.CharField(_('Tender Title'), max_length=100, help_text='Maximum 100 characters')
    tender_image_or_icon = models.ImageField(
        _('Tender Image or Icon'),
        upload_to='Tenders/tender_image_or_icon/',
        help_text=mark_safe(
            'For icons, visit <a href="https://www.flaticon.com/" target="_blank">https://www.flaticon.com/</a>'
        )
    )

    def __str__(self):
        return self.tender_title
    
    class Meta:
        verbose_name = _("Tenders")
        verbose_name_plural = _("Tenders") 


class Tender(models.Model):
    category = models.ForeignKey(
        TenderCategory,
        on_delete=models.CASCADE,
        related_name="tenders",
        help_text=mark_safe(_('Here you can choose more than one tender; you must save and continue editing for it to appear.'))
    )
    image_banner = models.ForeignKey(Image_Banner_Tender, on_delete=models.CASCADE)
    category_title = models.CharField(_('Category Title'), max_length=100, help_text='Maximum 100 characters')
    category_pdf_file = models.FileField(_('Category PDF File'), upload_to='Tenders/PDF/')
    category_description = models.TextField(_('Category Description'), max_length=2000, help_text='Maximum 2000 characters')

    def __str__(self):
        return self.category_title
    
    class Meta:
        verbose_name = _("Tender Category")
        verbose_name_plural = _("Tender Categories")
