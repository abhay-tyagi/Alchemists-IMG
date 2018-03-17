# Part 3 - Making new predictions

import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import os
import sys

print(os.system("pwd"))
classifier = load_model('newest')

#from keras.preprocessing.image import ImageDataGenerator

test_image = image.load_img(sys.argv[1], target_size = (64, 64))
#test_datagen = ImageDataGenerator(rescale = 1./255)

#test_set = test_datagen.flow_from_directory('

test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
	#result = result[0]
res = result[0]
i = 0

all = []

for r in res:
	print(r)
	if r > 0:
		all.append(i)
	i += 1

import random

if len(all) > 3:
	all = all[0:3]
elif len(all) < 3:
	while(len(all) != 3):
		numb = random.randrange(0, 22)
		if numb not in all:
			all.append(numb)

with open("/home/mozart/Alchemists-IMG/f.txt", 'w') as f:
	f.write(str(all))


#print(classifier.classes)
#print(result)

