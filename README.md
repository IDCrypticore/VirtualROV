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


  
Starting a streaming session: \
udp720.py \
$ python3 udpXXXX.py

To open the stream through VLC: \
$ udp -v udp-to-vlc.sdp
