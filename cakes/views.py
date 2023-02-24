from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CakePost, CakeComment
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.text import slugify
from .forms import CreateComment, CreateCake

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


class CreateCakeView(LoginRequiredMixin, CreateView):
    """
    Creates cake view so that users can create a new
    blog on the front end
    """

    template_name = 'create_cake.html'
    form_class = CreateCake

    def get_success_url(self):
        """
        sets the reverse url when
        user creates a new cake post
        """
        return reverse('cakes')

    def test_func(self):
        """
        Checks if user is logged in
        """
        return self.request.user.is_authenticated

    def form_valid(self, form):
        """
        Validates the form and adds the new cake post to the
        cakes.html page
        """

        form = form.save(commit=False)
        form.slug = slugify(form.title)
        messages.success(
            self.request,
            'You have created a new Cake Post.  It will be sent\
                admin for approval.')
        return super().form_valid(form)


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

# Management


class ReviewCakePost(LoginRequiredMixin, ListView):
    """
    Checks to see if user is superuser, gets a list of
    Cake posts made by a user and allows Admin
    to approve or Delete Posts
    """

    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    template_name = 'cake_review.html'
    model = CakePost
    queryset = CakePost.objects.filter(
        cake_approve=False).order_by('-date_created')
    context_object_name = 'to_approve'

    def get_context_data(self, **kwargs):
        """
        Gets the posts to approve
        """
        context = super().get_context_data(**kwargs)
        context[
                'cake_review'] = CakePost.objects.filter(
                    cake_approve=False).order_by('-date_created')
        return context


class ApproveCake(LoginRequiredMixin, View):
    """
    Admin who is logged in can approve cake posts 
    made by users
    """

    def test_func(self):
        """
        Checks if user is superuser 
        """
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        """
        gets the object instance's post and assigns primary key
        """
        cakepost = get_object_or_404(CakePost, pk=pk)
        context = {
            'cakepost': cakepost,
        }

        return render(
            request,
            'cake_approve.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):
        """
        gets the content the user made and checks
        if the content has been approved.  Admin can
        then approve
        """

        cakepost = get_object_or_404(CakePost, pk=pk)
        if request.method == "POST":
            cakepost.cake_approve = True
            cakepost.save()
        messages.success(
            self.request,
            'The Cake Post has been posted')
        return redirect('cake_review')


class DeleteCake(LoginRequiredMixin, DeleteView):
    """
    Checks to see if user is admin and allows admin
    to delete a cake post made by the user
    """
    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        """
        gets the object instance's comment and assigns primary key
        """
        cakepost = get_object_or_404(CakePost, pk=pk)
        context = {
            'cakepost': cakepost,
        }

        return render(
            request,
            'cake_delete.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):
        """
        gets the content the user made and checks
        if the content has been approved.  Admin can
        then delete the cake post
        """

        cakepost = get_object_or_404(CakePost, pk=pk)
        cakepost.delete()
        messages.success(
            self.request,
            'The post has been deleted')
        return redirect('cake_review')


class ReviewComments(LoginRequiredMixin, ListView):
    """
    Checks to see if user is superuser, gets a list of
    Comments made on a blog by user which allows Admin
    to approve Comments
    """

    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    template_name = 'review_comments.html'
    model = CakeComment
    queryset = CakeComment.objects.filter(
        comment_approve=False).order_by('comment_created')
    context_object_name = 'to_approve'

    def get_context_data(self, **kwargs):
        """
        Gets the comments to approve
        """
        context = super().get_context_data(**kwargs)
        context[
                'comments'] = CakeComment.objects.filter(
                    comment_approve=False).order_by('-comment_created')
        return context

