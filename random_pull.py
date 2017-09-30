import urllib2
from PIL import Image



def pull_random_int(bottom,top,amount):
	response = urllib2.urlopen("https://www.random.org/integers/?num={num}&min={min}&max={max}&col=1&base=10&format=plain&rnd=new".format(num=amount,min=bottom,max=top)).read()
	response = response.split('\n')[0:-1]
	return(map(int, response))


def create_random_image():
	img = Image.new( 'RGB', (128,128), "black") # create a new black image
	pixels = img.load()
	randoms = pull_random_int(0,255,128)
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			pixels[i,j] = (randoms[i], randoms[j], 100)
	img.show()


create_random_image()
