#!/usr/bin/env python

import signal
import sys
import time
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

# Signal handler for stopping pipeline before destruction.
def signal_handler(sig, frame):
    p.set_state(Gst.State.NULL)
    sys.exit(0)

# Initialize GStreamer.
GObject.threads_init()
Gst.init(None)

# Defining the GStreamer pipeline.
# X and Y positions can be changed, for instance to a 2x2 grid, as well as the width and height on the display windows.
gst_str = "nvcompositor name=mix background-w=1920 background-h=270 \
    sink_3::xpos=0    sink_3::ypos=0   sink_3::width=480 sink_3::height=270 \
    sink_2::xpos=480  sink_2::ypos=0   sink_2::width=480 sink_1::height=270 \
    sink_1::xpos=960  sink_1::ypos=0   sink_1::width=480 sink_2::height=270 \
    sink_0::xpos=1440 sink_0::ypos=0   sink_0::width=480 sink_0::height=270 \
    ! video/x-raw(memory:NVMM),format=RGBA, width=1920,height=270 ! nvvidconv flip_method=0 ! video/x-raw(memory:NVMM),format=I420 ! nvv4l2h264enc insert-vui=1 insert-sps-pps=1 ! h264parse ! rtph264pay ! udpsink host=192.168.1.1 port=5000  \
    nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM),format=NV12,width=480,height=270,framerate=30/1 ! queue ! mix.sink_0    \
    nvarguscamerasrc sensor-id=1 ! video/x-raw(memory:NVMM),format=NV12,width=480,height=270,framerate=30/1 ! queue ! mix.sink_1    \
    nvarguscamerasrc sensor-id=2 ! video/x-raw(memory:NVMM),format=NV12,width=480,height=270,framerate=30/1 ! queue ! nvvidconv flip_method=2 ! mix.sink_2    \
    nvarguscamerasrc sensor-id=3 ! video/x-raw(memory:NVMM),format=NV12,width=480,height=270,framerate=30/1 ! queue ! mix.sink_3 "

# Creating the pipeline
p = Gst.parse_launch (gst_str)

# Register signal handler in order to terminate the session if receiving SIGINT, for instance Ctrl-C.
signal.signal(signal.SIGINT, signal_handler)

# Start the pipeline
p.set_state(Gst.State.READY)
p.set_state(Gst.State.PAUSED)
p.set_state(Gst.State.PLAYING)

# Running session for 1000 seconds, before exit.
# This can be set to another desired value.
time.sleep(1000)

# Done. Stop the pipeline before clean up on exit.
p.set_state(Gst.State.NULL)
exit(0)
