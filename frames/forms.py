from django import forms

from .models import Applicant

class ApplicantForm1(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'amount',
            'purpose',
            'credit',
        ]

class ApplicantForm2(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'first_name',
            'last_name',
            'city',
            'state',
            'zip_code',
            'birth_month',
            'birth_day',
            'birth_year',
            'annual_income',
            'email',
            'password',
        ]

class ApplicantForm3(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'ownership',
            'citizenship',
            'email_address',
            'social_security',
            'active_duty',
            'terminal_service_date',
            'service_branch',
            'service_type',
            'rank',
            'mos',
            'service_years',
            'duty_station',
            'other_income',
            'other_income_monthly',
            'reduced_income',
            'reduced_income_explanation',
        ]

class ApplicantForm4(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'credit_request_type',
            'loan_types',
            'loan_type',
            'repay',
        ]
        
