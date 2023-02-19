""" Models """

from django.db import models
from user_profiles .models import UserProfile
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Posted"))


class CakePost(models.Model):
    """ Model for Users to Post a Cake """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='cakes')
    full_name = models.CharField(max_length=80, null=False, blank=False)
    title = models.CharField(max_length=220, unique=True)
    cake_image = CloudinaryField('image', default='placeholder1')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=220, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    favourite = models.ManyToManyField(
        User,
        related_name='favourite',
        blank=True)
    cake_approve = models.BooleanField(default=False)

    class Meta:
        """
        cakes are displayed in order from newest to oldest posted
        """
        ordering = ['-date_created']

    def __str__(self):
        """
        returns string representation of the object
        """
        return f"{self.title}"

    def number_of_favourites(self):
        """
        Returns total number of times a user has marked
        a cake image as a favourite
        """
        return self.favourite.count()


class CakeComment(models.Model):
    """Model for User to leave a comment on a cake post"""
    post = models.ForeignKey(CakePost, on_delete=models.CASCADE,
                             related_name="user_comments",)
    name = models.CharField(max_length=80, default="Anonymous User")
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField()
    comment_approve = models.BooleanField(default=False)

    class Meta:
        """
        comments are ordered from latest to oldest
        """
        ordering = ['comment_created']

    def __str__(self):
        """
        returns string representation of the object
        """
        return f"{self.name}, {self.comment_created}"
