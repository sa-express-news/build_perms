from django.http import HttpResponse, Http404
from django.template import RequestContext, loader 

from django.shortcuts import render

from permits.models import ShapePermit, CouncilDistrictsPost, CouncilDistrictsPrior

def get_permits_by_year_by_district_post():
    post_permits_by_year_by_district = {}
    years_prior = range(2003,2013)
    years_post = range(2012,2015)

    post_dists = CouncilDistrictsPost.objects.all()

    for dist in post_dists:
        post_permits_by_year_by_district[dist.name] = {}   
        for year in years_post:
            post_permits_by_year_by_district[dist.name].update

            start_date = "%d-01-01" % year
            end_date = "%d-12-31" % year
            permit_count = len(ShapePermit.objects.filter(geom__within=dist.geom).filter(permit_dat__range=(start_date,end_date)))

            post_permits_by_year_by_district[dist.name].update({year:permit_count})

    return post_permits_by_year_by_district


def index(request):

    template = loader.get_template('permits/index.html')
    context = {'post_tots': get_permits_by_year_by_district_post()}

    return render(request, 'permits/index.html', context) 