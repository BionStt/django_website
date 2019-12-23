from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

from blog.forms import BlogsFeed
from free_chapter.views import RequestFreeChapter, ConfirmFreeChapter
from search import views as search_views

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^comments/', include('django_comments_xtd.urls')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^newsletter/', include('newsletter.urls')),

    path('free_chapter/', RequestFreeChapter.as_view(), name='request-free-chapter'),
    path('confirm/<str:secret_code>', ConfirmFreeChapter.as_view(), name='confirm-free-chapter'),

    url('^sitemap\.xml$', sitemap),
    url(r'feed\.rss$', BlogsFeed(), name='feed'),

    url(r'', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
