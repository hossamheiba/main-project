from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *

class AboutUsModelTest(TestCase):
    def setUp(self):
        self.image_file = SimpleUploadedFile(
            "test_image.jpg", 
            b"file_content", 
            content_type="image/jpeg"
        )

        self.about_us = About_Us.objects.create(
            image_banner=self.image_file,  
            video=None,
            image=self.image_file,
            Years_Of_Experienced=10,
            description="Test description of About Us."
        )

    def test_about_us_str(self):
        self.assertEqual(str(self.about_us), "About_Us")
    
    def test_years_of_experience(self):
        self.assertEqual(self.about_us.Years_Of_Experienced, 10)

    def test_description(self):
        self.assertEqual(self.about_us.description, "Test description of About Us.")

    def test_image_tag_with_image(self):
        image_tag = self.about_us.image_tag()
        self.assertIn('src', image_tag)  

    def test_image_tag_no_image(self):
        self.about_us.image_banner = None
        self.about_us.save()
        image_tag = self.about_us.image_tag()
        self.assertEqual(image_tag, "No Image")
class CardModelTest(TestCase):
    def setUp(self):
        self.image_file = SimpleUploadedFile(
            "test_card_image.jpg", 
            b"file_content", 
            content_type="image/jpeg"
        )

        self.about_us = About_Us.objects.create(
            image_banner=self.image_file,
            video=None,
            image=self.image_file,
            Years_Of_Experienced=10,
            description="Test description"
        )

        self.card = Card.objects.create(
            card=self.about_us,
            image_card=self.image_file,  
            title_card="Test Card Title",
            description_card="Test Card Description",
            is_collapsible=True,
            collapse_description="Test Collapse Description"
        )

    def test_card_str(self):
        self.assertEqual(str(self.card), "Test Card Title")

    def test_is_collapsible(self):
        self.assertTrue(self.card.is_collapsible)

    def test_description_card(self):
        self.assertEqual(self.card.description_card, "Test Card Description")

    def test_collapse_description(self):
        self.assertEqual(self.card.collapse_description, "Test Collapse Description")
class ImageBannerModelTest(TestCase):
    def setUp(self):
        self.image_file = SimpleUploadedFile(
            "test_banner_image.jpg", 
            b"file_content", 
            content_type="image/jpeg"
        )

        self.image_banner = Image_Banner.objects.create(
            image_banner=self.image_file 
        )

    def test_image_banner_str(self):
        self.assertEqual(str(self.image_banner), "Board Of Directors")

    def test_image_tag_with_image(self):
        image_tag = self.image_banner.image_tag()
        self.assertIn('src', image_tag)  

    def test_image_tag_no_image(self):
        self.image_banner.image_banner = None
        self.image_banner.save()
        image_tag = self.image_banner.image_tag()
        self.assertEqual(image_tag, "No Image")
class BoardMemberModelTest(TestCase):
    def setUp(self):
        self.image_file = SimpleUploadedFile(
            "test_person_image.jpg", 
            b"file_content", 
            content_type="image/jpeg"
        )
        self.image_banner = Image_Banner.objects.create(
            image_banner=self.image_file  
        )

        self.board_member = BoardMember.objects.create(
            image_banner=self.image_banner,
            person_name="John Doe",
            person_position="CEO",
            person_image=self.image_file  
        )

    def test_board_member_str(self):
        self.assertEqual(str(self.board_member), "John Doe")

    def test_person_position(self):
        self.assertEqual(self.board_member.person_position, "CEO")

    def test_person_image(self):
        self.assertIsNotNone(self.board_member.person_image)
class BrandsModelTest(TestCase):
    def setUp(self):
        self.image_file = SimpleUploadedFile(
            "test_brand_image.jpg", 
            b"file_content", 
            content_type="image/jpeg"
        )
        self.image_banner_brand = Image_Banner_Brand.objects.create(
            image_banner_brand=self.image_file 
        )

        self.brand = Brands.objects.create(
            image_banner_brand=self.image_banner_brand,
            brand_name="Test Brand",
            brand_image=self.image_file  
        )

    def test_brands_str(self):
        self.assertEqual(str(self.brand), "Test Brand")
    
    def test_brand_name(self):
        self.assertEqual(self.brand.brand_name, "Test Brand")

    def test_brand_image(self):
        self.assertIsNotNone(self.brand.brand_image)
