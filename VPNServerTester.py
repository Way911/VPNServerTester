'''
Created on 2015-7-20

@author: Wayne Cao
'''

import subprocess
import re

if __name__ == '__main__':
    serverHosts = { "p1.jp1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.jp1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.jp2.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.jp2.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.jp3.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.jp3.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.us1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.us1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.us2.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.us2.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.us3.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.us3.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.us4.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.us4.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.us5.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.us5.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.sg1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.sg1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.sg2.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.sg2.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.hk1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.hk1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.hk2.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.hk2.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.tw1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.tw1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p1.uk1.towersee.com":{'loss':100, 'avgTime':5000},
                    "p2.uk1.towersee.com":{'loss':100, 'avgTime':5000}}
    
    
    
    processDict = {}
    for host in serverHosts.keys():
        processDict[host] = subprocess.Popen('ping -c 10 ' + host,stdout=subprocess.PIPE, shell=True)
    
    for host in processDict.keys():
        (stdoutdata, stderrdata) = processDict[host].communicate()
        if stderrdata or 'cannot resolve' in stdoutdata:
            serverHosts.pop(host)
            print stderrdata
            continue
        print stdoutdata
        loss = re.findall(r"\d{1,3}.\d{1}[%]", stdoutdata)[0].replace('%','')
        if loss == "100.0":
            serverHosts.pop(host)
            continue
        avgTime = stdoutdata.split('/')[-3]
        serverHosts[host]['loss'] = float(loss)
        serverHosts[host]['avgTime'] = float(avgTime)
       
    servers = sorted(serverHosts.items(), lambda x, y: cmp(x[1]['avgTime'], y[1]['avgTime']), reverse = False)
    servers = servers[0:4]
    servers = sorted(servers, lambda x, y: cmp(x[1]['loss'], y[1]['loss']), reverse = False)
    print servers
