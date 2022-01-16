from django.urls import path
from .views import home, KayitListView,KayitDetailView,KayitListCreate , KayitRetrieveUpdateDelete , KayitConceteListCreate,KayitConceteRetrieveUpdateDelete

urlpatterns = [
    path('', home),
    
    # path('list/', KayitListView.as_view()),
    # path('detail/<int:pk>', KayitDetailView.as_view() , name = 'serializer'),
    
    # path('list/', KayitListCreate.as_view()),
    # path('detail/<int:pk>', KayitRetrieveUpdateDelete.as_view() , name = 'serializer'),
    
    path('list/', KayitConceteListCreate.as_view()),
    path('detail/<int:pk>', KayitConceteRetrieveUpdateDelete    .as_view() , name = 'serializer'),
    
]