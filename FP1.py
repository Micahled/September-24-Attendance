import random # imports random module
varUserName = input("What is your name? ")
print ("\nHello, " +varUserName+". Welcome to the Lucky Number Generator!")
print ("Lets generate your six lucky numbers...")

print ("Here are your numbers:")
# print random numbers here
################################################
varPB1 = random.randint(1,69)
varPB2 = random.randint(1,69)
varPB3 = random.randint(1,69)
varPB4 = random.randint(1,69)
varPB5 = random.randint(1,69)
varPB6 = random.randint(1,69)
################################################

print (str(varPB1) + "  " + str(varPB2) + "  " + str(varPB3) + "  " + str(varPB4) + "  " + str(varPB5) + "    " + str(varPB6))

print ("\nGood luck, " + varUserName + ". Have a wonderful day.")