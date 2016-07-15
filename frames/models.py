from __future__ import unicode_literals
import calendar
from django import forms
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Applicant(models.Model):
    """
    WIREFRAME 1
    """
    #how much do you need?
    amount = models.CharField(max_length=200, blank=True, null=True)
    #what is it for?
    PURPOSE_1 = 'What is it for?'
    PURPOSE_2 = '2'
    PURPOSE_3 = '3'
    PURPOSE_4 = '4'
    PURPOSE_CHOICES = (
        (PURPOSE_1, 'purpose 1'),
        (PURPOSE_2, 'purpose 2'),
        (PURPOSE_3, 'purpose 3'),
        (PURPOSE_4, 'purpose 4'),
    )
    purpose = models.CharField(
        max_length=200,
        choices=PURPOSE_CHOICES,
        blank=True,
        null=True,
    )

    #how is your credit?
    CREDIT_1 = 'How is your credit?'
    CREDIT_2 = '2'
    CREDIT_3 = '3'
    CREDIT_4 = '4'
    CREDIT_CHOICES = (
        (CREDIT_1, 'credit 1'),
        (CREDIT_2, 'credit 2'),
        (CREDIT_3, 'credit 3'),
        (CREDIT_4, 'credit 4'),
    )
    credit = models.CharField(
        max_length=200,
        choices=CREDIT_CHOICES,
        blank=True,
        null=True,
    )

    """
    WIREFRAME 2
    """
    #first name
    first_name = models.CharField(max_length=200, blank=True, null=True)

    #last name
    last_name = models.CharField(max_length=200, blank=True, null=True)

    #address
    street_address = models.CharField(max_length=200, blank=True, null=True)

    #city
    city = models.CharField(max_length=200, blank=True, null=True)

    #state
    ALABAMA = 'AL'
    ALASKA = 'AK'
    ARIZONA = 'AZ'
    ARKANSAS = 'AR'
    CALIFORNIA = 'CA'
    COLORADO = 'CO'
    CONNECTICUT = 'CT'
    DELAWARE = 'DE'
    FLORIDA = 'FL'
    GEORGIA = 'GA'
    HAWAII = 'HI'
    IDAHO = 'ID'
    ILLINOIS = 'IL'
    INDIANA = 'IN'
    IOWA = 'IA'
    KANSAS = 'KS'
    KENTUCKY = 'KY'
    LOUISIANA = 'LA'
    MAINE = 'ME'
    MARLAND = 'MD'
    MASSACHUSETTS = 'MA'
    MICHIGAN = 'MI'
    MINNESOTA = 'MN'
    MISSISSIPPI = 'MS'
    MISSOURI = 'MO'
    MONTANA = 'MT'
    NEBRASKA = 'NE'
    NEVADA = 'NV'
    NEW_HAMPSHIRE = 'NH'
    NEW_JERSEY = 'NJ'
    NEW_MEXICO = 'NM'
    NEW_YORK = 'NY'
    NORTH_CAROLINA = 'NC'
    NORTH_DAKOTA = 'ND'
    OHIO = 'OH'
    OKLAHOMA = 'OK'
    OREGON = 'OR'
    PENNSYLVANIA = 'PA'
    RHODE_ISLAND = 'RI'
    SOUTH_CAROLINA = 'SC'
    SOUTH_DAKOTA = 'SD'
    TENNESSEE = 'TN'
    TEXAS = 'TX'
    UTAH = 'UT'
    VERMONT = 'VT'
    VIRGINIA = 'VA'
    WASHINGTON = 'WA'
    WEST_VIRGINIA = 'WV'
    WISCONSIN = 'WI'
    WYOMING = 'WY'
    STATE_CHOICES = (
        (ALABAMA, 'Alabama'),
        (ALASKA, 'Alaska'),
        (ARIZONA, 'Arizona'),
        (ARKANSAS, 'Arkansas'),
        (CALIFORNIA, 'California'),
        (COLORADO, 'Colorado'),
        (CONNECTICUT, 'Connecticut'),
        (DELAWARE, 'Delaware'),
        (FLORIDA, 'Florida'),
        (GEORGIA, 'Georgia'),
        (HAWAII, 'Hawaii'),
        (IDAHO, 'Idaho'),
        (ILLINOIS, 'Illinois'),
        (INDIANA, 'Indiana'),
        (IOWA, 'Iowa'),
        (KANSAS, 'Kansas'),
        (KENTUCKY, 'Kentucky'),
        (LOUISIANA, 'Louisiana'),
        (MAINE, 'Maine'),
        (MASSACHUSETTS, 'Massachusetts'),
        (MICHIGAN, 'Michigan'),
        (MINNESOTA, 'Minnesota'),
        (MISSISSIPPI, 'Mississippi'),
        (MISSOURI, 'Missouri'),
        (MONTANA, 'Montana'),
        (NEBRASKA, 'Nebraska'),
        (NEVADA, 'Nevada'),
        (NEW_HAMPSHIRE, 'New Hampshire'),
        (NEW_JERSEY, 'New Jersey'),
        (NEW_MEXICO, 'New Mexico'),
        (NEW_YORK, 'New York'),
        (NORTH_CAROLINA, 'North Carolina'),
        (NORTH_DAKOTA, 'North Dakota'),
        (OHIO, 'Ohio'),
        (OKLAHOMA, 'Oklahoma'),
        (OREGON, 'Oregon'),
        (PENNSYLVANIA, 'Pennsylvania'),
        (RHODE_ISLAND, 'Rhode Island'),
        (SOUTH_CAROLINA, 'South Carolina'),
        (SOUTH_DAKOTA, 'South Dakota'),
        (TENNESSEE, 'Tennessee'),
        (TEXAS, 'Texas'),
        (UTAH, 'Utah'),
        (VERMONT, 'Vermont'),
        (VIRGINIA, 'Virginia'),
        (WASHINGTON, 'Washington'),
        (WEST_VIRGINIA, 'West Virginia'),
        (WISCONSIN, 'Wisconsin'),
        (WYOMING, 'Wyoming'),
    )
    state = models.CharField(
        max_length=200,
        choices=STATE_CHOICES,
        blank=True,
        null=True,
    )

    #zip code
    zip_code = models.CharField(max_length=200, blank=True, null=True)

    #birth month
    JANUARY = 'JAN'
    FEBRUARY = 'FEB'
    MARCH = 'MAR'
    APRIL = 'APR'
    MAY = 'MAY'
    JUNE = 'JUN'
    JULY = 'JUL'
    AUGUST = 'AUG'
    SEPTEMBER = 'SEP'
    OCTOBER = 'OCT'
    NOVEMBER = 'NOV'
    DECEMBER = 'DEC'
    MONTH_CHOICES = (
        (JANUARY, 'January'),
        (FEBRUARY, 'February'),
        (MARCH, 'March'),
        (APRIL, 'April'),
        (MAY, 'May'),
        (JUNE, 'June'),
        (JULY, 'July'),
        (AUGUST, 'August'),
        (SEPTEMBER, 'September'),
        (OCTOBER, 'October'),
        (NOVEMBER, 'November'),
        (DECEMBER, 'December'),
    )
    birth_month = models.CharField(
        max_length=200,
        choices=MONTH_CHOICES,
        blank=True,
        null=True,
    )

    #birth day
    DAY_CHOICES = [ (i, i) for i in range(1, 32) ]
    birth_day = models.IntegerField(
        choices=DAY_CHOICES,
        blank=True,
        null=True,
    )

    #birth year
    YEAR_CHOICES = [ (i, i) for i in range(1920, 2017) ]
    birth_year = models.IntegerField(
        choices=YEAR_CHOICES,
        blank=True,
        null=True,
    )

    #annual income
    annual_income = models.CharField(max_length=200, blank=True, null=True)

    #email
    email = models.CharField(max_length=200, blank=True, null=True)

    #password
    password = models.CharField(max_length=200, blank=True, null=True)

    """
    WIREFRAME 3
    """

    #do you rent or own?
    RENT = 'rent'
    OWN = 'own'
    OWNERSHIP_CHOICES = (
        (RENT, 'Rent'),
        (OWN, 'Own')
    )
    ownership = models.CharField(
        max_length=200,
        choices=OWNERSHIP_CHOICES,
        blank=True,
        null=True,
    )

    #are you a u.s. citizen?
    YES_CITIZEN = 'yes'
    NO_CITIZEN = 'yes'
    CITIZENSHIP_CHOICES = (
        (YES_CITIZEN, 'Yes'),
        (NO_CITIZEN, 'No')
    )
    citizenship = models.CharField(
        max_length=200,
        choices=CITIZENSHIP_CHOICES,
        blank=True,
        null=True,
    )

    #email address
    email_address = models.CharField(max_length=200, blank=True, null=True)

    #social security number
    social_security = models.CharField(max_length=200, blank=True, null=True)

    #are you active duty military?
    YES_ACTIVE_DUTY = 'yes'
    NO_ACTIVE_DUTY = 'no'
    ACTIVE_DUTY_CHOICES = (
        (YES_ACTIVE_DUTY, 'Yes'),
        (NO_ACTIVE_DUTY, 'No')
    )
    active_duty = models.CharField(
        max_length=200,
        choices=ACTIVE_DUTY_CHOICES,
        blank=True,
        null=True,
    )

    #terminal service date
    terminal_service_date = models.CharField(max_length=200, blank=True, null=True)

    #branch of service
    BRANCH_1 = 'Branch of Service'
    BRANCH_2 = '2'
    BRANCH_3 = '3'
    BRANCH_4 = '4'
    BRANCH_CHOICES = (
        (BRANCH_1, 'branch 1'),
        (BRANCH_2, 'branch 2'),
        (BRANCH_3, 'branch 3'),
        (BRANCH_4, 'branch 4'),
    )
    service_branch = models.CharField(
        max_length=200,
        choices=BRANCH_CHOICES,
        blank=True,
        null=True,
    )

    #type of service
    TYPE_1 = 'Type of Service'
    TYPE_2 = '2'
    TYPE_3 = '3'
    TYPE_4 = '4'
    TYPE_CHOICES = (
        (TYPE_1, 'type 1'),
        (TYPE_2, 'type 2'),
        (TYPE_3, 'type 3'),
        (TYPE_4, 'type 4'),
    )
    service_type = models.CharField(
        max_length=200,
        choices=TYPE_CHOICES,
        blank=True,
        null=True,
    )

    #rank of service
    RANK_1 = 'Rank of Service'
    RANK_2 = '2'
    RANK_3 = '3'
    RANK_4 = '4'
    RANK_CHOICES = (
        (RANK_1, 'rank 1'),
        (RANK_2, 'rank 2'),
        (RANK_3, 'rank 3'),
        (RANK_4, 'rank 4'),
    )
    rank = models.CharField(
        max_length=200,
        choices=RANK_CHOICES,
        blank=True,
        null=True,
    )

    #MOS
    mos = models.CharField(max_length=200, blank=True, null=True)

    #years of service
    service_years = models.CharField(max_length=200, blank=True, null=True)

    #duty station
    duty_station = models.CharField(max_length=200, blank=True, null=True)

    #other sources of income
    NONE = 'none'
    OTHER = 'other'
    CHILD_SUPPORT = 'child_support'
    ALIMONY = 'alimony'
    OTHER_CHOICES = (
        (NONE, 'None'),
        (OTHER, 'Other'),
        (CHILD_SUPPORT, 'Child Support'),
        (ALIMONY, 'Alimony')
    )
    other_income = models.CharField(
        max_length=200,
        choices=OTHER_CHOICES,
        blank=True,
        null=True,
    )

    #total/month
    other_income_monthly = models.CharField(max_length=200, blank=True, null=True)

    #is any of the income above likely to be reduced before the credit request
    #is paid off?
    YES_REDUCED = 'yes'
    NO_REDUCED = 'no'
    REDUCED_INCOME_CHOICES = (
        (YES_REDUCED, 'Yes'),
        (NO_REDUCED, 'No')
    )
    reduced_income = models.CharField(
        max_length=200,
        choices=REDUCED_INCOME_CHOICES,
        blank=True,
        null=True,
    )

    #please explain
    reduced_income_explanation = models.TextField(blank=True, null=True)

    """
    WIREFRAME 4
    """

    #type of credit requesting
    CREDIT_REQUEST_TYPE_1 = 'Type of Credit Requesting'
    CREDIT_REQUEST_TYPE_2 = '2'
    CREDIT_REQUEST_TYPE_3 = '3'
    CREDIT_REQUEST_TYPE_4 = '4'
    CREDIT_REQUEST_TYPE_CHOICES = (
        (CREDIT_REQUEST_TYPE_1, 'credit request type 1'),
        (CREDIT_REQUEST_TYPE_2, 'credit request type 2'),
        (CREDIT_REQUEST_TYPE_3, 'credit request type 3'),
        (CREDIT_REQUEST_TYPE_4, 'credit request type 4'),
    )
    credit_request_type = models.CharField(
        max_length=200,
        choices=CREDIT_REQUEST_TYPE_CHOICES,
        blank=True,
        null=True,
    )

    #type(s) of loans that you are applying for. check all that apply
    AUTO_LOAN_NEW = 'auto_loan_new'
    UNSECURED_PERSONAL_LOAN_NEW = 'unsecured_personal_loan_new'
    SECURED_PERSONAL_LOAN = 'secured_personal_loan'
    AUTO_LOAN_REFINANCE = 'auto_loan_refinance'
    UNSECURED_PERSONAL_LOAN_REFINANCE = 'unsecured_personal_loan_refinance'
    STUDENT_LOANS = 'student_loans'
    HOME_IMPROVEMENT = 'home_improvement'
    OTHER = 'other'
    LOAN_TYPE_CHOICES = (
        (AUTO_LOAN_NEW, 'Auto Loan (New)'),
        (UNSECURED_PERSONAL_LOAN_NEW, 'Unsecured Personal Loan (New)'),
        (SECURED_PERSONAL_LOAN, 'Secured Personal Loan'),
        (AUTO_LOAN_REFINANCE, 'Auto Loan (Refinance)'),
        (UNSECURED_PERSONAL_LOAN_REFINANCE, 'Unsecured Personal Loan (Refinance)'),
        (STUDENT_LOANS, 'Student Loans'),
        (HOME_IMPROVEMENT, 'Home Improvement'),
        (OTHER, 'Other')
    )
    loan_types = MultiSelectField(choices=LOAN_TYPE_CHOICES, blank=True, null=True)

    #type of loan
    loan_type = models.CharField(max_length=200, blank=True, null=True)

    #loan amount
    loan_amount = models.CharField(max_length=200, blank=True, null=True)

    #want to repay:
    MONTHLY_ALLOTMENT = 'monthly_allotment'
    MONTHLY_BANK_ACH = 'monthly_bank_ach'
    THE_FEDERAL_SAVINGS_BANK_CHECKING_ACCOUNT = 'federal_savings'
    REPAY_CHOICES = (
        (MONTHLY_ALLOTMENT, 'Monthly Allotment'),
        (MONTHLY_BANK_ACH, 'Monthly Bank ACH'),
        (THE_FEDERAL_SAVINGS_BANK_CHECKING_ACCOUNT, 'The Federal Savings Bank Checking Account (save up to 10 percent on your loan)')
    )
    repay = models.CharField(
        max_length=200,
        choices=REPAY_CHOICES,
        blank=True,
        null=True,
    )
