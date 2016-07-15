# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='active_duty',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='amount',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='annual_income',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='birth_day',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='birth_month',
            field=models.CharField(blank=True, choices=[(b'1', b'January'), (b'2', b'February'), (b'3', b'March'), (b'4', b'April'), (b'5', b'May'), (b'6', b'June'), (b'7', b'July'), (b'8', b'August'), (b'9', b'September'), (b'10', b'October'), (b'11', b'November'), (b'12', b'December')], max_length=9),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='branch_of_service',
            field=models.CharField(blank=True, choices=[('1', 'branch 1'), ('2', 'branch 2'), ('3', 'branch 3'), ('4', 'branch 4')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='citizenship',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='credit',
            field=models.CharField(choices=[('1', 'credit 1'), ('2', 'credit 2'), ('3', 'credit 3'), ('4', 'credit 4')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='credit_request_type',
            field=models.CharField(blank=True, choices=[('1', 'credit request type 1'), ('2', 'credit request type 2'), ('3', 'credit request type 3'), ('4', 'credit request type 4')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='duty_station',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email_address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='first_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='loan_amount',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='loan_type',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='loan_types',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AUTO LOAN (NEW)', 'Auto Loan (New)'), ('UNSERCURED PERSONAL LOAN (NEW)', 'Unsecured Personal Loan (New)'), ('SECURED PERSONAL LOAN', 'Secured Personal Loan'), ('AUTO LOAN (REFINANCE)', 'Auto Loan (Refinance)'), ('UNSECURED PERSONAL LOAN (REFINANCE)', 'Unsecured Personal Loan (Refinance)'), ('STUDENT LOANS', 'Student Loans'), ('HOME IMPROVEMENT', 'Home Improvement'), ('OTHER', 'Other')], max_length=163),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='mos',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='other_income',
            field=models.CharField(blank=True, choices=[('NONE', 'None'), ('OTHER', 'Other'), ('CHILD SUPPORT', 'Child Support'), ('ALIMONY', 'Alimony')], default='NONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='other_income_monthly',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='ownership',
            field=models.CharField(blank=True, choices=[('RENT', 'Rent'), ('OWN', 'Own')], max_length=4),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='password',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='purpose',
            field=models.CharField(choices=[('1', 'purpose 1'), ('2', 'purpose 2'), ('3', 'purpose 3'), ('4', 'purpose 4')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='rank_of_service',
            field=models.CharField(blank=True, choices=[('1', 'rank 1'), ('2', 'rank 2'), ('3', 'rank 3'), ('4', 'rank 4')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='reduced_income',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='repay',
            field=models.CharField(blank=True, choices=[('MONTHLY ALLOTMENT', 'Monthly Allotment'), ('MONTHLY BANK ACH', 'Monthly Bank ACH'), ('THE FEDERAL SAVINGS BANK CHECKING ACCOUNT', 'The Federal Savings Bank Checking Account (save up to 10%% on your loan)')], max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='service_years',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='social_security',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='state',
            field=models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='AL', max_length=2),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='street_address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='terminal_service_date',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='type_of_service',
            field=models.CharField(blank=True, choices=[('1', 'type 1'), ('2', 'type 2'), ('3', 'type 3'), ('4', 'type 4')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='year',
            field=models.IntegerField(blank=True, choices=[(1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='zip_code',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
