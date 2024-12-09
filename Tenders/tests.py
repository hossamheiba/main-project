from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Image_Banner_Tender, TenderCategory, Tender

class ImageBannerTenderModelTest(TestCase):
    def setUp(self):
        self.image_banner = Image_Banner_Tender.objects.create(
            image_banner_tender=SimpleUploadedFile(
                "test_image.jpg", b"image_data", content_type="image/jpeg"
            )
        )

    def test_image_banner_str(self):
        self.assertEqual(str(self.image_banner), "Tenders")

    def test_image_tag(self):
        image_tag = self.image_banner.image_tag()
        self.assertIn('<img src="', image_tag)  

    def test_image_banner_blank(self):
        image_banner_blank = Image_Banner_Tender.objects.create(image_banner_tender=None)
        self.assertEqual(str(image_banner_blank), "Tenders")

class TenderCategoryModelTest(TestCase):
    def setUp(self):
        self.image_banner = Image_Banner_Tender.objects.create(
            image_banner_tender=SimpleUploadedFile(
                "test_image.jpg", b"image_data", content_type="image/jpeg"
            )
        )
        self.tender_category = TenderCategory.objects.create(
            image_banner=self.image_banner,
            tender_title="Test Tender Category",
            tender_image_or_icon=SimpleUploadedFile(
                "test_icon.png", b"icon_data", content_type="image/png"
            )
        )

    def test_tender_category_str(self):
        self.assertEqual(str(self.tender_category), "Test Tender Category")

class TenderModelTest(TestCase):
    def setUp(self):
        self.image_banner = Image_Banner_Tender.objects.create(
            image_banner_tender=SimpleUploadedFile(
                "test_image.jpg", b"image_data", content_type="image/jpeg"
            )
        )
        self.tender_category = TenderCategory.objects.create(
            image_banner=self.image_banner,
            tender_title="Test Tender Category",
            tender_image_or_icon=SimpleUploadedFile(
                "test_icon.png", b"icon_data", content_type="image/png"
            )
        )
        self.tender = Tender.objects.create(
            category=self.tender_category,
            image_banner=self.image_banner,
            category_title="Test Tender",
            category_pdf_file=SimpleUploadedFile(
                "test_pdf.pdf", b"pdf_data", content_type="application/pdf"
            ),
            category_description="This is a test description for the tender."
        )

    def test_tender_str(self):
        self.assertEqual(str(self.tender), "Test Tender")

    def test_tender_fields(self):
        self.assertEqual(self.tender.category_title, "Test Tender")
        self.assertEqual(self.tender.category_description, "This is a test description for the tender.")
        uploaded_filename = self.tender.category_pdf_file.name.split('/')[-1]
        self.assertTrue(uploaded_filename.startswith("test_pdf") and uploaded_filename.endswith(".pdf"))
