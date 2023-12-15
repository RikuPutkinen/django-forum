from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Board, Post, Comment
from .forms import PostForm, CommentForm

def index(request):
    boards = Board.objects.all()
    recent_posts = Post.objects.order_by("-post_date")[:20]
    context = {"boards": boards, "recent_posts": recent_posts}
    return render(request, "forum/index.html", context)


def boards(request, board_name):
    board = Board.objects.filter(board_name=board_name)[0]

    if request.method == "POST":
        form = PostForm(request.POST)
        if (form.is_valid()):
            p = Post(**form.cleaned_data)
            p.post_date = timezone.now()
            p.board_id = board
            p.save()
            return redirect(p)

    if request.method == "GET":
        
        context = {"board": board}
        return render(request, "forum/board.html", context)


def posts(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if (form.is_valid()):
            c = Comment(**form.cleaned_data)
            c.post_date = timezone.now()
            c.post_id = post
            c.save()
            return redirect(post)
        
    context = {"post": post}
    return render(request, "forum/post.html", context)


## HTMX stuff


def new_post(request, board_name):
    form = PostForm()
    context = {"board_name": board_name, "form": form}
    return render(request, "forum/post-form.html", context)


def post_list(request, board_name):
    board = Board.objects.filter(board_name=board_name)[0]
    posts = board.post_set.all()

    paginator = Paginator(posts, 2)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    page_range = range(1, paginator.num_pages + 1)
    
    context = {"page_obj": page_obj, "page_range": page_range, "board_name": board_name}
    return render(request, "forum/post-list.html", context)


def new_comment(request, post_id):
    form = CommentForm()
    context = {"post_id": post_id, "form": form}
    return render(request, "forum/comment-form.html", context)


def comment_list(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment_set.all()
    number_of_comments = len(comments)
    
    context = {"post_id": post_id, "comment_list": comments, "number_of_comments": number_of_comments}
    return render(request, "forum/comment-list.html", context)