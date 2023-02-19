from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, UpdateView
from django.views import generic, View
from .models import CakePost, CakeComment
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.text import slugify
from .forms import CreateComment

# Create your views here.


class CakeList(generic.ListView):
    """
    Displays a list of Cake Posts with status of Posted
    using the CakePost Model
    """
    model = CakePost
    queryset = CakePost.objects.filter(status=1,
                                       cake_approve=True).order_by(
                                       '-date_created')
    template_name = 'cakes.html'
    context_object_name = "cakelist"


class CakeDetail(View):
    """
    This class will display the cake detail to the user.
    It will also render comments the user makes
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Sets favourites to False and returns the cake post
        in a detailed view
        """
        queryset = CakePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.user_comments.filter(
                                             comment_approve=True
                                             ).order_by('comment_created')
        favourite = False
        if post.favourite.filter(id=self.request.user.id).exists():
            favourite = True

        return render(
            request,
            "cake_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "favourite": favourite,
                "comment_form": CreateComment()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Takes the CakePost Object and allows the user
        to click on an icon to mark it as a favourite
        and to leave a comment for approval underneath
        the cake post.  Validates the comment and saves it for
        approval.
        """
        queryset = CakePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.user_comments.filter(
                                             comment_approve=True
                                             ).order_by('comment_created')
        favourite = False
        if post.favourite.filter(id=self.request.user.id).exists():
            favourite = True

        comment_form = CreateComment(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        else:
            comment_form = CreateComment()

        return render(
            request,
            "cake_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "favourite": favourite,
                "comment_form": CreateComment()
            },
        )
        

class Favourites(View):
    """
    Creates a view so user can like cake posts
    """

    def post(self, request, slug):
        """
        checks if user has id and can add or remove likes
        reloads cake_detail page
        """
        post = get_object_or_404(CakePost, slug=slug)

        if post.favourite.filter(id=request.user.id).exists():
            post.favourite.remove(request.user)
        else:
            post.favourite.add(request.user)

        return HttpResponseRedirect(reverse('cake_detail', args=[slug]))