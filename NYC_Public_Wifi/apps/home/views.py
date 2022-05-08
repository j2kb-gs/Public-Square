
from datetime import datetime
from email import message
from django.shortcuts import get_object_or_404, redirect, render

from django.shortcuts import render,redirect


# Create your views here.
from django import template
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from .forms import ReviewForm
from .models import Hotspot_Location, Hotspot_Neighborhood, Review
from django.contrib.auth.models import User

from .forms import BoroughForm, NeighborhoodForm, ProviderForm
from .models import Hotspot_Location, Neighborhood, Provider
from django.contrib import messages

from django.core.paginator import Paginator


#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query: 
            lookups = (
                Q(ntacode__ntacode__icontains=query) | Q(ntacode__postcode__icontains=query) |
                Q(ntacode__nta__icontains=query) | 
                Q(obj_id__location__icontains=query) |
                Q(obj_id__loc_name__icontains=query) |
                Q(obj_id__hotspot_borough__boro_code__name__icontains=query)

            )
            results = Hotspot_Neighborhood.objects.filter(lookups).distinct()

            context = {'results': results, 'submitbutton':submitbutton}
            return render(request, 'home/search.html', context)
        else:
            return render(request, 'home/index.html')
    else:
        return render(request, 'home/index.html')


def hotspot_profile(request, pk):
    hotspot = Hotspot_Neighborhood.objects.filter(obj_id=pk)

    if not hotspot.exists():
        raise Http404
    else:
        hotspot = hotspot.first()
    
    context = { 'hotspot':hotspot, }
    return render(request, 'home/hotspot_profile.html', context)


#--------------------------------------------------------------------------#
#--------------------------- Reviews Related ------------------------------#
#--------------------------------------------------------------------------#

def review_detail(request, pk):
    rev = Review.objects.filter(obj_id= pk)
    return render (request, 'home/review_detail.html', {'rev':rev})

def hotspot_reviews(request, pk):
    hot = Hotspot_Location.objects.filter(obj_id= pk)
    rev = Review.objects.filter(obj_id= pk)
    hotspot = Hotspot_Neighborhood.objects.filter(obj_id=pk)
    form = ReviewForm()



    if not hotspot.exists():
        raise Http404
    else:
        hotspot = hotspot.first()

    form = ReviewForm()
    context = {'hotspot': hotspot, 'form': form, 'rev': rev, 'hot':hot}
    return render(request, 'home/hotspot_reviews.html', context)

@login_required(login_url="/login/")
def add_review(request, pk):
    hotspot = Hotspot_Location.objects.filter(obj_id= pk)
    form = ReviewForm(request.POST)

    if not hotspot.exists():
        raise Http404
    else:
        hotspot = hotspot.first()


    if form.is_valid():
        rate = form.cleaned_data['rate']
        review = form.cleaned_data['review']
        owner = request.user

        rev = Review()
        rev.obj_id = hotspot
        rev.rate = rate
        rev.owner = owner
        rev.review = review
        rev.date_added = datetime.now()
        rev.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        context = {'hotspot': hotspot, 'form': form}
            
        return HttpResponseRedirect(reverse('hotspot_reviews', args=(pk,)))

    return render(request, 'home/hotspot_reviews.html', context)

@login_required(login_url="/login/")
def delete_review(request):
    if request.method =='POST':
        ids = ()
        data = request.POST.copy()
        data.pop('csrfmiddlewaretoken', None) # remove csrf_token
        for key in data.keys():
            ids = ids + (str(key))
            for s in range (0, len(ids)):
                owner = User.objects.get(user_pk = request.user.id)
                hotspot = Hotspot_Location.objects.get(pk = id[s])

                obj = Review.objects.get(owner = owner, obj_id = hotspot)

                obj.deleted = True
                obj.save()
                message.success(request, 'Successfully deleted!')

        return redirect('user_reviews')

def best_rated_reviews(request):
    hotspot = Hotspot_Location.objects.all()
    return render (request, 'home/best_rated_reviews.html', {'hotspot':hotspot})

@login_required(login_url="/login/")
def user_reviews(request):
    owner = User.objects.get(user_pk = request.user.id)
    rev = Review.objects.get(owner = owner, deleted = False)
    context = {
        'rev':rev
    }

    return render (request, 'home/user_reviews.html', context )
    

#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def add_borough(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = BoroughForm(request.POST)
			if form.is_valid():
					form.save()
					return 	HttpResponseRedirect('/add_borough?submitted=True')	
		else:
			form = BoroughForm(request.POST)
			if form.is_valid():
				#form.save()
				event = form.save(commit=False)
				event.manager = request.user # logged in user
				event.save()
				return 	HttpResponseRedirect('/add_borough?submitted=True')	
	else:
		# Just Going To The Page, Not Submitting 
		if request.user.is_superuser:
			form = BoroughForm
		else:
			form = BoroughForm

		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'home/add-borough.html', {'form':form, 'submitted':submitted})


