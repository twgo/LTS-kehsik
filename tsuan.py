import re
import html

piau = re.compile('[<>*]')
kak = re.compile('[a-z]+[0-9]\<([a-z]+[0-9])\>')
tsenn = re.compile('[a-z]+[0-9]\*([a-z]+[0-9]-?)\*')
tsenn_khang = re.compile('[a-z]+[0-9]\*( +)\*')


def tiau(ku):
    try:
        hua_guan, tai_guan = ku.split('/', 1)
    except ValueError:
        hua_guan, tai_guan = '', ku
    hua = piau.sub('', hua_guan)
    tai = kak.sub(lambda m: m.group(1), tai_guan)
    tai = tsenn.sub(lambda m: m.group(1).rstrip('-'), tai)
    tai = tsenn_khang.sub(lambda m: m.group(1), tai)

    tai = piau.sub('', tai).replace(' -', '').replace('-,', ',')
    return '{}/{}'.format(hua, tai)


def _main():
    with open('LTS-003.trs') as jip:
        with open('LTS-003-hong.trs', 'w') as tshut:
            for tsua in jip:
                if '<' in tsua:
                    print(tsua.rstrip(), file=tshut)
                elif tsua.rstrip() == '':
                    print(file=tshut)
                else:
                    print(
                        html.escape(
                            tiau(html.unescape(tsua.rstrip()))),
                        file=tshut
                    )


if __name__ == '__main__':
    _main()
