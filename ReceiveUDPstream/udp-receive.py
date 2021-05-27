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

# Defining the GStreamer pipeline, searching for stream on port 5000.
#gst_str = "nvarguscamerasrc ! video/x-raw(memory:NVMM),format=(string)NV12,width=(int)640,height=(int)480, framerate=30/1 ! nvvidconv ! xvimagesink "
gst_str = "udpsrc port=5000 ! application/x-rtp,encoding-name=H264 ! rtpjitterbuffer latency=1000 drop-on-latency=false ! rtph264depay ! h264parse! avdec_h264 ! xvimagesink"

# Creating the pipeline.
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
