# from rest_framework.authentication import BaseAuthentication
# from rest_framework.permissions import BasePermission
# from rest_framework.throttling import BaseThrottle
# from rest_framework.versioning import QueryParameterVersioning, URLPathVersioning
# from rest_framework import serializers
# from rest_framework import validators
import time
from datetime import datetime
from dateutil.parser import parse
import json
time0 = parse('2022-07-19')
now = datetime.now()

print(now.year, now.month, now.day)
print((time.mktime(time0.timetuple())-time.mktime(now.timetuple()))>0)