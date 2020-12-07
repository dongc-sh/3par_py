# healthcheck user guide
healthcheck HPE 3par storage with python paramiko. The script has been verified in 3par OS 3.2.2MU6, 3.3.1MU2, with Python 3.8.2

1, The healthcheck script will work with command.txt and devive_info.txt.
command.txt               #Customize your healthcheck command(3par CLI command)
device_info.txt           #List the 3par storage IP,username,password

2, Customize the file path in the script

3, python healthcheck.py. Will get the seperated output files named as the 3par MGMT IP

# capacity collection user guide
collect 3par system information and capacity with HPE3parclient SDK
1, the collection script will work with device_info.txt.
device_info.txt           #List the 3par storage IP,username,password

2, Customize the file path in the script

3, python healthcheck.py. Will get the overall capacity information of the storage


...
Mgmt IP:10.x.x.x
version:3.2.2.709
hostname: storagename
model:HP_3PAR 7400
SN:1626754
###
SSD Total Capacity:0.0 GB
SSD Free Capacity:0.0 GB
FC Total Capacity:39312.0 GB
FC Free Capacity:13859.0 GB
NL Total Capacity:120318.0 GB
NL Free Capacity:41482.0 GB
#############################
