from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Video, Flipbook, Tag, Category, Actor
from .forms import SearchForm
#from searchengine.documents import VideoDocument
#from haystack.query import SearchQuerySet

# Create your views here.
def index(request):
	#list all vidz
	vidz = Video.objects.filter(rating__gt=65)
	#vidz on eachpage
	paginator = Paginator(vidz, 20)
	page = request.GET.get('page')
	try:
		vidz = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer deliver the first page
		vidz = paginator.page(1)
	except EmptyPage:
	# If page is out of range deliver last page of results
		vidz = paginator.page(paginator.num_pages)
	return render(request, 'videos/index.html', {'page': page, 'tubes':vidz})

#search with basic
def post_search(request):
	query = request.GET.get('q')

	if query:
		results = Video.objects.filter(Q(title__icontains=query))
	else:
		results = Video.objects.filter(rating__gt=65.00)

	paginator = Paginator(results, 20)
	page = request.GET.get('page')
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
	except EmptyPage:
		results = paginator.page(paginator.num_pages)
	return render(request, 'videos/search.html', {'page': page, 'query': query, 'results': results})
	

#search with psql text search
'''
def post_search(request):
	form = SearchForm()
	query = None
	results = []

	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			query = form.cleaned_data['query']
			results = Video.objects.annotate(search=SearchVector('title')).filter(search=query)
	else:
		form = SearchForm()

	paginator = Paginator(results, 20)
	page = request.GET.get('page')
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
	except EmptyPage:
		results = paginator.page(paginator.num_pages)
	return render(request, 'videos/search.html', {'page': page, 'form': form, 'query': query, 'results': results})
'''	