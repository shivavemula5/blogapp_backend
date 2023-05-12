from blogposts import models
from accounts import models as accounts_models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts_models.UserAccount
        fields = ['id','email','name']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id','user','image','title','body','created','time_required']
        read_only_fields = ['id','user']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id','user','post','comment']
        read_only_fields = ['id','user']

class LikedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikedPosts
        fields = ['id','user','post','liked']
        read_only_fields = ['id','user']


class SavedPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SavedPosts
        fields = ['id','saved','post','user']
        read_only_fields = ['id','user']
    
class MarkAsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SavedPosts
        fields = ['id','saved','post','user']
        read_only_fields = ['id']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = ['id','tag']
        read_only_fields = ['id']

class PostsWithTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostWithTags
        fields = ['id','tag','post']
        read_only_fields = ['id']

class GetLikesForPostSerializer(serializers.Serializer):
    likes = serializers.IntegerField()

class GetCommentsForPostSerializer(serializers.Serializer):
    comments = serializers.IntegerField()

class GetSavedCountForPostSerializer(serializers.Serializer):
    saved = serializers.IntegerField()

class GetPostLikeSummary(serializers.Serializer):
    posts = serializers.IntegerField()

class PostSummarySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    image = serializers.CharField()
    created = serializers.DateTimeField()
    body  = serializers.CharField()
    time_required = serializers.IntegerField()
    liked = serializers.BooleanField(required=False,allow_null=True)
    saved = serializers.BooleanField(required=False,allow_null=True)

class PostSummarySerializerId(serializers.Serializer):
    id = serializers.IntegerField()