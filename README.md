# VirtualROV
This repositories contains the scripts for streaming in 720p and 1080p, additionally the scripts for running the SER-110X servo either manually or scheduled.
The usb-state.py is a script to schedule when to power on/off the USB port of which the battery charger are connected to.

# SSH connection and remote desktop
If your computer is directly connected to the injector by ethernet, manually set your IP-address to 192.168.1.1 and gateway to 192.168.1.3
If you want to connect to the virtualROV by being in the same local network, the network settings on the Jetson must be set to automatic.

Establish a ssh session with the Xavier: \
$ssh tenteam10@<IP-address> \
  or \
$ ssh tenteam10@tenteam10-desktop \
\
Use JTOP to control fan: \
In Terminal on Xavier: \
$ x11vnc \
\
In Terminal on receiving computer: \
$ gvncviewer tenteam10-desktop:0 or 1 (Information given by x11vnc)
or \
$ gvncviewer IP-address:0 or 1 (Set the Xaviers IP-address) \
\
In Terminal on Jetson: \
$ jtop

# Streaming
You can either stream in 720p or 1080p, record or use VLC. \
Remember to replace <IP-address-of-receiving-computer> with the IP-address of the receiving computer in the python script. 
- udp720.py and udp1080.py have <IP-address-of-receiving-computer> to be replaced 
- udp720direct.py and udp1080direct.py is streaming to 192.168.1.1 
- udp720self.py is streaming to the Jetson itself (127.0.0.1) 
- udp-receive is to receive the stream on port 5000 
- udp-rec.py is to record the stream, but is not visible before the user has stopped the recording. 
- udp-to-vlc.sdp is used to view the stream in VLC. 
\
Make sure an ssh session has been established.\
In Terminal of tenteam10-desktop (Jetson):\
$ python3 <insert-udp-script>.py \
  or
$ ./<insert-udp-script>.py
\
Open new Terminal on receiving computer \
$ python3 udp-receive.py \
  or \
$ ./udp-receive.py \

To receive the stream through VLC: \
$ udp -v udp-to-vlc.sdp
  
To record the UDP stream:
$ python3 udp-rec.py 
  or
$ ./udp-rec.py
