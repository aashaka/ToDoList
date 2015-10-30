from django.shortcuts import render,get_object_or_404,render_to_response	
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,Http404
from GetThingsDone.forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
#from GetThingsDone.forms import ProfileForm
from GetThingsDone.models import toDo
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main_page(request):
    template = get_template('main_page.html')
    variables = Context({ 'user': request.user })
    output = template.render(variables)
    return HttpResponse(output)

def welcome(request):
	if request.user.is_authenticated():
		user=request.user.username;
		return HttpResponseRedirect('../list')
	elif request.method=="POST":
		signupform=UserForm(request.POST)
		if signupform.is_valid():
			new_user=User.objects.create_user(**signupform.cleaned_data)
			new_user.backend='django.contrib.auth.backends.ModelBackend'
			messages.add_message(request,messages.SUCCESS,'Registration Successful !!')
			return HttpResponseRedirect('../welcome')
		else:
			return render(request,'GetThingsDone/welcome.html',{'form':signupform})	
 	else:
		signupform=UserForm()
		return render(request,'GetThingsDone/welcome.html',{'form':signupform})

		


def log_out(request):                                                               
	logout(request)
	return HttpResponseRedirect('../welcome/')


@csrf_exempt
def index(request):
	if request.user.is_authenticated():
		user1 = request.user.username
		items= toDo.objects.filter(user=request.user).order_by('-created')
		return render_to_response('GetThingsDone/index.html',{'items': items,'username': user1})
	elif request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(username=username, password=password)
		request.session['state']="Login Successful"
		request.session['username']=username
		login(request, user)
		return HttpResponseRedirect("../welcome")

@csrf_exempt
def addToDo(request):
	if request.method == 'POST':
		user = request.user
		heading = request.POST.get('heading')
		description = request.POST.get('description')
		new_todo=toDo.objects.create(user=user, heading=heading, description=description)
		new_todo.backend='django.contrib.auth.backends.ModelBackend'
		messages.add_message(request,messages.SUCCESS,'New ToDo Added.')
		return HttpResponseRedirect("../list")
		
	else:
		user = request.user.username
		items= toDo.objects.all()
		return render_to_response(request,'GetThingsDone/index.html',{'items': items,'username': user}, RequestContext(request))

@csrf_exempt
def delete(request):
	if request.method == 'POST':
		user = request.user
		itemId = request.POST.get('itemId')
		toDo.objects.filter(id=itemId).delete()
	return HttpResponseRedirect("../list")

