
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class RevendedorView(View):
    def get(self, request):
        return render(request, 'revendedor.html')
    
class SobreView(View):
    def get(self, request):
        return render(request, 'sobre.html')
    
class ProdutoView(View):
    def get(self, request):
        return render(request, 'produtos.html')