import urllib2
from PIL import Image
import struct
import wave

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

def create_White_noise(SAMPLE_LEN):
	#current method takes a conisderable amount of time
	noise_output = wave.open('noise.wav', 'w')
	noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
	values = pull_random_int(-32767, 32767, SAMPLE_LEN)
	for i in range(0, SAMPLE_LEN):
	        value = values[i]
	        packed_value = struct.pack('h', value)
	        noise_output.writeframes(packed_value)
	        noise_output.writeframes(packed_value)

	noise_output.close()


create_random_image()
create_White_noise(10000) #132,300 is 3 seconds
