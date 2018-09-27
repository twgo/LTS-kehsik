import re
piau = re.compile('[<>*]')


def tiau(ku):
    hua_guan, tai_guan = ku.split('/', 1)
    hua = piau.sub('', hua_guan)
    return '{}/{}'.format(hua, tai_guan)
