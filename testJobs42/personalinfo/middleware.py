from django.db import connection
from models import HttpStoredQuery

class QueryCountMiddleware(object):
    def process_request(self, request):
	req = HttpStoredQuery()
        req.path = request.path
        req.method = request.metod
	req.user = request.user
        req.save()
        return None

