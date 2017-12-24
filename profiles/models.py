from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProductType(models.Model):
	product_type_id = models.IntegerField()
	name = models.CharField(max_length = 45)

class ProductCategory(models.Model):
	product_category_id = models.IntegerField()
	name = models.CharField(max_length = 45)
	product_type = models.ForeignKey(ProductType)


class Company(models.Model):
	company_id = models.IntegerField()
	name = models.CharField(max_length = 45)
	business_registration = models.CharField(max_length = 45)
	company_type = models.CharField(max_length = 1)


class Product(models.Model):
	product_id = models.IntegerField()
	name = models.CharField(max_length = 45)
	sub_category = models.CharField(max_length = 45)
	company = models.ForeignKey(Company)
	product_category = models.ForeignKey(ProductCategory)


class Client(models.Model):
	client_id = models.IntegerField()
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	identification_no = models.CharField(max_length = 45)
	birth_date = models.CharField(max_length=10)
	gender = models.CharField(max_length = 1)
	salutation = models.CharField(max_length = 1)            #salutation size
	nationality = models.CharField(max_length = 45)            # CHANGED INT to VARCHAR
	profession = models.CharField(max_length = 45)
	income_range = models.CharField(max_length = 45)
	smoker = models.IntegerField()						   # SMOKER
	company = models.ForeignKey(Company)


class Policy(models.Model):
	policy_id = models.IntegerField()                        # CHANGED id_product to policy_id
	product_no = models.CharField(max_length = 45)	           # CHECk product_no or policy_no
	status = models.CharField(max_length = 1)
	sum_assured = models.CharField(max_length = 45)
	term_years = models.CharField(max_length = 45)
	premiums = models.CharField(max_length = 45)
	product = models.ForeignKey(Product)

# class ClientPolicy(models.Model)
# 	product_no=models.CharField(max_length=45)
# 	policy=models.ForeignKey(Policy)
# 	client=models.ForeignKey(Client)


class Users(models.Model):
	user_id=models.IntegerField()
	email=models.CharField(max_length=200)
	password=models.CharField(max_length=45)
	registration_date=models.CharField(max_length=10)
	client=models.ForeignKey(Client)
	email_verified=models.BooleanField()
	mobile_verified=models.BooleanField()


class Package(models.Model):
	gender = models.CharField(max_length=1)
	start_age = models.IntegerField()
	end_age = models.IntegerField()
	policy=models.ForeignKey(Policy)
