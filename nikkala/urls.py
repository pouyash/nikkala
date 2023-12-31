from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from django.views.decorators.cache import never_cache
from filebrowser.sites import site
from ckeditor_uploader import views as ckeditor_views
from contact_us.views import ContactUsView
from about_us.views import AboutUsView
urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('accounts/', include('account.urls')),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('order/', include('order.urls')),
    path('blog/', include('blog.urls')),
    re_path(r'^ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    re_path(r'^ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)