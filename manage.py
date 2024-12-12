import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leonidas.settings')

app = get_wsgi_application()  # Vercel requires this `app` variable
