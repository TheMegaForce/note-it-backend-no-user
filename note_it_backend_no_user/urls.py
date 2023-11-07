from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from notes.views import NoteViewSet

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'notes', NoteViewSet) #register "/notes" routes


urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]