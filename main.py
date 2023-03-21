import os
def myping(host):
    response = os.system("ping -n 1 " + host)

    if response == 0:
        return True
    else:
        return False


print(myping("34.212.34.156"))