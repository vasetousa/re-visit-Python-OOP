STATIC_URL = '/static/'
MEDIA_URL = ''
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATIC_ROOT = s.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']

''' create folder staticfiles, static/images'''

''' in the urls.py file create the paths:
from django.conf import settings,
from django.conf.urls.static import static,
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

'''
