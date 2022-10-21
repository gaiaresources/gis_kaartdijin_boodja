"""Kaartdijin Boodja URL Configuration.

The `urlpatterns` list routes URLs to views.
For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path("", views.home, name="home")
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""


# Third-Party
from django import conf
from django import urls
from django.contrib import admin


# Admin Site Settings
admin.site.site_header = conf.settings.PROJECT_TITLE
admin.site.index_title = conf.settings.PROJECT_TITLE
admin.site.site_title = conf.settings.PROJECT_TITLE


# Django URL Patterns
urlpatterns = [
    # Django Administration
    urls.path("admin/", admin.site.urls),

    # API Endpoints
    urls.path("api/accounts/", urls.include("kaartdijin_boodja.apps.accounts.urls")),
    urls.path("api/docs/", urls.include("kaartdijin_boodja.apps.swagger.urls")),
    urls.path("api/catalogue/", urls.include("kaartdijin_boodja.apps.catalogue.urls")),
]
