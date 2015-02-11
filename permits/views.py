from django.http import HttpResponse, Http404
from django.template import RequestContext, loader 

from django.shortcuts import render

from permits.models import ShapePermit, CouncilDistrictsPost, CouncilDistrictsPrior

def index(request):
    years_prior = range(2003,2013)

    post_dists = CouncilDistrictsPost.objects.all()

    for dist in post_dists:
        len(ShapePermit.objects.filter(geom__within=dist.geom).filter(permit_dat__range=("2012-01-01","2012-12-31")))


    template = loader.get_template('permits/index.html')
    context = {'years': years_prior}

    return render(request, 'permits/index.html', context) 