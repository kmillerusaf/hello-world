import csv
import sys

# Function to ask user which AP group to select
# def select_ap_group():
#    invalid = True
#    ap_group = int(input("What AP Group should the APs belong to? (Select a number from above): "))
#    try:
#        group_name = resnet_ap_group_list[ap_group -1]
#    except (IndexError, LookupError, ValueError):
#        print("Please enter a valid number.")
#        select_ap_group()
#    while invalid == True:
#        try:
#            response_valid = input("You chose the AP Group name %s, are you sure? (y/N): " % (group_name))
#            if response_valid == "y":
#                return group_name
#                invalid = False
#            elif response_valid == "N":
#                select_ap_group()
#        except:
#            continue


def select_ap_group(ap_group_dict):
    ap_group = input("AP Group? Choose a number: ")
    while ap_group not in ap_group_dict.keys():
        ap_group = input("Invalid number. Please enter a valid number: ")
    group_name = ap_group_dict[ap_group]
    print(group_name)
    while True:
        check_group = input("You selected %s, are you sure? (y/N): " % (group_name))
        if check_group.upper() in "YES":
            invalid = False
            return group_name
        elif check_group.upper() in "NO":
            sys.exit()
        else:
            continue


# Function to print list of CLI commands that change AP name and AP group
def print_cli_commands(ap_group_dict):
    group_name = select_ap_group(ap_group_dict)
    with open(
        "/Users/keithmiller/Work/ib-import-carmichael06062019.csv", mode="r"
    ) as input_file:
        reader = csv.reader(input_file)
        list = []
        print(
            """
        !!! Printing CLI comnmands !!!
        """
        )
        for row in reader:
            list.append(row)
        for row in list[1:]:
            print("ap-rename ap-name %s %s" % (row[2], row[3]))
            print("ap-regroup ap-name %s %s" % (row[3], group_name))


def main():
    # Pull list of ResNET AP Groups from file and create a list
    ap_group_file = open("groups.txt", mode="r")
    lines = ap_group_file.read().splitlines()
    resnet_ap_group_list = []
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        resnet_ap_group_list.append(line)
    print(resnet_ap_group_list)
    ap_group_file.close()

    # Create empty list to give AP Groups a number and set starting number to 1
    ap_group_dict = {}
    count = 1

    # Loop through AP Group list and append/increment number string to group names
    for group in resnet_ap_group_list:
        ap_group_dict[str(count)] = group
        count += 1

    # Print list of numbered AP groups
    for k, v in ap_group_dict.items():
        print("%s. %s" % (k, v))

    print_cli_commands(ap_group_dict)


if __name__ == "__main__":
    main()
