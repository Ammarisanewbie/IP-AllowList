#Open the allow_list.txt
with open("Mod 4\\allow_list.txt", "r") as file:
    allowIP = file.read()

#Open the remove list
with open ("Mod 4\\remove_list.txt","r") as file:
    removeIP = file.read()


#Converting allow_list(str) to list
allow_list = allowIP.split()
# print("Before check", allow_list)

#Converting remove_list(str) to list
remove_list = removeIP.split()

#Code to iterate through allow_list
for ip in remove_list:
    #check if ip is in remove_list, remove if yes
    if ip in allow_list:
        allow_list.remove(ip)

#Updating the txt file: allow_list.txt with revised list of IPs
#First we need to convert the list to a string, on newlines for better readability
updated_allow_list="\n".join(allow_list)

#Update file with revised list of IPs
with open ("Mod 4\\allow_list.txt","w") as file:
    file.write(updated_allow_list)