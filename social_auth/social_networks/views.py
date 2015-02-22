from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.template.context import RequestContext
# Create your views here.

class SocialTestView(TemplateView):

	template = 'social_networks/testsocialauth.html'

	def get(self, request):

		print(request)
		context = RequestContext(
			request, {
				'request': request,
				'user': request.user,
			}
		)

		return render_to_response(self.template, 
			context_instance=context
		)