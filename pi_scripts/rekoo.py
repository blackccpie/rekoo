import subprocess

subprocess.call('raspistill -w 640 -h 480 -o rekoo_image.jpg',shell=True)

message = "This looks like nothing!"

cmd = subprocess.Popen('sudo ./rekoo rekoo_image.jpg',shell=True,stdout=subprocess.PIPE)
for line in cmd.stdout:
	if "REKOOGNIZED" in line:
		message = "This looks like a " + line.split()[1]
		break;
		
print message

subprocess.call('sh speech.sh ' + message, shell=True)
		
