from mysite.exceptions import FiguresException

from django.shortcuts import render


class ExceptionMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_exception(self, request, exception):
		if isinstance(exception, FiguresException):
			return render(request, 'mysite/error.html', {
				'title': exception.title,
				'message': exception.message,
				'data': exception.data,
			}, status=400)
			