from django.contrib.auth import get_user_model
from django.db.models import Sum

from category.models import Category
from post.models import Post

User = get_user_model()


def get_admin_stats(request):
    if 'admin' not in request.path:
        return {}

    return {
        'total_users': User.objects.count(),
        'total_posts': Post.objects.count(),
        "total_categories": Category.objects.count(),

        # Most liked posts
        "most_liked_posts": Post.objects.order_by('-total_likes')[:5],

        # Most liked categories linked to posts
        "most_liked_categories": Category.objects.annotate(total_category_likes=Sum('posts__total_likes')).order_by(
            '-total_category_likes')[:5]

    }
