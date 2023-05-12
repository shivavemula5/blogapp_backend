from rest_framework.viewsets import ModelViewSet , ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination

from django.core.paginator import Paginator
from django.db import connection

from django_filters.rest_framework import DjangoFilterBackend 

from blogposts.api import permissions

from blogposts.api import serializers
from blogposts import models
from accounts import models as accounts_models

class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = accounts_models.UserAccount.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]

class PostViewSet(ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
    authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,]
    filterset_fields = ['user']
    search_fields = ['title','body']
    order_fields = ['created','time_required']

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
class CommentViewSet(ModelViewSet):
    serializer_class  = serializers.CommentSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = models.Comment.objects.filter(post__id = self.kwargs['posts_pk'])
        return queryset
    def perform_create(self, serializer):
        serializer.save(user = self.request.user )

class LikedPostsViewSet(ModelViewSet):
    serializer_class = serializers. LikedPostSerializer
    def get_queryset(self):
        queryset = models.LikedPosts.objects.prefetch_related('post').filter(user__id = self.kwargs['users_pk'])
        return queryset       
    def perform_create(self, serializer):
        serializer.save(user = self.request.user )

class SavedPostsViewset(ModelViewSet):
    serializer_class = serializers.SavedPostsSerializer
    def get_queryset(self):
        queryset = models.SavedPosts.objects.prefetch_related('post').filter(user__id = self.kwargs['users_pk'])
        return queryset       
    def perform_create(self, serializer):
        serializer.save(user = self.request.user )

class MarkAsReadViewset(ModelViewSet):
    serializer_class = serializers.MarkAsReadSerializer
    def get_queryset(self):
        queryset = models.Comment.objects.filter(user__id = self.kwargs['users_pk'])
        return queryset  

class TagsViewSet(ModelViewSet):
    serializer_class = serializers.TagsSerializer
    queryset = models.Tags.objects.all()

class PostsWithTagsViewSet(ModelViewSet):
    serializer_class = serializers.PostsWithTagsSerializer
    def get_queryset(self):
        queryset = models.Comment.objects.filter(post__id = self.kwargs['posts_pk'])
        return queryset    

@api_view(['GET'])
def getLikesForPost(request,id):
    likes = {'likes':models.LikedPosts.objects.filter(post=id).count()}
    serializeData = serializers.GetLikesForPostSerializer(data=likes)
    serializeData.is_valid(raise_exception=True)
    return Response(serializeData.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getCommentsForPost(request,id):
    comments = {'comments':models.Comment.objects.filter(post=id).count()}
    serializeData = serializers.GetCommentsForPostSerializer(data=comments)
    serializeData.is_valid(raise_exception=True)
    return Response(serializeData.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getSaveCountForPost(request,id):
    saved = {'saved':models.SavedPosts.objects.filter(post=id).count()}
    serializeData = serializers.GetSavedCountForPostSerializer(data=saved)
    serializeData.is_valid(raise_exception=True)
    return Response(serializeData.data,status=status.HTTP_200_OK)

    
class MyPostSummary(APIView):
    def get(self,request):
        cursor = connection.cursor()
        query = f'SELECT  blogposts_post.id,blogposts_post.title,blogposts_post.image,blogposts_post.created,    \
                          blogposts_post.body,blogposts_post.time_required FROM blogposts_post WHERE             \
                          blogposts_post.user_id={request.user.id}'
        cursor.execute(query)
        data_list = cursor.fetchall()
        dictionary_list = [{'id':tup[0],'title':tup[1],'image':tup[2],'created':tup[3],'body':tup[4],'time_required':tup[5]} for tup in data_list]
        serializeData = serializers.PostSummarySerializer(data=dictionary_list,many=True,context={'request':request})
        serializeData.is_valid(raise_exception=True)
        return Response({'data':serializeData.data},status=status.HTTP_200_OK)

class MySavedPostSummary(APIView):
    def get(self,request):
        query = f'SELECT distinct blogposts_post.id,blogposts_post.title,               \
                  blogposts_post.body,blogposts_post.image,blogposts_post.created,      \
                  blogposts_post.time_required,blogposts_savedposts.saved from          \
                  blogposts_savedposts left join                                        \
                  blogposts_post on blogposts_savedposts.post_id = blogposts_post.id    \
                  where blogposts_savedposts.user_id={request.user.id}'
        cursor = connection.cursor()
        cursor.execute(query)
        data_list = cursor.fetchall()
        dictionary_list = [{'id':tup[0],'title':tup[1],'body':tup[2],'image':tup[3],'created':tup[4],'time_required':tup[5],'saved':tup[6]} for tup in data_list]
        serializeData = serializers.PostSummarySerializer(data=dictionary_list,many=True,context={'request':request})
        serializeData.is_valid(raise_exception=True)
        return Response({'saved':serializeData.data},status=status.HTTP_200_OK)

class MyLikedPostSummary(APIView):
    def get(self,request):
        query = f'SELECT distinct blogposts_post.id,blogposts_post.title,               \
                  blogposts_post.body,blogposts_post.image,blogposts_post.created,      \
                  blogposts_post.time_required,blogposts_likedposts.liked from          \
                  blogposts_likedposts left join                                        \
                  blogposts_post on blogposts_likedposts.post_id = blogposts_post.id    \
                  where blogposts_likedposts.user_id={request.user.id}'
        cursor = connection.cursor()
        cursor.execute(query)
        data_list = cursor.fetchall()
        dictionary_list = [{'id':tup[0],'title':tup[1],'body':tup[2],'image':tup[3],'created':tup[4],'time_required':tup[5],'liked':tup[6]} for tup in data_list]
        serializeData = serializers.PostSummarySerializer(data=dictionary_list,many=True,context={'request':request})
        serializeData.is_valid(raise_exception=True)
        return Response({'liked':serializeData.data},status=status.HTTP_200_OK)

class MyLikedPostSummaryId(APIView):
    def get(self,request):
        query = f'SELECT distinct blogposts_likedposts.post_id from     \
                 blogposts_likedposts left join blogposts_post          \
                 on blogposts_likedposts.post_id = blogposts_post.id    \
                 where blogposts_likedposts.user_id={request.user.id}'
        cursor = connection.cursor()
        cursor.execute(query)
        data_list = cursor.fetchall()
        dictionary_list = [{'id':tup[0]} for tup in data_list]
        serializeData = serializers.PostSummarySerializerId(data=dictionary_list,many=True,context={'request':request})
        serializeData.is_valid(raise_exception=True)
        return Response({'liked':serializeData.data},status=status.HTTP_200_OK)

class MySavedPostSummaryId(APIView):
    def get(self,request):
        query = f'SELECT distinct blogposts_savedposts.post_id from \
                 blogposts_savedposts left join blogposts_post \
                 on blogposts_savedposts.post_id = blogposts_post.id \
                 where blogposts_savedposts.user_id={request.user.id}'
        cursor = connection.cursor()
        cursor.execute(query)
        data_list = cursor.fetchall()
        dictionary_list = [{'id':tup[0]} for tup in data_list]
        serializeData = serializers.PostSummarySerializerId(data=dictionary_list,many=True,context={'request':request})
        serializeData.is_valid(raise_exception=True)
        return Response({'saved':serializeData.data},status=status.HTTP_200_OK)