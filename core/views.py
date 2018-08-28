from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View


#class BaseView(LoginRequiredMixin, View):
class BaseView(View):
    redirect_field_name = 'redirect_to'
    login_url = '/usuario/login'
    # permission_required = 'usuarios.Admin'


class ViewIndexBemVindo(BaseView):

    template = 'index_bemvindo.html'

    def get(self, request):
        return render(request, self.template)

class ViewIndex(BaseView):

    template = 'index.html'

    def get(self, request):
        return render(request, self.template)
