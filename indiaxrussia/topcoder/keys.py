class EllysKeys:
    def getmax(self, keys):
        if len(keys)==1:
            return 1
        else:
            from collections import defaultdict
            d=defaultdict(list)
            for i in range(len(keys)):
                d[i] = set([i for i, x in enumerate(keys[i]) if x == "^"])
            l=[]
            # print(d)
            for i in range(len(keys)):
                count=[i]
                for j in range(len(keys)):
                    if len(d[i]&d[j])==0:
                        if j not in count: count.append(j)
                l.append(sorted(count))
                # print(l)
            dd=defaultdict(int)
            for i in l:
                dd[tuple(i)]+=1
            # print(dd)
            res=max(dd.values())
            for i in dd:
                if len(i)==len(keys)-1:
                    res+=1
            # print(max(dd.values()))
            return(res)

e=EllysKeys()
# print(e.getmax(["..^.^^.^", "^.^^...^", "^.....^."]))
print(e.getmax(["^..^...^", ".^^.....", ".^..^...", "..^...^.", "...^^.^."]))
# print(e.getmax(["..^.^^.^", "^.^^...^", "^.....^."]))
# print(e.getmax(["....................", "^^^^^^..^^^^..^^^^^.", "..^^...^^..^^.^^..^^", "..^^...^^..^^.^^^^^.", "..^^...^^..^^.^^....", "..^^....^^^^..^^....", "....................", ".^^^^...^^^^..^^^^..", "^^...^.^^..^^.^^..^^", "^^.....^^..^^.^^..^^", "^^...^.^^..^^.^^..^^", ".^^^^...^^^^..^^^^..", "....................", "...^^^^^^...^^^^^...", "...^^.......^^..^^..", "...^^^^^....^^^^^...", "...^^.......^^.^^...", "...^^^^^^...^^..^^..", "...................."]))
