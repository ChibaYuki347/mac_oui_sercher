# -*- coding: utf-8 -*-

maclist=[
        # 'fa:16:3e:ad:ba:a0',
        # 'fa:16:3e:ac:b2:e0',
        # 'fa:16:3e:83:80:be',
        'fa16.3ef9.8d1e',
        # 'fa16.3ef9.8d1e',
        # '0016.3e2a.3302',
        # '0016-3e10-102e',
        # '0016-3ed9-075d',
        ]

pat = str.maketrans({
    '-': '',
    ':': '',
    '.': '',
})


for dirtymac in maclist:
    clsmac = dirtymac.translate(pat) # '0016-3e10-102e' -> '00163e10102e'
    colmac = ':'.join(a + b for a, b in zip(clsmac[::2], clsmac[1::2])) # '00163e10102e' -> '00 16 3e 10 10 2e' -> '00:16:3e:10:10:2e'
    print("colmac : ",colmac)

test_mac = 'fa163ef98d1e'

print(test_mac)
print(test_mac[::2])
print(test_mac[1::2])


test_mac2 = ':'.join(a + b for a, b in zip(test_mac[::2], test_mac[1::2]))
print(test_mac2)