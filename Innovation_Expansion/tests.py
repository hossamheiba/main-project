from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import ImageBannerInnovation, InnovationExpansion, InnovationMainPage


class InnovationModelsTest(TestCase):

    def test_image_banner_innovation_creation(self):
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        image_banner_innovation = ImageBannerInnovation.objects.create(image_banner_innovation=image)
        self.assertTrue(image_banner_innovation.image_banner_innovation.name.startswith('innovation/image_banner_innovation/'))
        self.assertEqual(str(image_banner_innovation), "Innovation & Expansion")

    def test_innovation_expansion_creation(self):
        image = SimpleUploadedFile("innovation_image.jpg", b"file_content", content_type="image/jpeg")
        image_banner_innovation = ImageBannerInnovation.objects.create(image_banner_innovation=image)
        innovation_expansion = InnovationExpansion.objects.create(
            image_banner_innovation=image_banner_innovation,
            innovation_image=image,
            innovation_title="Innovation Title",
            innovation_description="This is an innovation description."
        )
        self.assertEqual(innovation_expansion.innovation_title, "Innovation Title")
        self.assertTrue(innovation_expansion.innovation_image.name.startswith('innovation/innovation_card_image/'))

    def test_innovation_main_page_creation_with_slug(self):
        image = SimpleUploadedFile("innovation_image.jpg", b"file_content", content_type="image/jpeg")
        image_banner_innovation = ImageBannerInnovation.objects.create(image_banner_innovation=image)
        innovation_expansion = InnovationExpansion.objects.create(
            image_banner_innovation=image_banner_innovation,
            innovation_image=image,
            innovation_title="Innovation Title",
            innovation_description="Innovation Description"
        )
        
        innovation_main_page = InnovationMainPage.objects.create(
            innovationexpansion=innovation_expansion,
            ImageBannerInnovation=image_banner_innovation,
            detsils_innovation_image=image,
            detsils_innovation_title="Innovation Main Page",
            detsils_innovation_description="Details of innovation.",
            video=image  
        )
        
        self.assertEqual(innovation_main_page.slug, "innovation-main-page")
        self.assertTrue(innovation_main_page.detsils_innovation_image.name.startswith('innovation/detsils_innovation_image/'))
        self.assertTrue(innovation_main_page.video.name.startswith('innovation/videos_page/'))
        self.assertEqual(str(innovation_main_page), "Innovation Main Page")

