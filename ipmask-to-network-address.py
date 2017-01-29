import ipaddress

networkliststr = """
172.20.223.253/24
172.20.225.243/24
172.20.225.244/24
172.21.15.11/24
172.22.104.13/30
172.22.104.45/30
172.22.136.9/30
172.22.17.61/30
172.22.22.49/30
172.22.24.169/30
172.22.24.229/30
172.22.24.237/30
172.22.24.85/30
172.22.24.89/30
172.22.40.113/30
172.22.40.41/30
172.22.56.77/30
172.22.8.109/30
172.22.8.209/30
172.22.88.21/30
172.22.93.121/30
172.22.93.129/30
172.22.93.33/30
172.22.97.89/30
172.24.104.21/30
172.24.108.153/30
172.24.108.157/30
172.24.108.169/30
172.24.108.89/30
172.24.24.101/30
172.24.24.105/30
172.24.24.129/30
172.24.24.141/30
172.24.24.69/30
172.24.24.73/30
172.24.24.81/30
172.24.24.85/30
172.24.24.97/30
172.24.40.129/30
172.24.40.221/30
172.24.40.65/30
172.24.40.81/30
172.24.42.161/30
172.24.56.237/30
172.24.56.53/30
172.24.72.253/30
172.24.72.49/30
172.24.72.5/30
172.24.8.105/30
172.24.88.21/30
172.26.104.13/30
172.26.120.5/30
172.26.120.61/30
172.26.136.117/30
172.26.136.21/30
172.26.136.41/30
172.26.136.5/30
172.26.136.93/30
172.26.152.117/30
172.26.152.41/30
172.26.24.101/30
172.26.24.49/30
172.26.40.253/30
172.26.40.37/30
172.26.40.77/30
172.26.40.81/30
172.26.40.85/30
172.26.40.89/30
172.26.48.213/30
172.26.48.45/30
172.26.48.57/30
172.26.56.101/30
172.26.56.105/30
172.26.56.13/30
172.26.56.29/30
172.26.56.45/30
172.26.56.65/30
172.26.72.233/30
172.26.72.241/30
172.26.72.245/30
172.26.72.41/30
172.26.72.61/30
172.26.8.69/30
172.26.82.149/30
172.26.88.17/30
172.26.88.5/30
172.28.18.117/30
172.28.18.121/30
172.28.18.61/30
172.28.18.89/30
172.28.18.9/30
172.28.24.173/30
172.28.24.181/30
172.28.24.197/30
172.28.24.205/30
172.28.24.221/30
172.28.24.229/30
172.28.24.245/30
172.28.24.73/30
172.28.24.81/30
172.28.28.245/30
172.28.40.125/30
172.28.40.225/30
172.28.56.109/30
172.28.56.177/30
172.28.56.185/30
172.28.56.201/30
172.28.59.69/30
172.28.72.137/30
172.28.72.185/30
172.28.72.5/30
172.28.72.73/30
172.28.8.221/30
172.28.8.73/30
172.28.8.85/30
172.28.88.189/30
172.28.88.197/30
172.28.93.185/30
172.28.93.33/30
172.30.104.77/30
172.30.108.250/24
172.30.120.249/30
172.30.120.61/30
172.30.131.17/30
172.30.136.177/30
172.30.136.5/30
172.30.15.133/30
172.30.152.13/30
172.30.152.69/30
172.30.152.93/30
172.30.168.165/30
172.30.168.17/30
172.30.168.173/30
172.30.168.21/30
172.30.168.49/30
172.30.168.5/30
172.30.216.13/30
172.30.216.253/30
172.30.24.13/30
172.30.24.197/30
172.30.24.5/30
172.30.33.73/30
172.30.40.129/30
172.30.40.26/30
172.30.40.49/30
172.30.40.73/30
172.30.47.109/30
172.30.56.177/30
172.30.56.45/30
172.30.56.53/30
172.30.56.61/30
172.30.56.81/30
172.30.56.93/30
172.30.72.41/30
172.30.72.5/30
172.30.72.53/30
172.30.72.57/30
172.30.72.65/30
172.30.72.73/30
172.30.77.245/30
172.30.79.97/30
172.30.8.169/30
172.30.8.173/30
172.30.8.233/30
172.30.88.105/30
172.30.88.5/30
172.30.88.93/30
172.30.94.73/30
"""

networklist = networkliststr.splitlines()
ofile = open('tsnets.txt', 'w')
for ipmask in networklist:
    ipmask = unicode(ipmask)
    if ipmask != u'':
        print ipmask
        net = ipaddress.ip_network(ipmask, strict=False)
        firstip = list(net)[1].__str__()
        lastip = list(net)[-2].__str__()
        ofile.write('%s\t%s\t%s\n' % (net, firstip, lastip))