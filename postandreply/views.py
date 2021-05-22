
"""
	Author		 : Jagat Iyer
	Developer	 : Prasanna Vijayan
	Created Date : 10th Jan 2015
	Description	 : Gets the request from FrontEnd and updates the Post, Reply and Corresponding Likablilty of that particular post or reply
	Projct Name	 : PostReplyPrasanna
	Last Updated : 14 Jan 2015
									"""




from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# import post form
from django.template.loader import render_to_string

from django.utils import timezone




from .models import Post, Reply, PostLikes, ReplyLikes
from django.core.context_processors import request

# Create your views here.
button_staus = 0

def postform(request):
	posts = Post.objects.all().order_by('-posted_date')
	replys = Reply.objects.all().order_by('-posted_date')
	for rep in posts:
		reply = list(Reply.objects.filter(post=rep))
		rep.reply = reply
		
	for plike in posts:
		like = list(PostLikes.objects.filter(post=plike))
		plike.like = like
		
	likes = PostLikes.objects.filter(user=request.user)
	
		
	return render(request, "post-reply.html",  { 'posts': posts, "iconpostlike": likes})

def getdata(request):
	posts = Post.objects.all().order_by('-posted_date')
	replys = Reply.objects.all().order_by('-posted_date')
	for rep in posts:
		reply = list(Reply.objects.filter(post=rep))
		rep.reply = reply
		
	for plike in posts:
		like = list(PostLikes.objects.filter(post=plike))
		plike.like = like
		
	likes = PostLikes.objects.filter(user=request.user)
	html=render_to_string('postrender.html', { 'posts': posts, "iconpostlike": likes})
	return HttpResponse(html) 

@csrf_exempt	
def addpost(request):
	print "welcome"
	data = request.POST['post_data']
	print data
	print request.user
	print  timezone.now()
	post = Post(post = data, user = request.user, posted_date = timezone.now(), updated=timezone.now(), number_of_replies=0)
	post.save()
	response = "True"
	#response = json.dumps(datasend)
	return HttpResponse(response)

@csrf_exempt	
def addreply(request):
	data = request.POST['reply_data']
	data_id = request.POST['postid']
	repost = Post.objects.get(id=int(data_id))
	reply = Reply(user = request.user, post=repost, reply=data, posted_date=timezone.now(), updated=timezone.now())
	reply.save()
	response = "True"
	#response = json.dumps(datasend)
	return HttpResponse(response) 
@csrf_exempt	
def addlikes(request):
	
	data_id = request.POST['postid']
	totallikes = int(request.POST['totallikes'])
	# get the values from Ajax
	user = request.user
	post = Post.objects.get(id=int(data_id))
	try:
		update_like = PostLikes.objects.filter(user=user, post=post)
		if update_like.exists():
			print "exist"
			for a in update_like:
				print a
				if a.status==True:
					print "in true"
					a.status=False
					a.save()
					post.likes = totallikes - 1
					post.save()
				else:
					a.status=True
					a.save()
					post.likes = totallikes + 1
					post.save()
		else:
			update_like = PostLikes(user=user, post=post, status=False)
			update_like.status = True
			update_like.save()
			post.likes = totallikes + 1
			post.save()
			print "created"
	except:
		pass
	
	
	response = "True"
	
	#response = json.dumps(datasend)
	return HttpResponse(response) 
@csrf_exempt
def replylikes(request):
	reply_id = request.POST['replyid']
	replylike = int(request.POST['replylikes'])
	user = request.user
	
	reply = Reply.objects.get(id=int(reply_id))
	print reply
	try:
		update_reply_like = ReplyLikes.objects.filter(user=user, reply=reply)
		if update_reply_like.exists():
			print "exists"
			for a in update_reply_like:
				print a
				if a.status == True:
					a.status = False
					a.save()
					reply.reply_likes = replylike - 1
					reply.save()
				else:
					a.status=True
					a.save()
					reply.reply_likes = replylike + 1
					reply.save()
		else:
			update_reply_like = ReplyLikes(user=user, reply=reply, status=False)
			update_reply_like.status = True
			update_reply_like.save()
			reply.reply_likes = replylike + 1
			reply.save()
			print "Created"
	except:
		pass
	
	response = "True"
	return HttpResponse(response)
	

def get_total_likes(post):
	print post	

	

