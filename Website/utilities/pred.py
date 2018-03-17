# Part 3 - Making new predictions

import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import os
import sys

print(os.system("pwd"))
classifier = load_model('newer')

test_image = image.load_img(sys.argv[1], target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
	#result = result[0]
res = result[0]
i = 0
for r in res:
	print(r)
	if r >= 0.9:
		with open("/home/mozart/Alchemists-IMG/f.txt", 'w') as f:
			print("yes")
			f.write(str(i))
	i += 1
#print(classifier.classes)
#print(result)

