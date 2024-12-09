from django.test import TestCase
from .models import Image_Banner, ContactInfo, ContactFormSubmission

class ContactModelsTest(TestCase):
    def test_create_image_banner(self):
        banner = Image_Banner.objects.create()
        self.assertEqual(str(banner), "Image Banner Contact Us")
    
    def test_create_contact_info(self):
        banner = Image_Banner.objects.create()
        contact = ContactInfo.objects.create(
            Image_Banner=banner,
            card_title="Test Card"
        )
        self.assertEqual(contact.card_title, "Test Card")
    
    def test_create_contact_form_submission(self):
        message = ContactFormSubmission.objects.create(
            name="Test User",
            email="test@example.com",
            phone=123456789,
            message="This is a test message"
        )
        self.assertEqual(message.name, "Test User")
