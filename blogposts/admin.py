from django.contrib import admin
from blogposts.models import Post , Comment , SavedPosts , LikedPosts , MarkAsRead  , Tags , PostWithTags

class PostAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    pass
class LikedPostAdmin(admin.ModelAdmin):
    pass
class SavedPostAdmin(admin.ModelAdmin):
    pass
class TagsAdmin(admin.ModelAdmin):
    pass
class MarkAsReadAdmin(admin.ModelAdmin):
    pass

class PostWithTagsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(SavedPosts,SavedPostAdmin)
admin.site.register(LikedPosts,LikedPostAdmin)
admin.site.register(MarkAsRead,MarkAsReadAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(PostWithTags,PostWithTagsAdmin)
