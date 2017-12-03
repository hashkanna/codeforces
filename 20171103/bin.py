s=input()
if "1" not in s:
    print("no")
else:
    n=s.index("1")
    print("yes") if s[n+1:].count("0")>=6 else print("no")
