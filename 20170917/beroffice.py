import sys

def typo(s):
    vowels = ['a','e','i','o','u']
    if len(s) <=2:
        return s
    for i in range(2,len(s)):
        if s[i] in vowels or s[i-1] in vowels or s[i-2] in vowels:
            pass
        elif s[i] == s[i-1] == s[i-2]:
            pass
        else:
            return s[:i] + ' ' + typo(s[i:])
    return s

def main():
    s='backtothefutttture'
    #s=sys.stdin.readline().strip()
    print(typo(s))

if __name__ == '__main__':
    main()
