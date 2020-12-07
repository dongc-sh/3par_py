# healthcheck user guide
healthcheck HPE 3par storage with python paramiko. The script has been verified in 3par OS 3.2.2MU6, 3.3.1MU2, with Python 3.8.2

1, The healthcheck script will work with command.txt and devive_info.txt.
command.txt               #Customize your healthcheck command(3par CLI command)
device_info.txt           #List the 3par storage IP,username,password

2, Customize the file path in the script

3, python healthcheck.py. Will get the seperated output files named as the 3par MGMT IP


