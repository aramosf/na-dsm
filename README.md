# Netgear Arlo Recordings downloader
# Tested on my Synology DSM 6

### Usage
Just run with your user/password and path.

```sh
ninjabox: aramosf$ python na-dsm.py
Netgear Arlo downloader
Usage: na-dsm.py <username> <password> <directory>
example: na-dsm.py aramosf@unsec.net Zurrupia1 /volume2/share2/

ninjabox: aramosf$ python na-dsm.py  aramosf@gmail.com Zurrupia1 /backup
Downloading https://arlos3-prod-z1.s3.amazonaws.com/082cac22_42c7_4711_93ac_8ff40b7e5f98/309-2373450/48B45BS932699/recordings/1484053598636.mp4?AWSAccessKeyId=Blah&Expires=1484157433&Signature=Blah2%2BTMgLeRfCpRCORek%3D to: /backup/2017/01/20170110_14h06m38s.mp4
Downloading https://arlos3-prod-z1.s3.amazonaws.com/082cac22_42c7_4711_93ac_8ff40b7e5f98/309-2373450/48B254733214B/recordings/1484053595835.mp4?AWSAccessKeyId=Blah&Expires=1484157433&Signature=Blah2%2BI%3D to: /backup/2017/01/20170110_14h06m35s.mp4
Downloading https://arlos3-prod-z1.s3.amazonaws.com/082cac22_42c7_4711_93ac_8ff40b7e5f98/309-2373450/48B254733214B/recordings/1484052716173.mp4?AWSAccessKeyId=Blah&Expires=1484157433&Signature=%2FBlah2%2BX6zIdEw%3D to: /backup/2017/01/20170110_13h51m56s.mp4
Downloading https://arlos3-prod-z1.s3.amazonaws.com/082cac22_42c7_4711_93ac_8ff40b7e5f98/309-2373450/48B254733214B/recordings/1484047045282.mp4?AWSAccessKeyId=Blah&Expires=1484157433&Signature=Blah2%3D to: /backup/2017/01/20170110_12h17m25s.mp4
```

