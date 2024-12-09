from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import ImageBannerStrategic, Partner_Brands, Testimonial, Partner


class StrategicModelsTest(TestCase):

    def test_image_banner_strategic_creation(self):
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        image_banner_strategic = ImageBannerStrategic.objects.create(image_banner_strategic=image)
        self.assertTrue(image_banner_strategic.image_banner_strategic.name.startswith('Strategic/image_banner_strategic/'))
        self.assertEqual(str(image_banner_strategic), "Strategic")

    def test_partner_brands_creation(self):
        image = SimpleUploadedFile("partner_image.jpg", b"file_content", content_type="image/jpeg")
        image_banner_strategic = ImageBannerStrategic.objects.create(image_banner_strategic=image)
        partner_brand = Partner_Brands.objects.create(
            image_banner_strategic=image_banner_strategic,
            partner_image=image)
        self.assertTrue(partner_brand.partner_image.name.startswith('Strategic/partner_image/'))

    def test_testimonial_creation(self):
        image = SimpleUploadedFile("partner_image.jpg", b"file_content", content_type="image/jpeg")
        image_banner_strategic = ImageBannerStrategic.objects.create(image_banner_strategic=image)
        testimonial = Testimonial.objects.create(
            image_banner_strategic=image_banner_strategic,
            partner_title="Testimonial Title",
            partner_content="This is a testimonial content.",
            partner_image=image)
        self.assertEqual(testimonial.partner_title, "Testimonial Title")
        self.assertTrue(testimonial.partner_image.name.startswith('Strategic/partner_image/'))

    def test_partner_creation_with_slug(self):
        image = SimpleUploadedFile("partner_image.jpg", b"file_content", content_type="image/jpeg")
        image_banner_strategic = ImageBannerStrategic.objects.create(image_banner_strategic=image)
        testimonial = Testimonial.objects.create(
            image_banner_strategic=image_banner_strategic,
            partner_title="Partner Testimonial",
            partner_content="Content for partner testimonial",
            partner_image=image)
        
        partner = Partner.objects.create(
            Testimonial=testimonial,
            image_banner_strategic=image_banner_strategic,
            partner_title="Test Partner",
            partner_description="This is the partner description.",
            partner_main_image=image,
            first_person_name="John Doe",
            first_person_position="CEO",
            first_person_image=image,
            second_person_name="Jane Smith",
            second_person_position="CTO",
            second_person_image=image
        )
        
        self.assertEqual(partner.slug, "test-partner")
        self.assertTrue(partner.partner_main_image.name.startswith('Strategic/partner_main_image/'))
        self.assertEqual(str(partner), "Test Partner")

