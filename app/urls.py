from django.urls import path
from .views import home, KayitListView,KayitDetailView

urlpatterns = [
    path('', home),
    path('list/', KayitListView.as_view()),
    path('detail/<int:pk>', KayitDetailView.as_view() , name = 'serializer'),
]