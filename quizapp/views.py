from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
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
    template_url = 'quizapp/create_quiz.html'
    success_url = reverse_lazy('home')

    def get(self, request):
        form = MakeTryout()
        ctx = {'form' : form}
        return render(request, self.template_url, ctx)
    
    def post(self, request):
        form = MakeTryout(request.POST)
        # jika form diisi dengan benar, save ke object Tryout lalu redirect ke home
        if form.is_valid():
            newTryout = form.save()
            return redirect(self.success_url)
        else:
        # jika tidak, minta user untuk mengisi kembali formnya 
            ctx = {'form' : form}
            return render(request, self.template_url, ctx)

# View untuk mengupdate tryout yang sudah ada
class UpdateView(View):
    def get(self, request):
        return render(request, 'quizapp/update_quiz.html')

# View untuk mendelete tryout yang sudah ada
class DeleteView(View):
    def get(self, request):
        return render(request, 'quizapp/delete_quiz.html')
