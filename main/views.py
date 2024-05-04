from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.views import generic
from django.utils.decorators import method_decorator
from destination.models import Places
from ratinghome.models import Rateinfo
# Create your views here.


@login_required(login_url='login')   
def mainpageview(request):
    return render(request ,"main.html" ) 

@login_required 
def profilepage(request):
    return render(request, 'profilehome.html')
    


@method_decorator(login_required, name='dispatch')
class Searchplace(generic.ListView):

    model = Places
    template_name = 'searchplace.html'
    def get_context_data(self, **kwargs):
        
            search_term =  self.request.GET.get('searched')
           
            places = Places.objects.all().order_by('name')
            object_list=[]
            
            if(search_term==None or search_term==''):
                pass
            else:
                
                
                searchlist = search_term.split()
                for word in searchlist:
                    object_list += Places.objects.filter(name__icontains=word)
                for word in searchlist:
                    for place in places:
                        tags = place.rateinfo.tags
                        tags = ' '.join(tags)
                        genres = place.rateinfo.genres
                        genres = ' '.join(genres)
                        if (word in tags):
                            object_list.append(place)
                        if (word in genres):
                            object_list.append(place)
                        
                    
            context = super(Searchplace, self).get_context_data(**kwargs)
            context.update({
                'object_list':sorted(object_list, key = lambda x : x.name),
                'searchterm': search_term
            })
            return context
        
        
    
