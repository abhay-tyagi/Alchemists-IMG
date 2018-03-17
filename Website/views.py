from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.conf import settings
from django.http import HttpResponseRedirect

#from .utilities import pred
import os

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

		picname = "/home/mozart/Alchemists-IMG/IMGfilter" + vids

		os.system("sudo python2 Website/utilities/pred.py " + picname)

		with open("/home/mozart/Alchemists-IMG/f.txt", 'r') as f:
			num = f.read()

#		num = pred.fn(picname)

		print(num)

		return render(request, 'Website/index.html', {'form': form, 'vid': myfile, 'resu': vids, 'fil1': num[0], 'fil2': num[1], 'fil3': num[2]})

	else:
		return render(request, 'Website/index.html', {'form': form})
