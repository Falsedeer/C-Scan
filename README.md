# G-Banner
Banner grabbing and port scanning via socket module in python
# Usage
python3 g-banner.py -t \<target host\> -p \<single or multiple ports to scan\>

This program will try to resolv the provided target by gethostbyname() in python,  
and attempt to connect to the target host via the selected port,  
to determine whether it is open or close|filterd.  

Then, it will send some data to the target port,  
in order to grab the banner of the service.  
