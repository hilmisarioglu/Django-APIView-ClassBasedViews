from django.urls import path, include
from .views import (home,
                    KayitListView,
                    KayitDetailView,
                    KayitListCreate , 
                    KayitRetrieveUpdateDelete,KayitConceteListCreate,KayitConceteRetrieveUpdateDelete,KayitVSListRetrieve,
                    KayitMVS
                    )

from rest_framework import routers

router = routers.DefaultRouter()
router.register('kayit-mvs', KayitMVS)
# router.register('kayit-list', KayitVSListRetrieve)


urlpatterns = [
    path('', home),       
    
    # path('list/', KayitListView.as_view()),
    # path('detail/<int:pk>', KayitDetailView.as_view() , name = 'serializer'),
    
    # path('list/', KayitListCreate.as_view()),
    # path('detail/<int:pk>', KayitRetrieveUpdateDelete.as_view() , name = 'serializer'),
    
    # path('list/', KayitConceteListCreate.as_view()),
    # path('detail/<int:pk>', KayitConceteRetrieveUpdateDelete    .as_view() , name = 'serializer'),
    path('', include(router.urls)),
]