import bluesky_cli

conn = bluesky_cli.blueskyconn("172.16.4.147:8189", "guest", "guest")
deviceList = conn.list_ed()
for device in deviceList:
    deviceIP = "0.0.0.0"
    connStatus = "offline"
    for key in device.keys():
        if key == "EDIP":
            deviceIP = device[key]
        if key == "connStatus":
            connStatus = device[key]
    if connStatus == "online":
#        deviceIP = "172.16.4.103"
        y = conn.getSensorDatByAdc(deviceIP, "mcp3208")
        print "{} {}".format(deviceIP, y)
#        print y
        y = conn.getSensorDatByAdcChannel(deviceIP, "mcp3208", "0")
        print y
