import ipaddress
import re
import pprint

SUBNETS = [
'10.21.0.0/24',
'10.21.1.0/24',
'10.21.3.0/24',
'10.21.4.0/24',
'10.21.5.0/24',
'10.21.6.0/24',
]

OUTPUT = open('output-policies.txt', 'w')
errorpolicies = open('errors.txt', 'w')

def expand_range(iprangestr):
    if is_ip_range(iprangestr):
        split = iprangestr.split('-')
        start_ip = split[0]
        iprange = (iprangestr.split('.')[-1]).split('-')
        iprange = list(range(int(iprange[0]),int(iprange[1])+1))
        netobj = ipaddress.IPv4Network(start_ip+'/24', strict=False)
        iprange = ([str(netobj[i]) for i in iprange])
        return iprange

def is_ip_range(teststr):
    return True if '-' in teststr else False

if __name__ == '__main__':
    policiesfile = open('policies-config.txt')
    policiesstr = policiesfile.read()
    pp = pprint.PrettyPrinter(indent=2)
    for i,line in enumerate(policiesstr.splitlines()):
        sources = []
        destinations = []
        flag = False
        error = False
        try:
            srcaddresses = re.findall(r'\|\s*set srcaddr (.+?)\|', line)[0]
            srcaddresses = re.sub('" "', '","', srcaddresses).split(',')
            for j, addr in enumerate(srcaddresses):
                addr = addr.replace('"','')
                srcaddresses[j] = addr
                if is_ip_range(addr):
                    sources += expand_range(unicode(addr))
                else:
                    sources.append(addr)
            dstaddresses = re.findall(r'\|\s*set dstaddr (.+?)\|', line)[0]
            dstaddresses = re.sub('" "', '","', dstaddresses).split(',')
            for j, addr in enumerate(dstaddresses):
                addr = addr.replace('"','')
                dstaddresses[j] = addr
                if is_ip_range(addr):
                    destinations += expand_range(unicode(addr))
                else:
                    destinations.append(addr)
        except:
            print "Ignoring line: %s" % line
            errorpolicies.write(line+'\n')
        sources = list(set(sources))
        destinations =  list(set(destinations))
        for subnet in SUBNETS:
            subnet = unicode(subnet)
            for ip in sources+destinations:
                if '/' in ip:
                    ipnet = unicode(ip)
                elif ip!='':
                    ipnet = unicode(ip+'/32')
                try:
                    c1 = ipaddress.ip_network(ipnet, strict=False).overlaps(ipaddress.IPv4Network(subnet))
                    c2 = ipaddress.ip_network(ipnet, strict=False).prefixlen > ipaddress.IPv4Network(subnet).prefixlen
                except:
                    error = True
                    continue
                if c1 and c2:
                    flag = True
        if error and not flag:
            errorpolicies.write(line+'\n')
        if flag:
            print "Policy is related to Selected Networks: %s ..." % line[0:30]
            OUTPUT.write(line+'\n')
    OUTPUT.close()
    errorpolicies.close()


