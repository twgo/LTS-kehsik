import re
piau = re.compile('[<>*]')
kak=re.compile('[a-z]+[0-9]\<([a-z]+[0-9])\>')

def tiau(ku):
    hua_guan, tai_guan = ku.split('/', 1)
    hua = piau.sub('', hua_guan)
    tai=kak.sub(lambda m:m.group(1),tai_guan)
    tai=piau.sub('',tai)
    return '{}/{}'.format(hua, tai)
