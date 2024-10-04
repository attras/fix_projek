from django.shortcuts import render, redirect
from django.db import transaction 
from django.views import View
from admin_setori.models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404


class Admin_faqViews(View):
    def get(self, request):
        dt_faq = Faq.objects.filter(delete_at__isnull = True)
        data = {
            'dt_faq' : dt_faq
        }
        return render(request, 'admin/admin_faq/index.html',data)
    
class Addfaq(View) :
    def post(self, request):
        jawaban = request.POST.get('pertanyaan')
        pertanyaan = request.POST.get('jawaban')
        try:
            table = Faq()
            table.pertanyaan = jawaban
            table.jawaban = pertanyaan
            table.create_at = timezone.now()
            table.save()
            return redirect('admin_setori:admin_faq')
        except Exception as e:
            print('Error Data')
            return redirect('admin_setori:admin_faq')
        
class Editfaq(View) :
    def get(self, request,id):
        editfaq= get_object_or_404(Faq,id=id)
        data={
            'edit_faq': editfaq
        }
        return render(request, 'admin/admin_faq/edit.html',data)
    
    def post(self, request,id):
        jawaban = request.POST.get('pertanyaan')
        pertanyaan = request.POST.get('jawaban')
        try:
            editfaq = get_object_or_404(Faq,id=id)
            editfaq.pertanyaan = jawaban
            editfaq.jawaban = pertanyaan
            editfaq.create_at = timezone.now()
            editfaq.save()
            messages.success(request, f"kategori berhasil ditambahkan")
            return redirect('admin_setori:admin_faq')
        except Exception as e:
            print('Error Data')
            return redirect('admin_setori:admin_faq')