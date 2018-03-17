from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.conf import settings
from django.http import HttpResponseRedirect
<<<<<<< HEAD
#from .utilities import pred
import os
=======

>>>>>>> c03188dc0ff313c8c51158003f12d9642ce18a87
# Create your views here.
def index(request):
	form = ImageForm()

	if request.method == 'POST':

		root = settings.MEDIA_ROOT
		myfile = request.FILES['myfile']
<<<<<<< HEAD

		vvid = Image()
		vvid.image = myfile
		vvid.save()

		vids = '/media/' + str(vvid.image)

		picname = "/home/mozart/Alchemists-IMG/IMGfilter" + vids

		os.system("sudo python2 Website/utilities/pred.py " + picname)

		with open("/home/mozart/Alchemists-IMG/f.txt", 'r') as f:
			num = f.read()
#		num = pred.fn(picname)

		print(num)

		if myfile:
			return render(request, 'Website/index.html', {'form': form, 'vid': myfile, 'resu': vids, 'fil': num})
=======
		
		vvid = Image()
		vvid.image = myfile
		vvid.save()
 
		vids = '/media/' + str(vvid.image)

		if myfile:
			return render(request, 'Website/index.html', {'form': form, 'vid': myfile, 'resu': vids})
>>>>>>> c03188dc0ff313c8c51158003f12d9642ce18a87
		else:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		vid = Image.objects.all()
		#print vid
		vid.delete()
		vid = None
<<<<<<< HEAD

		return render(request, 'Website/index.html', {'form': form, 'vid': vid})
=======
		
		return render(request, 'Website/index.html', {'form': form, 'vid': vid})
>>>>>>> c03188dc0ff313c8c51158003f12d9642ce18a87
