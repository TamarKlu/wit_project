#Upload 170
import os
def init():
	path = os.getcwd()
	if not os.path.exists(path + "/.wit."):
		wit = os.mkdir(path +"/.wit.")
		wit_images = os.mkdir(path + "/.wit/images")
		wit_staging_area =  os.mkdir(path + "/.wit./staging_area")
		activted = path + "/.wit" + "/activted.txt"
		with open(activted, "w") as txt:
			txt.write("")
			
	
if __name__ == "__main__":
	init()

