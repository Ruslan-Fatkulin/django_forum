from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
                  path('admin/', admin.site.urls),
              ] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('community/', include(('community.urls', 'forum'), namespace='community')),
    path('users/', include(('users.urls', 'forum'), namespace='users')),

)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += staticfiles_urlpatterns()
