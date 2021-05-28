from ppadb.client import Client as AdbClient
import time as t

client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("ce0919392d8ea714017e")

device.shell("dumpsys battery unplug")
t.sleep(60)
awake = device.shell("pidof com.snc.trax.service")
if len(awake) == 5:
    print("ATRAX is running")
else:
    print("ATRAX has died\n Please type 'f' in chat to show respect\n")

device.shell("dumpsys battery reset")
t.sleep(60)
awake = device.shell("pidof com.snc.trax.service")
if len(awake) == 5:
    print("ATRAX is running")
else:
    print("ATRAX has died\n Please type 'f' in chat to show respect\n")

doze_info = device.shell("dumpsys deviceidle")
print(doze_info)

device.shell("dumpsys deviceidle enable")
t.sleep(60)
awake = device.shell("pidof com.snc.trax.service")
if len(awake) == 5:
    print("ATRAX is running")
else:
    print("ATRAX has died\n Please type 'f' in chat to show respect\n")

light = device.shell("dumpsys deviceidle get light")
print(light)

deep = device.shell("dumpsys device get deep")
print(deep)

device.shell("dumpsys battery device-idle step light")
t.sleep(60)
awake = device.shell("pidof com.snc.trax.service")
if len(awake) == 5:
    print("ATRAX is running")
else:
    print("ATRAX has died\n Please type 'f' in chat to show respect\n")

device.shell("dumpsys battery deviceidle force-idle")
t.sleep(60)
awake = device.shell("pidof com.snc.trax.service")
if len(awake) == 5:
    print("ATRAX is running")
else:
    print("ATRAX has died\n Please type 'f' in chat to show respect\n")