#Add Neigborhood
def add_neighborhood(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = NeighborhoodForm(request.POST)
			if form.is_valid():
					form.save()
					return 	HttpResponseRedirect('/add_neighborhood?submitted=True')	
		else:
			form = NeighborhoodForm(request.POST)
			if form.is_valid():
				#form.save()
				event = form.save(commit=False)
				event.manager = request.user # logged in user
				event.save()
				return 	HttpResponseRedirect('/add_neighborhood?submitted=True')	
	else:
		# Just Going To The Page, Not Submitting 
		if request.user.is_superuser:
			form = NeighborhoodForm
		else:
			form = NeighborhoodForm

		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'home/add-neighborhood.html', {'form':form, 'submitted':submitted})



###### ADD OBJECTS ######

#Add Provider
def add_provider(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = ProviderForm(request.POST)
			if form.is_valid():
					form.save()
					return 	HttpResponseRedirect('/add_provider?submitted=True')	
		else:
			form = ProviderForm(request.POST)
			if form.is_valid():
				#form.save()
				event = form.save(commit=False)
				event.manager = request.user # logged in user
				event.save()
				return 	HttpResponseRedirect('/add_provider?submitted=True')	
	else:
		# Just Going To The Page, Not Submitting 
		if request.user.is_superuser:
			form = ProviderForm
		else:
			form = ProviderForm

		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'home/add-provider.html', {'form':form, 'submitted':submitted})

#### LIST OBJECTS ####

def neighborhood_list(request):
    neighborhood_list = Neighborhood.objects.all().order_by('ntcaode')
    return render(request, 'home/neighborhood-list.html',
               {'neighborhood_list':neighborhood_list})
    
def hotspot_list(request):
    hotspot_list = Hotspot_Location.objects.all().order_by('obj_id')
    return render(request, 'home/hotspot-list.html',
               {'hotspot_list':hotspot_list})

def provider_list(request):
    provider_list = Provider.objects.all().order_by('prov_id')
    return render(request, 'home/provider-list.html',
               {'provider_list':provider_list})

##### UPDATE OBJECTS #####

def update_neighborhood(request, ntacode):
	event = Neighborhood.objects.get(ntcaode=ntacode)
	if request.user.is_superuser:
		form = NeighborhoodForm(request.POST or None, instance=event)	
	else:
		form = NeighborhoodForm(request.POST or None, instance=event)
	
	if form.is_valid():
		form.save()
		return redirect('neighborhood-list')

	return render(request, 'home/update-neighborhood.html', 
		{'event': event,
		'form':form})
 
def update_hotspot(request, obj_id):
	event = Hotspot_Location.objects.get(obj_id=obj_id)
	if request.user.is_superuser:
		form = BoroughForm(request.POST or None, instance=event)	
	else:
		form = BoroughForm(request.POST or None, instance=event)
	
	if form.is_valid():
		form.save()
		return redirect('hotspot-list')

	return render(request, 'home/update-hotspot.html', 
		{'event': event,
		'form':form})
 
 
def update_provider(request, prov_id):
	event = Provider.objects.get(prov_id=prov_id)
	if request.user.is_superuser:
		form = ProviderForm(request.POST or None, instance=event)	
	else:
		form = ProviderForm(request.POST or None, instance=event)
	
	if form.is_valid():
		form.save()
		return redirect('provider-list')

	return render(request, 'home/update-provider.html', 
		{'event': event,
		'form':form})

#### DELETE OBJECTS ####

# Delete an Neighborhood
def delete_neighborhood(request, ntacode):
	event = Neighborhood.objects.get(ntcaode=ntacode)
	if request.user.is_superuser:
		event.delete()
		messages.success(request, ("Nieghborhood Deleted!!"))
		return redirect('neighborhood-list')		
	else:
		messages.success(request, ("You Aren't Authorized To Delete This Neighborhood!!"))
		return redirect('neighborhood-list')		

# Delete a Hotspot
def delete_hotspot(request, obj_id):
	event = Hotspot_Location.objects.get(obj_id=obj_id)
	if request.user.is_superuser:
		event.delete()
		messages.success(request, ("Hotspot Location Deleted!!"))
		return redirect('hotspot-list')		
	else:
		messages.success(request, ("You Aren't Authorized To Delete This Hotspot Lcoation!!"))
		return redirect('hotspot-list')		

# Delete a Provider
def delete_provider(request, prov_id):
	event = Provider.objects.get(prov_id=prov_id)
	if request.user.is_superuser:
		event.delete()
		messages.success(request, ("Provider Deleted!!"))
		return redirect('provider-list')		
	else:
		messages.success(request, ("You Aren't Authorized To Delete This Provider!!"))
		return redirect('provider-list')		
