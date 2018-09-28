import time,os,sys
timer = time.asctime()
print("ACL Generator by CLISoldier")
print("www.linkedin.com/in/jtodd7")
print("www.twitter.com/clisoldier\n")
# DEFINING FILENAME, FILE WILL BE SAVED WHEREEVER PYTHON SCRIPT IS SAVED
filename1 = input("Name Config File: ")
filename2 = filename1 + ".txt"
get_file = open(filename2, "w")
get_file.close()
get_file = open(filename2, "a")
with open(filename2, "a") as f:
  print("ACL Generator by CLISoldier", file=f)
  print("www.linkedin.com/in/jtodd7", file=f)
  print("www.twitter.com/clisoldier", file=f)
  print("Thank You For Using My Code. Copy Paste Configs Below\n", file=f)
get_file.close()
# BEGIN ACL BUILD
aclname = input("ACL Name: ")
acltype = input("Extended or Standard: ")
aclentries = input("Amount of entries for ACL?: ")
# WILL LOOP DEPENDING ON AMOUNT OF ACL ENTRIES
for j in range(int(aclentries)):
  print("New Entry")
  aclaction = input("Permit, Deny, Remark: ")
  # REMARK CONDITION
  if ((acltype == "extended") or (acltype == "standard")) and (aclaction == "remark"):
    remark = input("Enter your remark: ")
    with open(filename2, "a") as f:
      print("ip access-list %s %s %s ########## %s ##########" % (acltype,aclname,aclaction,remark), file=f)
  # EXTENDED ACL CONDITION, MORE OPTIONS THAN STANDARD ACL
  elif (acltype == "extended") and ((aclaction == "permit") or (aclaction == "deny")):
    aclprotocol = input("Define the protocol: ")
    aclsrc = input("Source IP: ")
    aclsrcport = input("Source Port(s): ")
    acldst = input("Destination IP: ")
    acldstport = input("Destination Port(s): ")
    with open(filename2, "a") as f:
      # NO SOURCE PORT + DESTINATION PORT
      if (aclsrcport == "") and (acldstport == str(acldstport)):
        print("ip access-list %s %s %s %s %s %s %s log" % (acltype,aclname,aclaction,aclprotocol,aclsrc,acldst,acldstport), file=f)
      # SOURCE PORT + NO DESTINATION PORT
      elif (aclsrcport == str(aclsrcport)) and (acldstport == ""):
        print("ip access-list %s %s %s %s %s %s %s log" % (acltype,aclname,aclaction,aclprotocol,aclsrc,aclsrcport,acldst), file=f)
      else:
        print("ip access-list %s %s %s %s %s %s %s %s log" % (acltype,aclname,aclaction,aclprotocol,aclsrc,aclsrcport,acldst,acldstport), file=f)
  # STANDARD ACL CONDITION
  elif (acltype == "standard") and ((aclaction == "permit") or (aclaction == "deny")):
    aclsrc = input("Source IP: ")
    with open(filename2, "a") as f:
      print("ip access-list %s %s %s %s log" % (acltype,aclname,aclaction,aclsrc), file=f)
  else:
    print("Invlaid Combination")
# OPEN AND READ THE FILE FOR VERIFICATION
get_file2 = open(filename2, "r")
for i in get_file2:
	print(i.strip()) 
get_file2.close()