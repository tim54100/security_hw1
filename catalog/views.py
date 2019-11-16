from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import hashlib

def hello_world(request):
    return HttpResponse("Hello World!")
# def hash_text(request, input_text):
#     """View function for home page of site."""
#     print(input_text)
#     h = hashlib.sha256()
# #     print(request.json())
#     h.update(input_text.encode('utf-8'))
    
    
#     context = {
#         'hash_text': h.hexdigest(),
#     }

#     return render(request, './website/index.html', context=context)
def hash_text(request, input_text):

    # Generate counts of some of the main objects
#     input_text = request.GET['input_text']
    print(input_text)
    h = hashlib.sha256()
#     print(request.json())
    h.update(input_text.encode('utf-8'))
    
    
    context = {
        'hash_text': h.hexdigest(),
    }
    
    # Render the HTML template index.html with the data in the context variable
    return HttpResponse(h.hexdigest())
def index(request):
    """View function for home page of site."""
    value = ""
#     try:
#         h = hashlib.sha256()
#         h.update("123".encode('utf-8'))
#         value =  h.hexdigest()
#     except:
#         pass
    context = {
        'hash_text': value,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, './website/index.html', context=context)