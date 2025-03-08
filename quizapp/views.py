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
class CreateQuiz(View):
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
        
# View untuk melihat detail tryout yang sudah ada
class ViewQuiz(View):
    model = Tryout
    def get(self, request, pk):
        tryout_object = get_object_or_404(self.model, pk=pk)
        ctx = {'tryout_object' : tryout_object}
        return render(request, 'quizapp/view_quiz.html',ctx)

# View untuk mengupdate tryout yang sudah ada
class UpdateQuiz(View):
    model = Tryout
    template_url = 'quizapp/update_quiz.html'

    def get(self, request, pk):
        # ambil object dari class Tryout dengan pk tertentu
        tryout_object = get_object_or_404(self.model, pk=pk)
        # buat form & "auto fill" sesuai dengan data object yg sudah disimpan 
        form = MakeTryout(instance=tryout_object)
        ctx = {'form' : form, 'tryout_object' : tryout_object}
        return render(request, self.template_url, ctx)
    
    def post(self, request, pk):
        tryout_object = get_object_or_404(self.model, pk=pk)
        form = MakeTryout(request.POST, instance=tryout_object)
        # jika form diisi dengan benar, save ke object Tryout lalu redirect ke home
        if form.is_valid():
            newTryout = form.save()
            success_url = reverse_lazy('view_quiz', kwargs={'pk': pk})
            return redirect(success_url)
        else:
        # jika tidak, minta user untuk mengisi kembali formnya 
            ctx = {'form' : form, 'tryout_object' : tryout_object}
            return render(request, self.template_url, ctx)

# View untuk mendelete tryout yang sudah ada
class DeleteQuiz(View):
    model = Tryout
    template_url = 'quizapp/delete_quiz.html'
    success_url = reverse_lazy('home')

    def get(self, request, pk):
        tryout_object = get_object_or_404(self.model, pk=pk)
        ctx = {'tryout_object' : tryout_object}
        return render(request, self.template_url, ctx)
    
    def post(self, request, pk):
        tryout_object = get_object_or_404(self.model, pk=pk)
        tryout_object.delete()
        return redirect(self.success_url)
