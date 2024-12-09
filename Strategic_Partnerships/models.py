from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from django.utils.text import slugify


class ImageBannerStrategic(models.Model):
    image_banner_strategic = models.ImageField(
        _("Image Banner strategic"),
        upload_to='Strategic/image_banner_strategic/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )
    def __str__(self):
        return "Strategic"
    
    def image_tag(self):
        if self.image_banner_strategic:
            return mark_safe(
                f'<img src="{self.image_banner_strategic.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #fcc00c;"/>'
            )
        return "No Image"
    image_tag.short_description = 'image banner strategic'
    
    class Meta:
        verbose_name = _("strategic")
        verbose_name_plural = _("strategic")

class Partner_Brands(models.Model):
    image_banner_strategic = models.ForeignKey(ImageBannerStrategic,on_delete=models.CASCADE)
    partner_image = models.ImageField(_('partner_image'),upload_to='Strategic/partner_image/')


    
class Testimonial(models.Model):
    image_banner_strategic = models.ForeignKey(ImageBannerStrategic,on_delete=models.CASCADE)
    partner_title = models.CharField(_("partner title"), max_length=100 , help_text='Maximum 100 characters')
    partner_content = models.TextField(_("partner content"), max_length=2000 , help_text='Maximum 2000 characters')
    partner_image = models.ImageField(_('partner image'),upload_to='Strategic/partner_image/')

    def __str__(self):
        return self.partner_title
    
    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonial")
        



class Partner(models.Model):
    Testimonial = models.OneToOneField(Testimonial, on_delete=models.CASCADE , 
        help_text=mark_safe(_('If you add a Testimonial Card, you must save and continue editing before typing any entry for it to appear in the drop-down list.')),)
    image_banner_strategic = models.ForeignKey(ImageBannerStrategic,on_delete=models.CASCADE ,blank=True, null=True)
    image_banner_inside_page = models.ImageField(_("image banner inside page"), upload_to='Strategic/image_banner/',  
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),blank=True,null=True)
    partner_title = models.CharField(_("partner title"), max_length=100 , help_text='Maximum 100 characters')
    partner_description = models.TextField(_("partner description"), max_length=2000 , help_text='Maximum 2000 characters')
    partner_main_image = models.ImageField(_('partner main image'),upload_to='Strategic/partner_main_image/' )
    
    first_person_name = models.CharField(_('first person name'),max_length=100 , help_text='Maximum 100 characters')
    first_person_position = models.CharField(_('first person position'),max_length=100 , help_text='Maximum 100 characters')
    first_person_image = models.ImageField(_('first person image'),upload_to='Strategic/Person_Prtner/' )
    
    second_person_name = models.CharField(_('second person name'),max_length=100 , help_text='Maximum1 100 characters')
    second_person_position = models.CharField(_('second person position'),max_length=100 , help_text='Maximum 100 characters')
    second_person_image = models.ImageField(_('second person image'),upload_to='Strategic/Person_Prtner/' )
    slug = models.SlugField(blank=True, null=True , max_length=100)

    def __str__ (self):
        return self.partner_title
    
    def save(self, *args, **kwargs):
        if self.partner_title and (not self.slug or slugify(self.partner_title) != self.slug):
            self.slug = slugify(self.partner_title)
        super(Partner, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partner")