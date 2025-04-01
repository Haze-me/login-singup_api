from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class StaffInfo(models.Model):
      
    choice_pick = [
        
        ('rider', 'Rider'),
        ('staff', 'Staff'),
        
        ]
      
    STATES_IN_NIGERIA = [
        ('AB', 'Abia'),
        ('AD', 'Adamawa'),
        ('AK', 'Akwa Ibom'),
        ('AN', 'Anambra'),
        ('BA', 'Bauchi'),
        ('BE', 'Benue'),
        ('BO', 'Borno'),
        ('CR', 'Cross River'),
        ('DE', 'Delta'),
        ('EB', 'Ebonyi'),
        ('ED', 'Edo'),
        ('EK', 'Ekiti'),
        ('EN', 'Enugu'),
        ('GO', 'Gombe'),
        ('IM', 'Imo'),
        ('JO', 'Jigawa'),
        ('KD', 'Kaduna'),
        ('KN', 'Kano'),
        ('KO', 'Kogi'),
        ('KT', 'Katsina'),
        ('KW', 'Kwara'),
        ('LA', 'Lagos'),
        ('NA', 'Nasarawa'),
        ('NI', 'Niger'),
        ('OG', 'Ogun'),
        ('ON', 'Ondo'),
        ('OS', 'Osun'),
        ('OY', 'Oyo'),
        ('PL', 'Plateau'),
        ('RI', 'Rivers'),
        ('SO', 'Sokoto'),
        ('TA', 'Taraba'),
        ('YO', 'Yobe'),
        ('ZA', 'Zamfara'),
    ]
    
    full_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(region='NG')
    email = models.EmailField()
    home_address = models.CharField(max_length=500)
    date_of_birth = models.DateField()  
    state_of_origin = models.CharField(max_length=20, choices=STATES_IN_NIGERIA) 
    emergence_phone_number = PhoneNumberField(region='NG')
    start_date = models.DateField()
    position_role = models.CharField(max_length=255)
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
    bank_details = models.TextField()
    select_role = models.CharField(max_length=20, choices=choice_pick, default='rider')
    document_1 = models.FileField(upload_to='staff_documents/', blank=True, null=True)
    document_2 = models.FileField(upload_to='staff_documents/', blank=True, null=True)

    
    def __str__(self):
        return f"{self.full_name},  {self.state_of_origin},   {self.select_role}"
