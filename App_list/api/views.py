from rest_framework.response import Response
from django.views import View
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
#from rest_framework.decorators import api_view
from App_list.models import Striming, WatchList, Public
from App_list.api.serialzers import StrimingSerilazer, WatchListSerilazer, PublicSerialzers
from App_list.api.permissions import AdminOrder, PublicUserOrReadOnly
from App_list.api  import permissions, serialzers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

#from rest_framework import mixins

from rest_framework import generics
 

class PublicDeatil(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublicSerialzers
    permmision_class = [IsAuthenticated]

    def get_queryset(self):
        queryset = Public.objects.all()
        local = self.request.query_params.get('local')
        if local is not None:
            queryset = queryset.filter(itemlocal = local)
        return queryset

class PublicList(generics.ListCreateAPIView):
    serializer_class = PublicSerialzers
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permmision_class = [IsAuthenticatedOrReadOnly]
    queryset = Public.objects.all()



    
    

# class StreamPlatformVS(viewsets.ModelViewSet):
#     queryset = Striming.objects.all()
#     serializer_class = serialzers.StrimingSerilazer
#     permission_classes = [permissions.AdminOrder]




class StrimingAR(APIView):

    def get(self, request):
        movie = Striming.objects.all()
        serialzer = StrimingSerilazer(movie, many=True)
        # context={'request': request}
        return Response(serialzer.data)
    
    def post(self, request):
        serialzer = StrimingSerilazer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StrimingDetails(APIView):
    def get(self, request, pk):
        try:
            movie = Striming.objects.get(pk=pk)
        except movie.DoesNotExits:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serialzer= StrimingSerilazer(movie)
        return Response(serialzer.data)
        
    
    
    def put(self, request, pk):
        movie = Striming.objects.get(pk=pk)
        
        serialzer = StrimingSerilazer(movie, data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
            
        else:
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = Striming.objects.get(pk=pk)
        
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        


class MovieList(APIView):
    def get(self, request):

        movie = WatchList.objects.all()
        serialzer = WatchListSerilazer(movie, many=True)
        return Response(serialzer.data)
    def post(self, request):

        serialzer = WatchListSerilazer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data) 

        else:
            return Response(serialzer.errors)
        
class MovieDetail(APIView):
    def get(self, request, pk):
        try:
            movies = WatchList.objects.get(pk=pk)
        except movies.DoesNotExist:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serialzer= WatchListSerilazer(movies)
        return Response(serialzer.data)
        
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        
        serialzer = WatchListSerilazer(movie, data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
            
        else:
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        
    









# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         serialzer = MovieSerilazer(movie, many=True)
#         return Response(serialzer.data)
#     if request.method == 'POST':
#         serialzer = MovieSerilazer(data=request.data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(serialzer.data) 

#         else:
#             return Response(serialzer.errors)
          
        

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):

#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except movie.DoesNotExist:
#             return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serialzer= MovieSerilazer(movie)
#         return Response(serialzer.data)
    
#     if request.method == 'PUT':
            
        
#             movie = Movie.objects.get(pk=pk)
        
#             serialzer = MovieSerilazer(movie, data=request.data)
#             if serialzer.is_valid():
#                 serialzer.save()
#                 return Response(serialzer.data)
        
#             else:
#                 return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
        
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
