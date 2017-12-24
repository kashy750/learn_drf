from rest_framework import serializers
from profiles.models import *  


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'		

class PolicySerializer(serializers.ModelSerializer):
	product = ProductSerializer()

	class Meta:
		model = Policy
		fields = '__all__'	

class PackageSerializer(serializers.ModelSerializer):
	policy = PolicySerializer()

	class Meta:
		model = Package
		fields = '__all__'