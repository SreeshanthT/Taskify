import os
from django.http import HttpResponse, Http404
from dj_docs.utils import DOC_HTMLS

# Create your views here.


def documentation_view(request):

    # Load the index.html file
    with open(os.path.join(DOC_HTMLS, 'index.html'), 'r') as f:
        html = f.read()

    # Serve the HTML as a response
    return HttpResponse(html)


def templates_view(request, **kwargs):
    template = kwargs.get('template_name')

    if template:
        template_path = os.path.join(DOC_HTMLS, template)
        if os.path.exists(template_path):
            with open(template_path, 'r') as f:
                html = f.read()
            return HttpResponse(html)

    raise Http404("Template does not exist")
