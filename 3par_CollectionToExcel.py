#import pprint
import time
import urllib3
import xlsxwriter
from hpe3parclient import client

class HPE3parcollection:
    row = 1

    def __init__(self, hpe3parip, username, password, workbook, worksheet):
        self.connection = client.HPE3ParClient('https://%s:8080/api/v1' % hpe3parip)
        self.connection.setSSHOptions(ip=hpe3parip, login=username, password=password)
        self.connection.login(username, password)



    def getsysteminfo(self):
        global storagename,systemVersion,Serialnumber,MgmtIP,storagemodel

        systeminfo = self.connection.getStorageSystemInfo()
        systemVersion = systeminfo['systemVersion']
        storagename = systeminfo['name']
        storagemodel = systeminfo['model']
        Serialnumber = systeminfo['serialNumber']
        MgmtIP = hpe3parip
        self.connection.logout()


    def getcapactiy(self):
        global SSDtotal,SSDFree,FCtotal,FCFree,NLtotal,NLFree
        capacity = self.connection.getOverallSystemCapacity()
        SSDtotal = int(capacity['SSDCapacity']['totalMiB'])/1024
        SSDFree = int(capacity['SSDCapacity']['freeMiB'])/1024
        FCtotal = int(capacity['FCCapacity']['totalMiB']) / 1024
        FCFree = int(capacity['FCCapacity']['freeMiB']) / 1024
        NLtotal = int(capacity['NLCapacity']['totalMiB']) / 1024
        NLFree = int(capacity['NLCapacity']['freeMiB']) / 1024
        self.connection.logout()


    def write_excel(self):
        global storagename,storagemodel,systemVersion,Serialnumber,MgmtIP,SSDtotal,SSDFree,FCtotal,FCFree,NLtotal,NLFree
        datainsert=[storagename,storagemodel,systemVersion,Serialnumber,MgmtIP,SSDtotal,SSDFree,FCtotal,FCFree,NLtotal,NLFree]
        worksheet.write_row(HPE3parcollection.row, 0, datainsert)
        HPE3parcollection.row += 1



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
dev_filepath = r"C:\\users\c64146\PycharmProjects\HP3par\device_info.txt"
dev_file = open(dev_filepath, "r")


workbook = xlsxwriter.Workbook("chart_3par.xlsx")
worksheet = workbook.add_worksheet('sheet1')
worksheet.set_column(0, 100, 13)
headings = ['hostname','Model','Version','SN','Mgmt IP','SSD total(GB)','SSD free(GB)','FC total(GB)','FC free(GB)','NL total(GB)','NL free(GB)']
bold = workbook.add_format({'bold': 1,'fg_color': '#D7E4BC', 'color': 'Black'})
worksheet.write_row(0, 0, headings, bold)



while 1:
    dev_info = dev_file.readline()
    if not dev_info:
        break
    else:
        devs = dev_info.split(',')
        hpe3parip = devs[0]
        username = devs[1]
        password = devs[2].strip()
        password = password.strip('\n')
        result = HPE3parcollection(hpe3parip, username, password, workbook, worksheet)
        result.getsysteminfo()
        result.getcapactiy()
        result.write_excel()
        print("collection completed at %s" %hpe3parip)
        time.sleep(1)

workbook.close()
dev_file.close()


