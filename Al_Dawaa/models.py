from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from django.utils.text import slugify
from colorfield.fields import ColorField


# We_Aldawaa ------------------------------------------------
class We_Aldawaa(models.Model):
    image_banner = models.ImageField(
        _("image banner"),
        upload_to='we_aldawaa/image_banner/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )
    section_image = models.ImageField(
        _("section image"),
        upload_to='we_aldawaa/section_image/'
    )
    section_title = models.CharField(
        _('section title'),
        max_length=100,
        help_text='Maximum 100 characters'
    )
    section_description = models.TextField(
        _("section description"),
        max_length=2000,
        help_text='Maximum 2000 characters'
    )

    class Meta:
        verbose_name = _("We_Aldawaa")
        verbose_name_plural = _("We_Aldawaa")

    def __str__(self):
        return self.section_title

    def image_tag(self):
        if self.section_image:
            return mark_safe(f'<img src="{self.section_image.url}" width="50" height="50" style="border-radius: 10%; border: solid 1px #fcc00c;"/>')
        return "No Image"
    image_tag.short_description = 'image banner We_Aldawaa'


class Feature(models.Model):
    we_aldawaa = models.ForeignKey(We_Aldawaa, related_name="process_icon", on_delete=models.CASCADE)
    feature_title = models.CharField(_('feature title'), max_length=100, help_text='Maximum 100 characters')
    feature_count = models.PositiveIntegerField(_('feature count'))
    feature_image_or_icon = models.ImageField(
        _('feature image or icon'),
        upload_to='we_aldawaa/feature_image_or_icon',
        help_text=mark_safe('For icons, visit <a href="https://www.flaticon.com/" target="_blank">https://www.flaticon.com/</a>')
    )

    def __str__(self):
        return self.feature_title


class TimelineEvent(models.Model):
    icon = models.ForeignKey(We_Aldawaa, related_name="process_timeline", on_delete=models.CASCADE)
    Time_line_year = models.PositiveIntegerField(_('Time line year'))
    Time_line_description = models.TextField(_('Time line description'), max_length=100, help_text='Maximum 100 characters')

    def __str__(self):
        return str(self.Time_line_year)


# AlDawaaDepartment ------------------------------------------------
class ImageBannerDepartment(models.Model):
    image_banner_department = models.ImageField(
        _("Image Banner Department"),
        upload_to='we_aldawaa/image_banner_department/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("AL Dawaa Department")
        verbose_name_plural = _("AL Dawaa Department")

    def __str__(self):
        return "AL Dawaa Department"

    def image_tag(self):
        if self.image_banner_department:
            return mark_safe(f'<img src="{self.image_banner_department.url}" width="50" height="50" style="border-radius: 10%; border: solid 1px #fcc00c;"/>')
        return "No Image"
    image_tag.short_description = 'Image Banner Department'


class AlDawaaDepartmentCard(models.Model):
    image_banner = models.ForeignKey(ImageBannerDepartment, on_delete=models.CASCADE)
    department_title = models.CharField(_('Department Title'), max_length=100, help_text='Maximum 100 characters')
    department_image_or_icon = models.ImageField(_('Department Image or Icon'), upload_to='we_ALdawaa/image_or_icon/',
    help_text=mark_safe(
            _('To select icons of specific sizes, please visit this site. For icons, '
              'visit <a href="https://www.flaticon.com/" target="_blank">Flaticon</a>.')
        ))
    department_description = models.TextField(_('Department Description'), max_length=1000, help_text='Maximum 1000 characters')
    department_bg_color = ColorField(_('Background Color'), default="#FFFFFF")
    department_text_color = ColorField(_('Text Color'), default="#000000")

    class Meta:
        verbose_name = _("Al Dawaa Department Card")
        verbose_name_plural = _("Al Dawaa Department Card")

    def __str__(self):
        return self.department_title


class Department_Inside_Page(models.Model):
    category = models.OneToOneField(
        AlDawaaDepartmentCard,
        on_delete=models.CASCADE,
        related_name="department",
        help_text=mark_safe(_('If you add a Al Dawaa Department Card, you must save and continue editing before typing any entry for it to appear in the drop-down list.'))
    )
    ImageBannerDepartment = models.ForeignKey(ImageBannerDepartment, on_delete=models.CASCADE  ,blank=True, null=True )
    image_banner_inside_page = models.ImageField(
        _("image banner"),
        upload_to='we_aldawaa/banner_Department_Inside_Page/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )
    section_title = models.CharField(_('Section Title'), max_length=100, help_text='Maximum 100 characters')
    section_description = models.TextField(_('Section Description'), max_length=2000, help_text='Maximum 2000 characters')
    section_image = models.ImageField(_('Section Image'), upload_to='we_aldawaa/section_image_Department_Inside_Page/')
    slug = models.SlugField(blank=True, null=True ,max_length=100)

    class Meta:
        verbose_name = _("Department Inside Page")
        verbose_name_plural = _("Department Inside Page")

    def __str__(self):
        return self.section_title

    def save(self, *args, **kwargs):
        if self.section_title and (not self.slug or slugify(self.section_title) != self.slug):
            self.slug = slugify(self.section_title)
        super(Department_Inside_Page, self).save(*args, **kwargs)


# Social_Responsibility ------------------------------------------------
class Social_Responsibility(models.Model):
    image_banner = models.ImageField(
        _("image banner"),
        upload_to='we_ALdawaa/Social_Responsibility_Banner/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )
    page_title = models.CharField(_('page title'), max_length=100, help_text='Maximum 100 characters')
    page_description = models.TextField(_('page description'), max_length=2000, help_text='Maximum 2000 characters')

    class Meta:
        verbose_name = _("Social_Page_Responsibility")
        verbose_name_plural = _("Social_Page_Responsibility")

    def __str__(self):
        return self.page_title

    def image_tag(self):
        if self.image_banner:
            return mark_safe(f'<img src="{self.image_banner.url}" width="50" height="50" style="border-radius: 10%; border: solid 1px #fcc00c;"/>')
        return "No Image"
    image_tag.short_description = 'image banner Social Page Responsibility'


class Card_Social_Responsibility(models.Model):
    image_banner = models.ForeignKey(Social_Responsibility, on_delete=models.CASCADE, related_name="categories", null=True, blank=True)
    card_title = models.CharField(_('card title'), max_length=100, help_text='Maximum 100 characters')
    card_image = models.ImageField(_('section image'), upload_to='we_aldawaa/Social_Responsibility_card_image/')
    card_description = models.TextField(_('section description'), max_length=2000, help_text='Maximum 2000 characters')

    class Meta:
        verbose_name = _("Social_Responsibility")
        verbose_name_plural = _("Social_Responsibility")

    def __str__(self):
        return self.card_title


class Social_Responsibility_details(models.Model):
    Card_Social_Responsibility = models.OneToOneField(
        Card_Social_Responsibility,
        on_delete=models.CASCADE,
        related_name="social_responsibility_details",
        help_text=mark_safe(_('If you add a social responsibility card, you must save and continue editing before typing any entry for it to appear in the drop-down lis'))
    )
    image_banner = models.ForeignKey(Social_Responsibility, on_delete=models.CASCADE , null=True, blank=True)
    image_banner_inside_page = models.ImageField(
        _("image banner"),
        upload_to='we_aldawaa/Social_Responsibility_Banner/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )
    title_details_social = models.CharField(_('title details social'), max_length=100, help_text='Maximum 100 characters')
    image_details_social = models.ImageField(_('image details social'), upload_to='Social_Responsibility/image_details_social/')
    description_details_social = models.TextField(_('description details social'), max_length=1000, help_text='Maximum 1000 characters')
    link = models.URLField(blank=True, null=True, help_text='optional')
    slug = models.SlugField(blank=True, null=True ,max_length=100)

    class Meta:
        verbose_name = _("Social_Responsibility_details")
        verbose_name_plural = _("Social_Responsibility_details")

    def __str__(self):
        return self.title_details_social
    
    def save(self, *args, **kwargs):
        if self.title_details_social and (not self.slug or slugify(self.title_details_social) != self.slug):
            self.slug = slugify(self.title_details_social)
        super(Social_Responsibility_details, self).save(*args, **kwargs)



# Our_Programs------------------------------------------------
class Image_Banner_Program(models.Model):
    image_banner_program = models.ImageField(
        _("image banner program"),
        upload_to='we_aldawaa/Image_Banner_Program/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name = _("Our Program")
        verbose_name_plural = _("Our Programs")

    def __str__(self):
        return "Image_Banner_Program"
        
    def image_tag(self):
        if self.image_banner_program:
            return mark_safe(
                f'<img src="{self.image_banner_program.url}" width="50" height="50" style="border-radius: 10%; border: solid 1px #fcc00c;"/>'
            )
        return "No Image"
    
    image_tag.short_description = 'image_banner_program'  


class Program(models.Model):
    image_banner_program = models.ForeignKey(
        Image_Banner_Program,
        related_name="process_image",
        on_delete=models.CASCADE
    )

    program_image_or_icon = models.ImageField(
        _('program image or icon'),
        upload_to='we_aldawaa/program_image_or_icon/',
        help_text=mark_safe(
            _('To select icons of specific sizes, please visit this site. For icons, '
              'visit <a href="https://www.flaticon.com/" target="_blank">Flaticon</a>.')
        )
    )
    program_title = models.CharField(
        _('program title'),
        max_length=100,
        help_text=_('Maximum 100 characters')
    )

    program_description = models.TextField(
        _('program description'),
        max_length=1000,
        help_text=_('Maximum 1000 characters')
    )


    def __str__(self):
        return self.program_title

    class Meta:
        verbose_name = _("Our Program")
        verbose_name_plural = _("Our Programs")