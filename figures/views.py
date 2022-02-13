from django.forms import Form
from django.http import HttpResponse, FileResponse
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.utils import timezone

from mysite.settings import BASE_DIR, PATH_TO_ARCHIVES, DAY_LIMIT_OF_FIGURES
from .models import Client, Circle
from .forms import FigureRequestForm
from .helper import make_archive
from mysite.exceptions import DownloadLimitException

from datetime import timedelta


def description(request):
	"""Main page with circle order form"""
	if request.method == 'POST':
		form = FigureRequestForm(request.POST)
		if form.is_valid():			
			ip = request.META['REMOTE_ADDR']
			name = form.cleaned_data['name']
			amount = form.cleaned_data['amount']

			# Check user downloads under daily limit and raise exceptions
			day_ago = timezone.now() - timedelta(days=1)
			total_user_figures_today = Circle.objects.filter(owner__ip=ip, sending_date__gt=day_ago).count()			
			if total_user_figures_today + amount > DAY_LIMIT_OF_FIGURES:
			 	raise DownloadLimitException(data={'figures_today': total_user_figures_today})
			if amount > len(Circle.get_free_figures()):
			 	raise DownloadLimitException(data={'figures_today': total_user_figures_today})

			user, is_created = Client.objects.get_or_create(
				ip=ip,
				name=name,
			)

			# Creating zipfile with circles
			archive_name = make_archive(user, amount)
			
			return FileResponse(open(str(BASE_DIR) + '/' + PATH_TO_ARCHIVES + archive_name, 'rb'))
			

	# on method GET
	ordinary_circles, rare_circles, unique_circles = Circle.free_figures_by_types()
	all_circles = ordinary_circles + rare_circles + unique_circles

	form = FigureRequestForm()
	return render(request, 'figures/main_page.html', {
		'all_circles': all_circles,
		'rare_circles': rare_circles,
		'unique_circles': unique_circles,
		'form': form
	})


def info(request):
	"""Infopage"""
	return render(request, 'figures/info_page.html')


def table(request):
	"""Table page"""

	# Making Q objects to bring together Client objects with sum of their circles by types.
	rare_number = Count('circle', filter=Q(circle__ftype='R'))
	unique_number = Count('circle', filter=Q(circle__ftype='U'))

	client_list = Client.objects.annotate(Count('circle')).annotate(rare_number=rare_number).annotate(unique_number=unique_number).filter(circle__count__gt=0).order_by('-circle__count', '-unique_number', '-rare_number')
	return render(request, 'figures/table_page.html', {'client_list': client_list})	
	
