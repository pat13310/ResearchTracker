from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View
from .forms import FundingForm
from .models import Funding


class FundingListView(ListView):
    model = Funding
    template_name = 'fundings/funding-list.html'
    context_object_name = 'fundings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FundingForm()  # Ajouter le formulaire au contexte
        return context


class FundingCreateView(View):
    def post(self, request, *args, **kwargs):
        form = FundingForm(request.POST)
        if form.is_valid():
            if request.user:
                name = request.user.last_name
                funding = form.save(commit=False)
                funding.name = name
            funding = form.save()
            # data = {
            #     'id': funding.id,
            #     'name': funding.name,
            #     'amount': funding.amount,
            #     'active': funding.active,
            #     'project': funding.project
            # }
            return redirect(f'/fundings/list/')
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)

    def get(self, request, *args, **kwargs):
        # Si vous avez besoin de gérer les requêtes GET aussi
        return HttpResponseNotAllowed(['POST'])
