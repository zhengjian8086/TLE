from django.shortcuts import render

# Create your views here.
import json
from django.conf import settings
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404, HttpResponse,JsonResponse
from haystack.forms import  ModelSearchForm
from haystack.query import EmptySearchQuerySet
RESULTS_PER_PAGE = getattr(settings, 'HAYSTACK_SEARCH_RESULTS_PER_PAGE', 20)



def basic_search(request, load_all=True, form_class=ModelSearchForm, searchqueryset=None, extra_context=None, results_per_page=None):
    query = ''
    results = EmptySearchQuerySet()
    if request.GET.get('q'):
        form = form_class(request.GET, searchqueryset=searchqueryset, load_all=load_all)

        if form.is_valid():
            query = form.cleaned_data['q']
            results = form.search()
    else:
        form = form_class(searchqueryset=searchqueryset, load_all=load_all)

    paginator = Paginator(results, results_per_page or RESULTS_PER_PAGE)
    try:
        page = paginator.page(int(request.GET.get('page', 1)))
    except InvalidPage:
        result = {"code": 404, "msg": 'No file found！', "data": []}
        return HttpResponse(json.dumps(result), content_type="application/json")

    context = {
        'form': form,
        'page': page,
        'paginator': paginator,
        'query': query,
        'suggestion': None,
    }
    if results.query.backend.include_spelling:
        context['suggestion'] = form.get_suggestion()

    if extra_context:
        context.update(extra_context)


    jsondata = []
    print(len(page.object_list))
    for result in page.object_list:
        data = {
            'pk': result.object.name,
            'title': result.object.title,
            'content': result.object.body,

        }
        jsondata.append(data)
    result = {"code": 200, "msg": 'Search successfully！', "data": jsondata}
    return JsonResponse(result, content_type="application/json")