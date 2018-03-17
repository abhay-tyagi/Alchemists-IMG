from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.conf import settings
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	form = ImageForm()

	if request.method == 'POST':

		root = settings.MEDIA_ROOT
		myfile = request.FILES['myfile']
		
		vvid = Image()
		vvid.image = myfile
		vvid.save()
 
		vids = '/media/' + str(vvid.image)

		if myfile:
			return render(request, 'Website/index.html', {'form': form, 'vid': myfile, 'resu': vids})
		else:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		vid = Image.objects.all()
		#print vid
		vid.delete()
		vid = None
		
		return render(request, 'Website/index.html', {'form': form, 'vid': vid})