import subprocess
import webbrowser

subprocess.call("ssh pi@192.168.0.101 'cd Projets/rekoo;raspistill -w 640 -h 480 -o rekoo_image.jpg'",shell=True)

message = "This looks like nothing!"

cmd = subprocess.Popen("ssh pi@192.168.0.101 'cd Projets/rekoo;sudo ./rekoo rekoo_image.jpg'",shell=True,stdout=subprocess.PIPE)
for line in cmd.stdout:
	if "REKOOGNIZED" in line:
		message = "This looks like a " + line.split()[1]
		break;

print message

subprocess.call("sh speech.sh " + message.replace(" ","+"), shell=True)

subprocess.call("scp pi@192.168.0.101:/home/pi/Projets/rekoo/rekoo_image.jpg rekoo_image.jpg")

searchTerm = message.rsplit(None, 1)[-1]

searchUrl = "http://www.google.com/search?q="+searchTerm+"&tbm=isch"
webbrowser.open(searchUrl)

qlmanage -p rekoo_image.jpg
