from .models import DeliveryData
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from .forms import DeliSearchForm
from django.db.models import Q


def base(request):
    return render(request, 'blog/base.html')

def result(request):
    return render(request, 'blog/result.html')


class SearchFormView(FormView):
    form_class = DeliSearchForm
    template_name = 'blog/result.html'

    def form_valid(self, form):
        schStart = '%s' % self.request.POST['start_point']
        schEnd = '%s' % self.request.POST['end_point']
        schLength = '%s' % self.request.POST['length_form']
        schWeight = '%s' % self.request.POST['weight_form']
        schTime = '%s' % self.request.POST['time_form']
        area_list = DeliveryData.objects.filter(Q(start_area=schStart) & Q(end_area=schEnd) & Q(total_length__gte=schLength) & Q(del_time__lte=schTime) & Q(weight__gte=schWeight)).order_by('price')
        context = {}
        context['form'] = form
        context['search_term'] = schStart
        context['object_list'] = area_list

        return render(self.request, self.template_name, context)
