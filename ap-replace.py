import csv


file = open('/Users/keithmiller/Work/resnet-ap-groups.txt', mode='r')
resnet_ap_group_list = (file.read().splitlines())
file.close()

numbered_groups = []
count = 1

for group in resnet_ap_group_list:
    numbered_groups.append("%s. %s" % (count,group))
    count += 1

for group in numbered_groups:
    print(group)

ap_group = input("What AP Group should the APs belong to? (Select a number from above): ")

if ap_group == "1":
    group_name = resnet_ap_group_list[0]
elif ap_group == "2":
    group_name = resnet_ap_group_list[1]
elif ap_group == "3":
    group_name = resnet_ap_group_list[2]
elif ap_group == "4":
    group_name = resnet_ap_group_list[3]
elif ap_group == "5":
    group_name = resnet_ap_group_list[4]
elif ap_group == "6":
    group_name = resnet_ap_group_list[5]
elif ap_group == "7":
    group_name = resnet_ap_group_list[6]
elif ap_group == "8":
    group_name = resnet_ap_group_list[7]
elif ap_group == "9":
    group_name = resnet_ap_group_list[8]
elif ap_group == "10":
    group_name = resnet_ap_group_list[9]
elif ap_group == "11":
    group_name = resnet_ap_group_list[10]
elif ap_group == "12":
    group_name = resnet_ap_group_list[11]
elif ap_group == "13":
    group_name = resnet_ap_group_list[12]
elif ap_group == "14":
    group_name = resnet_ap_group_list[13]
elif ap_group == "15":
    group_name = resnet_ap_group_list[14]
elif ap_group == "16":
    group_name = resnet_ap_group_list[15]
elif ap_group == "17":
    group_name = resnet_ap_group_list[16]
elif ap_group == "18":
    group_name = resnet_ap_group_list[17]
elif ap_group == "19":
    group_name = resnet_ap_group_list[18]
elif ap_group == "20":
    group_name = resnet_ap_group_list[19]
elif ap_group == "21":
    group_name = resnet_ap_group_list[20]
else:
    exit()

with open('/Users/keithmiller/Work/ib-import-carmichael06062019.csv', mode='r') as input_file:
    reader = csv.reader(input_file)
    list = []
    print("""
    !!! Printing CLI comnmands !!!

    """)
    for row in reader:
        list.append(row)
    for row in list[1:]:
        print("ap-rename ap-name %s %s" % (row[2],row[3]))
        print("ap-regroup ap-name %s %s" % (row[3],group_name))
