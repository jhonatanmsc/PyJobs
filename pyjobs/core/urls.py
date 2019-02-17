from django.conf.urls import include, url
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap

from pyjobs.core.models import Job
from pyjobs.core.views import *


class PyJobsSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Job.get_publicly_available_jobs()

    def lastmod(self, obj):
        return obj.created_at


urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^job/(?P<pk>\d+)/$", job_view, name="job_view"),
    url(r"^summary/$", summary_view, name="job_view"),
    url(r"^services/$", services_view, name="services"),
    url(r"^contact/$", contact, name="contact"),
    url(r"^register/new/job/$", register_new_job, name="register_new_job"),
    url(r"^pythonistas/$", pythonistas_area, name="pythonistas_area"),
    url(r"^pythonistas/signup/$", pythonistas_signup, name="pythonistas_signup"),
    url(r"^password/$", pythonista_change_password, name="change_password"),
    url(r"^info/$", pythonista_change_info, name="change_info"),
    url(r"^robots.txt$", robots_view, name="robots"),
    url(
        r"^sitemap\.xml$",
        sitemap,
        {"sitemaps": {"jobs": PyJobsSitemap()}},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    url(r"^select2/", include("django_select2.urls")),
    url(r"^feed/$", JobsFeed()),
]
