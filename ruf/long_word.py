from collections import Counter
words=["doog", "to", "toe", "toes","house"]
given="tghdoem"

given_dict = Counter(given)

res=[]
max_count=0
for word in words:
    word_dict = Counter(word)
    flag=True
    for i in word_dict:
        if word_dict[i] > given_dict[i]:
            flag=False
            break
    if flag==True:
        if len(word) > max_count:
            res=[word]
            max_count=len(word)
        elif len(word) == max_count:
            res.append(word)
print(res)
