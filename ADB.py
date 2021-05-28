from ppadb.client import Client as AdbClient


client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("ce0919392d8ea714017e")


def dump_logcat(connection, line_counter=30):
    while True:
        data = connection.read(1024)
        line = data.decode('utf-8')
        logcat = open("logcat.txt", "a+")
        logcat.write(line + "\n\n")
        line_counter -= 1
        if line_counter == 0:
            wholethang = logcat.readlines()
            if wholethang.find("Application is not responding") != True:
                logcat.close()
                logcat = open("logcat.txt", "w")
                logcat.write()
            else:
                break
        if not data:
            break
        print(data.decode('utf-8'))

device.shell("logcat", handler=dump_logcat)
print(device.is_installed("com.snc.trax"))
