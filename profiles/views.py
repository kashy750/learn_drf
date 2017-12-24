import json
import datetime
from django.http import JsonResponse
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from profiles.models import Client,Package
from profiles.serializers import PackageSerializer 


class ProfileView(APIView):
	def validate_payload(self, payload):
		if 'client_id' not in payload:
			return False
		if payload['client_id'] is None or payload['client_id']=='':
			return False
		return True	


	def post(self, request):
		request_dict = request.data
		if not(self.validate_payload(request_dict)):
			raise APIException('Invalid request payload')

		client_id = int(request_dict['client_id'])	
		client = Client.objects.get(client_id = client_id)
		dob = client.birth_date
		gender = client.gender
		age = datetime.date.today().year-datetime.datetime.strptime(dob,'%d-%m-%Y').date().year
		package=Package.objects.filter(gender=gender,start_age__lte=age,end_age__gt=age)
		package_serializer=PackageSerializer(package,many=True)
		policy_list=[package['policy'] for package in package_serializer.data]
		return JsonResponse({'response':policy_list})





		