# VirtualROV
This repositories contains the scripts for streaming in 720p and 1080p, additionally the scripts for running the SER-110X servo either manually or scheduled.
The usb-state.py is a script to schedule when to power on/off the USB port of which the battery charger are connected to.

# Dependency libraries
cmake \
build-essential \
pkg-config \
libx11-dev \
libgtk-3-dev \
libexpat1 -dev \
libjpeg-dev \
libgstreamer1.0 -dev \
libgstreamer-plugins-base1.0-dev \
libv4l-dev \
v4l-utils \
Openssh-server \
gtk-doc-tools \
gstreamer1.0 -alsa \
gstreamer1.0 -plugins-base \
gstreamer1.0 -plugins-good \
gstreamer1.0 -plugins-bad \
gstreamer1.0 -plugins-ugly \
gstreamer1.0 -libav \
libgstreamer1.0 -dev \
libgstreamer -plugins-base1.0-dev \
libgstreamer-plugins-good1.0-dev \
libgstreamer-plugins-bad1.0-dev  

# Other requirements
- Linux Ubuntu 18.04
- Python 2 and Python 3.6
- OpenCV 3 or OpenCV 4
- numpy
- schedule
- time


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
$ sudo nvpmodel -m 0 #To set the Xavier in max mode \
$ sudo jetson_clocks \
\
$ python3 <insert-udp-script>.py \
  or
$ ./<insert-udp-script>.py
\
Open new Terminal on receiving computer \
$ python3 udp-receive.py \
  or \
$ ./udp-receive.py \

To receive the stream through VLC: \
- Changing the IP-address in the sdp is necessary. 
$ udp -v udp-to-vlc.sdp
  
To record the UDP stream: \
$ python3 udp-rec.py \
  or \
$ ./udp-rec.py

# Servo
There are currently two servo scripts, where the ser-110x.py script is used to manually run the servo by typing in 1 + enter, and 2 + enter to stop. \
The scheduled.py script is to schedule a cleaning interval. \
The interval is currently set to run every 5 seconds for testing purposes, but other options are tagged in the script and can replace the 5 second function. \
\
$ sudo python3 scheduled.py \
  or \
$ python3 ser-110x.py

# USB on/off
A battery charger is connected to the USB port on the Xavier, whereas the usb-state.py script is used to schedule when the USB port will be enabled / disabled. \
The interval should be lower than the time it takes to fully charge the battery. \
  \
$ sudo python3 usb-state.py \
  \
The interval is currently set to run every 10 seconds for testing purposes, but other options are tagged in the script and can replace the 10 second function. \
This script rewrites the state within the state file located in /sys/class/regulator/regulator.13, but a safer option would be to implement a voltmeter to read the battery voltage, and rewrite the script to enable/disable the USB port based on that value.

Manually enable/disable USB port:
- Replace 'new-state' with enabled or disabled
  $ sudo -s \
  $ cd /sys/class/regulator/regulator.13 \
  $ echo 'new-state' > state

# Copying files to or from the Xavier
  Copy file from Xavier to receiving computer: \
  $ scp tenteam10@<IP-address>:/home/tenteam10/'file-location'/'file-name' /path/to/destination/on/receiving/computer \
  \
  Copy file from computer to Xavier: \
  $ scp /home/'user'/'file-location'/'file-name' tenteam10@'IP-address':/home/tenteam10

  # Sources
- https://github.com/JetsonHacksNano/CSI-Camera
- https://forums.developer.nvidia.com/t/gstreamer-python-script-to-send-and-receive-udp-stream/176718/8
- https://forums.developer.nvidia.com/t/switch-on-and-off-usb-ports-programmatically-on-agx/142974/4
- https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/using-the-adafruit-library

  
