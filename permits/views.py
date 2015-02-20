from django.http import HttpResponse, Http404
from django.template import RequestContext, loader 
from django.shortcuts import render

from permits.models import ShapePermit, CouncilDistrictsPost, CouncilDistrictsPrior
from django.db.models import Sum 

def get_permits_by_year_by_district_post():
    post_permits_by_year_by_district = {}
    years_post = range(2013,2015)

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

def get_permits_by_year_by_district_prior():
    prior_permits_by_year_by_district = {}
    years_prior = range(2003,2013)

    prior_dists = CouncilDistrictsPrior.objects.all()

    for dist in prior_dists:
        prior_permits_by_year_by_district[dist.name] = {}
        for year in years_prior:
            prior_permits_by_year_by_district[dist.name].update


            start_date = "%d-01-01" % year
            end_date = "%d-12-31" % year
            permit_count = len(ShapePermit.objects.filter(geom__within=dist.geom).filter(permit_dat__range=(start_date,end_date)))

            prior_permits_by_year_by_district[dist.name].update({year:permit_count})


    return prior_permits_by_year_by_district


def sum_amounts_by_year_by_district_prior():
    prior_permits_by_year_by_district_sum = {}
    years_prior = range(2003,2013)

    prior_dists = CouncilDistrictsPrior.objects.all()

    for dist in prior_dists:
        prior_permits_by_year_by_district_sum[dist.name] = {}
        for year in years_prior:
            prior_permits_by_year_by_district_sum[dist.name][year] = {}
            print(prior_permits_by_year_by_district_sum)

            start_date = "%d-01-01" % year
            end_date = "%d-12-31" % year

            amt_sum = ShapePermit.objects.filter(geom__within=dist.geom).filter(permit_dat__range=(start_date,end_date)).aggregate(Sum('declvltn'))

            prior_permits_by_year_by_district_sum[dist.name][year].update({ 'total_amount' : amt_sum['declvltn__sum'] })
            amt_per_acre = (amt_sum['declvltn__sum']/dist.acres)

            prior_permits_by_year_by_district_sum[dist.name][year].update({'amt_per_acre' : amt_per_acre})

    return prior_permits_by_year_by_district_sum


def index(request):

    sum_amounts_by_year_by_district_prior()


    template = loader.get_template('permits/index.html')
    context = { 
                'post_tots': get_permits_by_year_by_district_post(), 
                'prior_tots': get_permits_by_year_by_district_prior(),
                'amts': sum_amounts_by_year_by_district_prior() 
              }

    return render(request, 'permits/index.html', context)





 