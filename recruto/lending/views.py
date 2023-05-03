from django.views import generic
import logging

logger = logging.getLogger('recruto')


class HelloView(generic.TemplateView):
    template_name = 'landing.html'

    def get_context_data(self):
        super().get_context_data()
        message = self.request.GET.get('message', 'No messages yet!')
        name = self.request.GET.get('name', 'Noname')
        context = {
            'message': message,
            'name': name
        }
        logger.info(f'RECRUTO WAS REQUESTED BY {self.request.META.get("REMOTE_ADDR")}')
        return context
