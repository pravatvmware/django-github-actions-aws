from django.http import HttpResponse

def home(request):
   text = """<h1>Nice! This Appliaction is running on AWS EB environment V7</h1>"""
   return HttpResponse(text)