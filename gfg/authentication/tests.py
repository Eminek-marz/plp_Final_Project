from django.test import TestCase

# Create your tests here.
from django.template import engines
from django.http import JsonResponse

def debug_template_paths(request):
    dirs = engines['django'].engine.dirs
    app_dirs = engines['django'].engine.app_dirs
    return JsonResponse({"dirs": dirs, "app_dirs": app_dirs})
