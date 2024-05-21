#Upload 170
import logging
import os


def init(path_selected):
	path = path_selected
	logging.info("adding direcotry of wit")
	wit = os.makedirs(path +"/.wit", exist_ok = True)
	wit_images = os.makedirs(path + "/.wit/images", exist_ok = True)
	wit_staging_area =  os.makedirs(path + "/.wit/staging_area", exist_ok = True)
	activted = path + "/.wit" + "/activted.txt"
	with open(activted, "w") as txt:
		txt.write("")
	logging.info("direcotry add to the current diractory")		
	
if __name__ == "__main__":
	init(r"C:\Users\User\wit_project\test_folder")

