# VirtualROV
Bachelor project

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
$ jtop\

Starting a streaming session: \
udp720.py \
$ python3 udpXXXX.py

To open the stream through VLC: \
$ udp -v udp-to-vlc.sdp
