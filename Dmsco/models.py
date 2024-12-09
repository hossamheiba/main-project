from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

# About Us Section
class About_Us(models.Model):
    image_banner = models.ImageField(
        _("image banner"), 
        upload_to='about_us/image_banner/', 
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True, 
        null=True
    )
    video = models.FileField(_("video"), upload_to='about_us/videos_page/', blank=True, null=True)
    image = models.ImageField(_("image"), upload_to='about_us/image_page/')
    Years_Of_Experienced = models.IntegerField(_("Years Of Experience"))
    description = models.TextField(
        _("description"), 
        max_length=2000, 
        help_text='Maximum 2000 characters'
    )

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")
    
    def __str__(self):
        return "About_Us"
    
    def image_tag(self):
        if self.image_banner:
            return mark_safe(f'<img src="{self.image_banner.url}" width="50" height="50" style="border-radius: 10%; border: solid 1px #fcc00c;"/>')
        return "No Image"
    
    image_tag.short_description = 'image_banner'


# Card Section
class Card(models.Model):
    card = models.ForeignKey(About_Us, related_name="process_cards", on_delete=models.CASCADE)
    image_card = models.ImageField(_('Image Card'), upload_to='about_us/image_card/')
    title_card = models.CharField(_('title card'), max_length=50, help_text='Maximum 50 characters') 
    description_card = models.TextField(_("description"), max_length=100, help_text='Maximum 100 characters')
    is_collapsible = models.BooleanField(_('Is Collapsible'), default=False)
    collapse_description = models.TextField(_('Collapse Description'), max_length=300, help_text='Maximum 300 characters', blank=True, null=True)

    def __str__(self):
        return self.title_card


# Board Member Section-------------------------------------
class Image_Banner(models.Model):
    image_banner = models.ImageField(
        _("image banner"), 
        upload_to='about_us/Board_Member_image/', 
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name = _("Board Of Directors")
        verbose_name_plural = _("Board Of Directors")
    
    def __str__(self):
        return "Board Of Directors"
    
    def image_tag(self):
        if self.image_banner:
            return mark_safe(f'<img src="{self.image_banner.url}" width="50" height="50" style="border-radius: 10%; border: solid 1px #fcc00c;"/>')
        return "No Image"
    
    image_tag.short_description = 'image_banner'


class BoardMember(models.Model):
    image_banner = models.ForeignKey(Image_Banner, related_name="process_image", on_delete=models.CASCADE)
    person_name = models.CharField(_('Person name'), max_length=100, help_text='Maximum 100 characters')
    person_position = models.CharField(_('person position'), max_length=150, help_text='Maximum 150 characters')
    person_image = models.ImageField(_('person image'), upload_to='about_us/Board_Of_Directors_image', help_text="It's better to put a blank image")

    class Meta:
        verbose_name = _("Board Of Directors")
        verbose_name_plural = _("Board Of Directors")
    
    def __str__(self):
        return self.person_name


# Brand Section---------------------------------------
class Image_Banner_Brand(models.Model):
    image_banner_brand = models.ImageField(
        _("image banner_brand"), 
        upload_to='about_us/Image_Banner_Brand/', 
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name = _("Our Brand")
        verbose_name_plural = _("Our Brand")
    
    def __str__(self):
        return "Image_Banner_Brand"
    
    def image_tag(self):
        if self.image_banner_brand:
            return mark_safe(f'<img src="{self.image_banner_brand.url}" width="50" height="50" style="border-radius: 10%; border: solid 1px #fcc00c;"/>')
        return "No Image"
    
    image_tag.short_description = 'image_banner_brand'


class Brands(models.Model):
    image_banner_brand = models.ForeignKey(Image_Banner_Brand, related_name="process_image", on_delete=models.CASCADE)
    brand_name = models.CharField(_('brand name'), max_length=20, help_text='Maximum 20 characters')
    brand_image = models.ImageField(_('brand image'), upload_to='about_us/brands_images/')

    class Meta:
        verbose_name = _("Brands")
        verbose_name_plural = _("Brands")
    
    def __str__(self):
        return self.brand_name
