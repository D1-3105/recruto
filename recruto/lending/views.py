from django.shortcuts import render, redirect, reverse
from django.views import generic


class HelloView(generic.TemplateView):
    template_name = 'landing.html'

    def get_context_data(self):
        super().get_context_data()
        message= self.request.GET.get('message', 'No messages yet!')
        name= self.request.GET.get('name', 'Noname')
        context={
            'message':message,
            'name':name
        }
        return context

