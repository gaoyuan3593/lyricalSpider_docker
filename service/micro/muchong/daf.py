s = "helas"
s1 = ""
for c in s:
    st = c.encode("gb2312").hex()
    a, b = st[:2], st[2:]
    s1 += "%{}%{}".format(a.upper(), b.upper())
print(s1)