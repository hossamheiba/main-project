from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import ImageBannerNews, News, NewsDetails, ImageBannerMedia, Media, MediaDetails

class ImageBannerNewsTest(TestCase):
    def setUp(self):
        self.image_banner_news = ImageBannerNews.objects.create(
            image_banner_news='news_media/image_banner_news/sample_image.jpg'
        )

    def test_image_banner_news_creation(self):
        banner = ImageBannerNews.objects.get(id=self.image_banner_news.id)
        self.assertEqual(banner.image_banner_news.name, 'news_media/image_banner_news/sample_image.jpg')

class NewsTest(TestCase):
    def setUp(self):
        image_banner_news = ImageBannerNews.objects.create(
            image_banner_news='news_media/image_banner_news/sample_image.jpg'
        )
        self.news = News.objects.create(
            image_banner_news=image_banner_news,
            news_title='Test News Title',
            news_description='This is a test news description.',
            news_image='news_media/news_image/test_news_image.jpg'
        )

    def test_news_creation(self):
        news = News.objects.get(id=self.news.id)
        self.assertEqual(news.news_title, 'Test News Title')
        self.assertEqual(news.news_description, 'This is a test news description.')

class NewsDetailsTest(TestCase):
    def setUp(self):
        image_banner_news = ImageBannerNews.objects.create(
            image_banner_news='news_media/image_banner_news/sample_image.jpg'
        )
        self.news = News.objects.create(
            image_banner_news=image_banner_news,
            news_title='Test News Title',
            news_description='This is a test news description.',
            news_image='news_media/news_image/test_news_image.jpg'
        )
        self.news_details = NewsDetails.objects.create(
            news=self.news,
            image_banner_news=image_banner_news,
            news_page_title='Test News Page Title',
            news_page_description='Test News Page Description',
            news_page_image='news_media/news_page_image/test_news_page_image.jpg'
        )

    def test_news_details_creation(self):
        news_details = NewsDetails.objects.get(id=self.news_details.id)
        self.assertEqual(news_details.news_page_title, 'Test News Page Title')
        self.assertEqual(news_details.news_page_description, 'Test News Page Description')
        self.assertTrue(news_details.slug)

    def test_slug_creation_on_save(self):
        news_details = self.news_details
        news_details.news_page_title = 'Updated News Page Title'
        news_details.save()
        self.assertEqual(news_details.slug, 'updated-news-page-title')

class MediaTest(TestCase):
    def setUp(self):
        image_banner_media = ImageBannerMedia.objects.create(
            image_banner_media='news_media/image_banner_media/sample_image.jpg'
        )
        self.media = Media.objects.create(
            image_banner_media=image_banner_media,
            media_title='Test Media Title',
            media_description='This is a test media description.',
            media_image='news_media/media_image/test_media_image.jpg'
        )

    def test_media_creation(self):
        media = Media.objects.get(id=self.media.id)
        self.assertEqual(media.media_title, 'Test Media Title')
        self.assertEqual(media.media_description, 'This is a test media description.')

class MediaDetailsTest(TestCase):
    def setUp(self):
        image_banner_media = ImageBannerMedia.objects.create(
            image_banner_media='news_media/image_banner_media/sample_image.jpg'
        )
        self.media = Media.objects.create(
            image_banner_media=image_banner_media,
            media_title='Test Media Title',
            media_description='This is a test media description.',
            media_image='news_media/media_image/test_media_image.jpg'
        )
        self.media_details = MediaDetails.objects.create(
            media=self.media,
            image_banner_media=image_banner_media,
            media_page_title='Test Media Page Title',
            media_page_description='Test Media Page Description',
            media_page_video='news_media/videos_page/test_media_video.mp4'
        )

    def test_media_details_creation(self):
        media_details = MediaDetails.objects.get(id=self.media_details.id)
        self.assertEqual(media_details.media_page_title, 'Test Media Page Title')
        self.assertEqual(media_details.media_page_description, 'Test Media Page Description')
        self.assertTrue(media_details.slug)

    def test_slug_creation_on_save(self):
        media_details = self.media_details
        media_details.media_page_title = 'Updated Media Page Title'
        media_details.save()
        self.assertEqual(media_details.slug, 'updated-media-page-title')
