from django.shortcuts import render
from django.db.models import OuterRef , Subquery , Prefetch
from django.db import connection

from blogposts.api.serializers import UserSerializer
from accounts.models import UserAccount
from blogposts.models import Post , Comment , SavedPosts , LikedPosts 

def practiseQuery(request):
    pass