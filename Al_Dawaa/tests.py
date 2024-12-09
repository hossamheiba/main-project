from django.urls import reverse
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import (
    We_Aldawaa, Feature, TimelineEvent, ImageBannerDepartment, AlDawaaDepartmentCard,
    Department_Inside_Page, Social_Responsibility, Card_Social_Responsibility, 
    Social_Responsibility_details, Image_Banner_Program, Program
)

class WeAldawaaTestCase(TestCase):
    def setUp(self):
        # Model setup
        self.we_aldawaa = We_Aldawaa.objects.create(
            section_title="Test Section",
            section_description="Test Description",
            section_image=self.create_test_image(),
        )
        self.timeline_event = TimelineEvent.objects.create(
            icon=self.we_aldawaa,
            Time_line_year=2024,
            Time_line_description="Test Timeline Event Description",
        )
        self.image_banner_department = ImageBannerDepartment.objects.create(
            image_banner_department=self.create_test_image(),
        )
        self.department_card = AlDawaaDepartmentCard.objects.create(
            image_banner=self.image_banner_department,
            department_title="Test Department",
            department_description="Test Department Description",
            department_image_or_icon=self.create_test_image(),
            department_bg_color="#FFFFFF",
            department_text_color="#000000"
        )
        self.department_inside_page = Department_Inside_Page.objects.create(
            category=self.department_card,
            ImageBannerDepartment=self.image_banner_department,
            section_title="Test Department Inside Page",
            section_description="Test Section Description",
            section_image=self.create_test_image(),
        )
        self.social_responsibility = Social_Responsibility.objects.create(
            page_title="Test Social Responsibility",
            page_description="Test Social Responsibility Description",
            image_banner=self.create_test_image(),
        )
        self.card_social_responsibility = Card_Social_Responsibility.objects.create(
            image_banner=self.social_responsibility,
            card_title="Test Card Social Responsibility",
            card_description="Test Card Social Responsibility Description",
            card_image=self.create_test_image(),
        )
        self.social_responsibility_details = Social_Responsibility_details.objects.create(
            Card_Social_Responsibility=self.card_social_responsibility,
            title_details_social="Test Title",
            description_details_social="Test Description",
            image_details_social=self.create_test_image(),
        )
        self.image_banner_program = Image_Banner_Program.objects.create(
            image_banner_program=self.create_test_image(),
        )

    def create_test_image(self):
        return SimpleUploadedFile(
            name='test_image.jpg',
            content=b'file_content',
            content_type='image/jpeg'
        )
