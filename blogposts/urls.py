from django.urls import path , include
from rest_framework_nested import routers
from blogposts.api import views
from blogposts import views as blogposts_views

router = routers.DefaultRouter()

router.register('users',views.UserViewSet,basename='users')

liked_posts_nested_router = routers.NestedDefaultRouter(router,'users',lookup='users')
liked_posts_nested_router.register('liked_posts',views.LikedPostsViewSet,basename='liked_posts')

saved_posts_nested_router = routers.NestedDefaultRouter(router,'users',lookup='users')
saved_posts_nested_router.register('saved_posts',views.SavedPostsViewset,basename='saved_posts')

mark_as_read_nested_router = routers.NestedDefaultRouter(router,'users',lookup='users')
mark_as_read_nested_router.register('mark_as_read',views.MarkAsReadViewset,basename='mark_as_read')

router.register('posts',views.PostViewSet,basename='posts')

comment_nested_router = routers.NestedDefaultRouter(router,'posts',lookup='posts')
comment_nested_router.register('comments',views.CommentViewSet,basename='comments')

urlpatterns = [
    path('',include('rest_framework.urls')),

    path('getlikesforpost/<int:id>/',views.getLikesForPost),
    path('getcommentsforpost/<int:id>/',views.getCommentsForPost),
    path('getsavedcountforpost/<int:id>/',views.getSaveCountForPost),

    path('my/postsummary/',views.MyPostSummary.as_view()),    
    path('my/liked/postsummary/',views.MyLikedPostSummary.as_view()),
    path('my/saved/postsummary/',views.MySavedPostSummary.as_view()),
    path('my/liked/postsummary/id/',views.MyLikedPostSummaryId.as_view()),
    path('my/saved/postsummary/id/',views.MySavedPostSummaryId.as_view()),

    path('practisequery',blogposts_views.practiseQuery),
] + \
    router.urls + \
    comment_nested_router.urls + \
    saved_posts_nested_router.urls + \
    mark_as_read_nested_router.urls + \
    liked_posts_nested_router.urls 
