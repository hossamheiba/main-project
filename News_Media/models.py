from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from django.utils.html import mark_safe


# Image Banner Models
class ImageBannerNews(models.Model):
    image_banner_news = models.ImageField(
        _("Image Banner news"),
        upload_to='news_media/image_banner_news/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )

    def __str__(self):
        return "news"

    def image_tag(self):
        if self.image_banner_news:
            return mark_safe(
                f'<img src="{self.image_banner_news.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #fcc00c;"/>'
            )
        return "No Image"

    image_tag.short_description = 'image banner news'

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("news")



# News Models
class News(models.Model):
    image_banner_news = models.ForeignKey(ImageBannerNews, on_delete=models.CASCADE)
    news_title = models.CharField(_('news title'), max_length=100, help_text='Maximum 100 characters')
    news_description = models.TextField(_('news description'), max_length=2000, help_text='Maximum 2000 characters')
    news_date = models.DateField(default=timezone.now)
    news_image = models.ImageField(_('news image'), upload_to='news_media/news_image/')

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = _("News Card")
        verbose_name_plural = _("News Cards")


class NewsDetails(models.Model):
    news = models.OneToOneField(
        News,
        on_delete=models.CASCADE,
        help_text=mark_safe(_('If you add News Card, you must save and continue editing before typing any entry for it to appear in the drop-down list.'))
    )
    image_banner_news = models.ForeignKey(ImageBannerNews, on_delete=models.CASCADE, related_name="new" , blank=True, null=True)
    image_banner_inside_page = models.ImageField(
        _("image banner inside page"),
        upload_to='news_media/image_banner/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )
    news_page_image = models.ImageField(_('news page image'), upload_to='news_media/news_page_image/')
    news_page_title = models.CharField(_('news page title'), max_length=100, help_text='Maximum 100 characters')
    news_page_description = models.TextField(_('news page description'), max_length=2000, help_text='Maximum 2000 characters')
    slug = models.SlugField(blank=True, null=True ,max_length=100)

    def __str__(self):
        return self.news_page_title

    def save(self, *args, **kwargs):
        if self.news_page_title and (not self.slug or slugify(self.news_page_title) != self.slug):
            self.slug = slugify(self.news_page_title)
        super(NewsDetails, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("News Details")
        verbose_name_plural = _("News Details")





# Media Models
class ImageBannerMedia(models.Model):
    image_banner_media = models.ImageField(
        _("Image Banner media"),
        upload_to='news_media/image_banner_media/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )

    def __str__(self):
        return "Media"

    def image_tag(self):
        if self.image_banner_media:
            return mark_safe(
                f'<img src="{self.image_banner_media.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #fcc00c;"/>'
            )
        return "No Image"

    image_tag.short_description = 'image banner media'

    class Meta:
        verbose_name = _("media")
        verbose_name_plural = _("media")


class Media(models.Model):
    image_banner_media = models.ForeignKey(ImageBannerMedia, on_delete=models.CASCADE)
    media_title = models.CharField(_('media title'), max_length=100, help_text='Maximum 100 characters')
    media_description = models.TextField(_('media description'), max_length=2000, help_text='Maximum 2000 characters')
    media_image = models.ImageField(_('media image'), upload_to='news_media/media_image/')

    def __str__(self):
        return self.media_title

    class Meta:
        verbose_name = _("Media Card")
        verbose_name_plural = _("Media Cards")


class MediaDetails(models.Model):
    media = models.OneToOneField(
        Media,
        on_delete=models.CASCADE,
        help_text=mark_safe(_('If you add Media Card, you must save and continue editing before typing any entry for it to appear in the drop-down list.'))
    )
    image_banner_media = models.ForeignKey(ImageBannerMedia, on_delete=models.CASCADE, related_name="newmedia" , blank=True, null=True)
    image_banner_inside_page = models.ImageField(
        _("image banner inside page"),
        upload_to='news_media/image_banner/',
        help_text=mark_safe(_('Optional - as you like <br> If no image is selected, an automatic image appears.')),
        blank=True,
        null=True
    )
    
    media_page_video = models.FileField(_("video"), help_text='Optional', upload_to='news_media/videos_page/', blank=True, null=True)
    media_page_title = models.CharField(_('media page title'), max_length=100, help_text='Maximum 100 characters')
    media_page_description = models.TextField(_('media page description'), max_length=2000, help_text='Maximum 2000 characters')

    slug = models.SlugField(blank=True, null=True , max_length=100)

    def __str__(self):
        return self.media_page_title

    def save(self, *args, **kwargs):
        if self.media_page_title and (not self.slug or slugify(self.media_page_title) != self.slug):
            self.slug = slugify(self.media_page_title)
        super(MediaDetails, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Media Details")
        verbose_name_plural = _("Media Details")
