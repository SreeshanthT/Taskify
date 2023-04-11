from django.urls import path
from django.conf.urls.static import static
from dj_docs.utils import DOC_STATIC_ROOT, DOC_STATIC_URL
from .views import documentation_view, templates_view

urlpatterns = [
    path('', documentation_view, name='docs'),
    path('<str:template_name>/', templates_view, name='docs_templates'),
]

urlpatterns += static(DOC_STATIC_URL, document_root=DOC_STATIC_ROOT)
