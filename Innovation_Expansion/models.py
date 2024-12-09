from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils.html import mark_safe



class ImageBannerInnovation(models.Model):
    image_banner_innovation = models.ImageField(
        _("Image Banner innovation"),
        upload_to='innovation/image_banner_innovation/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )
    def __str__(self):
        return "Innovation & Expansion"
    
    def image_tag(self):
        if self.image_banner_innovation:
            return mark_safe(
                f'<img src="{self.image_banner_innovation.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #fcc00c;"/>'
            )
        return "No Image"
    image_tag.short_description = 'image banner innovation'
    
    class Meta:
        verbose_name = _("Innovation & Expansion")
        verbose_name_plural = _(" Innovation & Expansion")
    

class InnovationExpansion(models.Model):
    image_banner_innovation = models.ForeignKey(ImageBannerInnovation,on_delete=models.CASCADE)
    innovation_image = models.ImageField(_('innovation_image') , upload_to='innovation/innovation_card_image/')
    innovation_title = models.CharField(_('innovation title') , max_length=100 , help_text='Maximum 100 characters')
    innovation_description = models.TextField(_('innovation description') , max_length=1000 , help_text='Maximum 1000 characters')

    def __str__(self):
        return self.innovation_title
    
    class Meta:
        verbose_name = _("Innovation_Expansion")
        verbose_name_plural = _("Innovation_Expansion")
        

class InnovationMainPage(models.Model):
    innovationexpansion = models.OneToOneField(InnovationExpansion, on_delete=models.CASCADE ,related_name="innovation", help_text=mark_safe(_('If you add Innovation & Expansion, you must save and continue editing before typing any entry for it to appear in the drop-down list.')),)
    ImageBannerInnovation = models.ForeignKey(ImageBannerInnovation, on_delete=models.CASCADE, related_name="innovation" , blank=True, null=True)
    image_banner_inside_page = models.ImageField(_("image banner inside page"), upload_to='innovation/image_banner/',  help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),blank=True,null=True)
    detsils_innovation_image = models.ImageField(_('detsils innovation image') , upload_to='innovation/detsils_innovation_image/')
    detsils_innovation_title = models.CharField(_('detsils innovation title') , max_length=100 , help_text='Maximum 100 characters')
    detsils_innovation_description = models.TextField(_('detsils innovation description') , max_length=1000 , help_text='Maximum 1000 characters')
    video = models.FileField(_("video"), help_text='Optional', upload_to='innovation/videos_page/', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True ,max_length=100)

    def __str__ (self):
        return self.detsils_innovation_title
    
    def save(self, *args, **kwargs):
        if self.detsils_innovation_title and (not self.slug or slugify(self.detsils_innovation_title) != self.slug):
            self.slug = slugify(self.detsils_innovation_title)
        super(InnovationMainPage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Innovation_inside_Page")
        verbose_name_plural = _("Innovation_inside_Page")
