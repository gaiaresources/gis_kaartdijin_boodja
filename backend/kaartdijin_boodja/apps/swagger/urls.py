"""Kaartdijin Boodja Swagger UI Django Application URLs."""


# Third-Party
from django import urls
from django.views import generic

# Local
from . import views

# Swagger URL Patterns
urlpatterns = [
   # Redirect Index to Swagger UI
   urls.re_path(r"^$", generic.RedirectView.as_view(url="schema-swagger-ui", permanent=True)),

   # Swagger URLs
   urls.re_path(r"^schema(?P<format>\.json|\.yaml)$", views.SchemaView.without_ui(), name="schema-spec"),
   urls.re_path(r"^swagger/$", views.SchemaView.with_ui("swagger"), name="schema-swagger-ui"),
   urls.re_path(r"^redoc/$", views.SchemaView.with_ui("redoc"), name="schema-redoc-ui"),
]
