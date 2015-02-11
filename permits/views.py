from django.http import HttpResponse, Http404
from django.template import RequestContext, loader 

from django.shortcuts import render

from permits.models import ShapePermit, CouncilDistrictsPost, CouncilDistrictsPrior

def index(request):
    tot_post_permits = []
    years_prior = range(2003,2013)
    years_post = range(2012,2015)

    post_dists = CouncilDistrictsPost.objects.all()

    for dist in post_dists:
        print(dist.name)
        for year in years_post:
            print(year)
            start_date = "2012-01-01"
            end_date = "2012-12-31"
            ShapePermit.objects.filter(geom__within=dist.geom).filter(permit_dat__range=(start_date,end_date))


    print(years_prior[0])
    template = loader.get_template('permits/index.html')
    context = {'post_tots': tot_post_permits}

    return render(request, 'permits/index.html', context) 