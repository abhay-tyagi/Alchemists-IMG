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

		vidss = 'IMGfilter/' + vids
		picname = os.path.join(settings.BASE_DIR, vidss);

		os.system("sudo python2 Website/utilities/pred.py " + picname)

		with open(os.path.join(settings.BASE_DIR, "f.txt"), 'r') as f:
			num = f.read()

		num = num[1:]
		num = num[0:len(num)-1]

		num = num.split(',')

#		num = pred.fn(picname)
		# num = list(num)
		print(num)

		return render(request, 'Website/index.html', {'form': form, 'vid': myfile, 'resu': vids, 'fil1': int(num[0]), 'fil2': int(num[1]), 'fil3': int(num[2])})

	else:
		return render(request, 'Website/index.html', {'form': form})
