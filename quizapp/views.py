from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from quizapp.models import *
from quizapp.forms import *
from quizapp.filters import TryoutFilter

# View untuk menampilkan list semua try out yang ada
class MainView(View):
    def get(self, request):
        # ambil semua object tryout yang ada
        tryout_list = Tryout.objects.all()

        # filter pencarian tryout menggunakan django_filters
        tryout_filter = TryoutFilter(request.GET, queryset=tryout_list)
        tryout_list_filtered = tryout_filter.qs

        # pass ke render machine 
        ctx = {'tryout_list': tryout_list_filtered, 'tryout_filter': tryout_filter}
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
        # ambil object tryout
        tryout_object = get_object_or_404(self.model, pk=pk)
        # ambil daftar question yg ada di dalam tryout tersebut
        question_list = tryout_object.question_set.all()
        ctx = {'tryout_object' : tryout_object, 'question_list' : question_list}
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

# View untuk menambahkan question
class AddQuestion(View):
    template_url = 'quizapp/add_question.html'

    # pk_tryout = primary key tryout, tryout dimana question ini berasal 
    def get(self, request, pk_tryout):
        form = MakeQuestion()
        ctx = {'form' : form, 'pk_tryout' : pk_tryout}
        return render(request, self.template_url, ctx)
    
    def post(self, request, pk_tryout):
        form = MakeQuestion(request.POST)
        # jika form diisi dengan benar, save ke object Question lalu redirect ke page update quiz
        # yakni tryout dimana question ini berasal.
        if form.is_valid():
            # ambil object tryout
            tryout_object = get_object_or_404(Tryout, pk=pk_tryout)

             # simpan object question yang baru 
            newQuestion = form.save()  
             # sambungkan foreign key pertanyaan dengan primary key tryout
            newQuestion.tryout = tryout_object
            newQuestion.save()

            #tambahkan jumlah pertanyaan pada tryout 
            
            tryout_object.question_count += 1
            tryout_object.save()
            success_url = reverse_lazy('view_quiz', kwargs={'pk': pk_tryout})
            return redirect(success_url)
        else:
        # jika tidak, minta user untuk mengisi kembali formnya 
            ctx = {'form' : form, 'pk_tryout' : pk_tryout}
            return render(request, self.template_url, ctx)
    
# View untuk mengupdate question
class UpdateQuestion(View):
    model = Question
    template_url = 'quizapp/update_question.html'

    def get(self, request, pk_tryout, pk_question):
        # Ambil object question yg sudah ada
        question_object = get_object_or_404(self.model, pk=pk_question)
        # buat form & "auto fill" sesuai dengan data object yg sudah disimpan 
        form = MakeQuestion(instance=question_object)
        ctx = {'form' : form, 'pk_tryout' : pk_tryout}
        return render(request, self.template_url, ctx)
    
    def post(self, request, pk_tryout, pk_question):
        question_object = get_object_or_404(self.model, pk=pk_question)
        form = MakeQuestion(request.POST, instance=question_object)
        # jika form diisi dengan benar, save ke object question lalu redirect ke quiz
        if form.is_valid():
            newTryout = form.save()
            success_url = reverse_lazy('view_quiz', kwargs={'pk': pk_tryout})
            return redirect(success_url)
        else:
        # jika tidak, minta user untuk mengisi kembali formnya 
            ctx = {'form' : form, 'pk_tryout' : pk_tryout}
            return render(request, self.template_url, ctx)
        
# View untuk mendelete question yang sudah ada
class DeleteQuestion(View):
    model = Question
    template_url = 'quizapp/delete_question.html'

    def get(self, request, pk_tryout, pk_question):
        question_object = get_object_or_404(self.model, pk=pk_question)
        ctx = {'pk_tryout' : pk_tryout}
        return render(request, self.template_url, ctx)
    
    def post(self, request, pk_tryout, pk_question):
        question_object = get_object_or_404(self.model, pk=pk_question)
        question_object.delete()
        
        # kurangi jumlah pertanyaan pada tryout
        tryout_object = get_object_or_404(Tryout, pk=pk_tryout)  
        tryout_object.question_count -= 1
        tryout_object.save()

        success_url = reverse_lazy('view_quiz', kwargs={'pk': pk_tryout})
        return redirect(success_url)
    
# View untuk mengerjakan try out
class StartQuiz(View):
    def get(self, request, pk_tryout):
        return render(request, 'quizapp/start_quiz.html')