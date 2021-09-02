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

3, python 3par_CollectionToExcel.py, get the overall capacity information of the storage, export to the Excel table.

<img width="914" alt="微信图片_20210902153420" src="https://user-images.githubusercontent.com/65651866/131802109-891a5c7f-5f30-4953-9938-a6634e2a9742.png">


