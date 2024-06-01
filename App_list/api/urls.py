from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from App_list.api.views import movie_list, movie_details
from App_list.api.views import MovieList, MovieDetail, StrimingAR ,StrimingDetails,PublicList, PublicDeatil

# router = DefaultRouter()
# router.register('stream/', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', MovieList.as_view(), name="list"),
    path('<int:pk>', MovieDetail.as_view(), name="moviedetails"),
   # path('', include(router.urls)),
    path('str/', StrimingAR.as_view(), name="str"),
    path('str/<int:pk>', StrimingDetails.as_view(), name="StrimingDetails"),
    path('public/', PublicList.as_view(), name="public"),
    path('public/<int:pk>', PublicDeatil.as_view(), name="PublicDetails"),
    #path('<int:pk>/public-create/',ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/public/',PublicList.as_view(), name='review-list'),
    path('public/<int:pk>/',PublicDeatil.as_view(), name='review-detail'),


]
















