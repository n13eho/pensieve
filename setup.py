import os

start_dir = os.getcwd()

# mahimahi
os.system("sudo sysctl -w net.ipv4.ip_forward=1")

# copy the webpage files to /var/www/html
os.chdir( start_dir )
os.system("sudo cp video_server/myindex_*.html /var/www/html")
os.system("sudo cp video_server/dash.all.min.js /var/www/html")
os.system("sudo cp -r video_server/video* /var/www/html")
os.system("sudo cp video_server/Manifest.mpd /var/www/html")

# make results directory
os.system("mkdir cooked_traces")
os.system("mkdir rl_server/results")
os.system("mkdir run_exp/results")
os.system("mkdir real_exp/results")

# need to copy the trace and pre-trained NN model
print "Need to put trace files in 'pensieve/cooked_traces'."
print "Need to put pre-trained NN model in 'pensieve/rl_server/results'."
