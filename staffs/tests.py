from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from staffs.models import StaffInfo
from datetime import date
from decimal import Decimal
from phonenumber_field.phonenumber import PhoneNumber
from django.core.exceptions import ValidationError

class StaffInfoModelTests(TestCase):
    
    def setUp(self):
        """Create a test staff record before each test runs."""
        self.staff = StaffInfo.objects.create(
            full_name="John Doe",
            phone_number="+2348031234567",  # Valid Nigerian phone number
            email="johndoe@example.com",
            home_address="123 Main Street, Lagos",
            date_of_birth=date(1990, 5, 15),
            state_of_origin="LA",  # Lagos
            emergence_phone_number="+2348037654321",
            start_date=date(2024, 4, 1),
            position_role="Driver",
            pay_rate=Decimal("50000.00"),
            bank_details="Bank Name: XYZ, Account Number: 1234567890",
            select_role="rider",  # Should be either 'rider' or 'staff'
            document_1=None,
            document_2=None
        )
    
    # TEST MODEL CREATION
    def test_staff_creation(self):
        """Check if the StaffInfo object is created successfully."""
        self.assertEqual(StaffInfo.objects.count(), 1)
        self.assertEqual(self.staff.full_name, "John Doe")

    #  TEST REQUIRED FIELDS
    def test_required_fields(self):
        """Ensure required fields raise errors when missing."""
        staff = StaffInfo(
            phone_number="+2348031234567",  # Missing required fields
        )
        with self.assertRaises(ValidationError):
            staff.full_clean()  # This method checks model validation

    # TEST CHOICE FIELD VALIDATION
    def test_invalid_select_role(self):
        """Ensure select_role only accepts 'rider' or 'staff'."""
        self.staff.select_role = "manager"  # Invalid choice
        with self.assertRaises(ValidationError):
            self.staff.full_clean()

    # TEST STATE CHOICES
    def test_invalid_state_of_origin(self):
        """Ensure state_of_origin only allows predefined states."""
        self.staff.state_of_origin = "XYZ"  # Invalid state
        with self.assertRaises(ValidationError):
            self.staff.full_clean()

    # TEST PHONE NUMBER VALIDATION
    def test_phone_number_format(self):
        """Ensure phone number is stored in correct format."""
        self.assertEqual(str(self.staff.phone_number), "+2348031234567")

    # TEST DECIMAL FIELD PAY RATE
    def test_pay_rate_precision(self):
        """Ensure pay_rate field handles decimal values correctly."""
        self.staff.pay_rate = Decimal("75000.50")  # Valid decimal
        self.staff.full_clean()
        self.assertEqual(self.staff.pay_rate, Decimal("75000.50"))

    # TEST STRING REPRESENTATION (__str__)
    def test_string_representation(self):
        """Ensure __str__ method returns correct string."""
        expected_string = "John Doe,  LA,   rider"
        self.assertEqual(str(self.staff), expected_string)

