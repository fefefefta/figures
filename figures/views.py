from django.shortcuts import render
from .models import Client, Circle

# Create your views here.

def description(request):
	if request.method == 'GET':
		ordinary_circles, rare_circles, unique_circles = Circle.not_sended_figures_by_types()
		all_circles = ordinary_circles + rare_circles + unique_circles

		return render(request, 'figures/main_page.html', {
				'all_circles': all_circles,
				'rare_circles': rare_circles,
				'unique_circles': unique_circles
			})

	