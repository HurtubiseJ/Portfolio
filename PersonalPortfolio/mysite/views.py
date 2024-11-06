from django.shortcuts import render
from django.views import View


class index_view(View):
    def get(self, request):
        return render(request, 'index.html')

class resume_view(View):
    def get(self, request):
        return render(request, 'resume.html')

class projects_view(View):
    def get(self, request):
        return render(request, 'projects.html')

class about_view(View):
    def get(self, request):
        return render(request, 'about.html')