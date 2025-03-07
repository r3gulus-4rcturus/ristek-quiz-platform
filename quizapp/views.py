from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from quizapp.models import Tryout
from quizapp.forms import MakeTryout

# View untuk menampilkan list semua try out yang ada
class MainView(View):
    def get(self, request):
        # ambil semua object tryout yang ada
        tryout_list = Tryout.objects.all()
        # pass ke render machine 
        ctx = {'tryout_list': tryout_list}
        return render(request, 'quizapp/home.html', ctx)
    
class AboutView(View):
    def get(self, request):
        return render(request, 'quizapp/about_page.html')
    
class ContactView(View):
    def get(self, request):
        return render(request, 'quizapp/contact.html')
    
# View untuk membuat tryout baru
class CreateView(View):
    def get(self, request):
        return render(request, 'quizapp/create_quiz.html')
    
    def post(self, request):
        

# View untuk mengupdate tryout yang sudah ada
class UpdateView(View):
    def get(self, request):
        return render(request, 'quizapp/update_quiz.html')

# View untuk mendelete tryout yang sudah ada
class DeleteView(View):
    def get(self, request):
        return render(request, 'quizapp/delete_quiz.html')
