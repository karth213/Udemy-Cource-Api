from django.contrib import admin
from . models import Striming, WatchList, Public
# Register your models here.


admin.site.register(Striming)

admin.site.register(WatchList)

admin.site.register(Public)






# class ReviewCreate(generics.CreateAPIView):
#     serializer_class = serialzers.PublicSerialzers
#     permission_classes = [IsAuthenticated]
    

#     def get_queryset(self):
#         return Public.objects.all()

#     def perform_create(self, serializer):
#         pk = self.kwargs.get('pk')
#         watchlist = WatchList.objects.get(pk=pk)

#         review_user = self.request.user
#         review_queryset = Public.objects.filter(
#             watchlist=watchlist, review_user=review_user)

#         if review_queryset.exists():
#             raise ValidationError("You have already reviewed this movie!")

#         if watchlist.number_rating == 0:
#             watchlist.avg_rating = serializer.validated_data['rating']
#         else:
#             watchlist.avg_rating = (
#                 watchlist.avg_rating + serializer.validated_data['rating'])/2

#         watchlist.number_rating = watchlist.number_rating + 1
#         watchlist.save()

#         serializer.save(watchlist=watchlist, review_user=review_user)