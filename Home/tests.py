from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import HomePgae


class HomePageTest(TestCase):

    def test_homepage_creation_with_video(self):
        video_file = SimpleUploadedFile("test_video.mp4", b"file_content", content_type="video/mp4")
        
        homepage = HomePgae.objects.create(
            video=video_file,
            facebook="https://facebook.com/username",
            instagram="https://instagram.com/username",
            linkedin="https://linkedin.com/in/username",
            youtube="https://youtube.com/channel/username",
            x="https://x.com/username"
        )
        
        self.assertTrue(homepage.video.name.startswith('videos/'))
        
        self.assertEqual(homepage.facebook, "https://facebook.com/username")
        self.assertEqual(homepage.instagram, "https://instagram.com/username")
        self.assertEqual(homepage.linkedin, "https://linkedin.com/in/username")
        self.assertEqual(homepage.youtube, "https://youtube.com/channel/username")
        self.assertEqual(homepage.x, "https://x.com/username")        
        self.assertEqual(str(homepage), "HomePgae")
