import csv

# Function to ask user which AP group to select
def select_ap_group():
    invalid = True
    ap_group = int(input("What AP Group should the APs belong to? (Select a number from above): "))
    try:
        group_name = resnet_ap_group_list[ap_group -1]
    except (IndexError, LookupError, ValueError):
        print(int(input("Please enter a valid number: ")))
    while invalid == True:
        try:
            response_valid = input("You chose the AP Group name %s, are you sure? (y/N): " % (group_name))
            if response_valid == "y":
                return group_name
                invalid = False
            elif response_valid == "N":
                select_ap_group()
        except:
            break

# Function to print list of CLI commands that change AP name and AP group
def print_cli_commands():
    group_name = select_ap_group()
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

# Pull list of ResNET AP Groups from file and create a list
ap_group_file = open('/Users/keithmiller/Work/resnet-ap-groups.txt', mode='r')
resnet_ap_group_list = (ap_group_file.read().splitlines())
ap_group_file.close()

# Create empty list to give AP Groups a number and set starting number to 1
numbered_ap_groups = []
count = 1

# Loop through AP Group list and append/increment number string to group names
for group in resnet_ap_group_list:
    numbered_ap_groups.append("%s. %s" % (count,group))
    count += 1

# Print list of numbered AP groups
for option in numbered_ap_groups:
    print(option)

print_cli_commands()
