"""
    Author         : Jagat Iyer
    Developer     : Prasanna Vijayan
    Created Date : 10th Jan 2015
    Description     : Models are created here and so to create database 
    Projct Name     : PostReplyPrasanna
    Last Updated : 14 Jan 2015
                                    """

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    post = models.CharField(max_length=200, null=True, blank = True)
    posted_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    number_of_replies = models.IntegerField(default=0,null=True, blank=True)
    likes = models.IntegerField(default=False)

    def __unicode__(self):
        return self.post
    
        
class Reply(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    post = models.ForeignKey(Post, null=True, blank=True)
    reply = models.CharField(max_length=300, null=True, blank = True)
    posted_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    reply_likes = models.IntegerField(default=False)

    def __unicode__(self):
        return str(self.user)
    
    
class PostLikes(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    post = models.ForeignKey(Post, null=True, blank=True)
    status = models.BooleanField(default=False)
    
    
    def __unicode__(self):
        return self.user.username
    

class ReplyLikes(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    reply = models.ForeignKey(Reply, null=True, blank=True)
    status = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.user.username
    
    

     

