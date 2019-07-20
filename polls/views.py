from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world your at the polls index.")

# Create your views here.
