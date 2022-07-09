# %% [markdown]
# P161: Find the longest common string
# %%
import re
# txt1 = input()
# txt2 = input()

txt1 = 'Aux1256'
txt2 = '123456'

max_str = ''
max_len = 0
for i in range(len(txt1)):
    temp_str = ''
    for j in txt1[i:]:
        if re.search(temp_str + j, txt2) != None:
            temp_str = temp_str + j
            print(temp_str)
            pass
        else:
            break
    if len(temp_str) >= max_len:
        max_len = len(temp_str)
        max_str = temp_str
print(max_str)

# %% [markdown]
# P162: Find the longest non-repeating substring
# %%
import re
# txt = input()
txt = 'abcabcccdd'

max_str = ''
max_len = 0
for i in range(len(txt)):
    temp_str = ''
    for j in txt[i:]:
        # print(temp_str)
        if j not in temp_str:
            temp_str += j
            # print(j)
        else:
            break
    if len(temp_str) >= max_len:
        max_str = temp_str
        max_len = len(temp_str)
        # print('max: ', max_str)
print(max_len)
# %% [markdown]
# P163: Print the smallest number by removing N elements from string S
# %%
# N = int(input())
# txt = input()

N = 4
txt = '1234567'
print(txt[:-N])
# %% [markdown]
# P164: Find the common prefix among the N strings
# %%
# N = int(input())
# txt = []
# for i in range(N):
#     txt.append(input())
N = 4 
txt = ['laynhunotcc', 'laynhunoeyqfwnbwl', 'laynhunohknd', 'laynhunowydsnj', 'laynhunopodmvwq', 'laynhunomvveat', 'laynhunodrfharvd', 'laynhunotbrlqcoi', 'laynhunoruonmlz', 'laynhunoifkd', 'laynhunopwdxwu', 'laynhunozilcby', 'laynhunofmcydymql', 'laynhunor', 'laynhunohwemu', 'laynhuno', 'laynhunoate', 'laynhunonfeaj', 'laynhunoye', 'laynhunokgln', 'laynhuno', 'laynhunofszwm', 'laynhunoutvope', 'laynhunokilxopxzz', 'laynhunodmhkzurzb', 'laynhunobxxktqf', 'laynhunohjyrul', 'laynhunokcpjbkn']
prefix_str = ''
for i in range(len(txt[0])):
    # print(i, txt[0][i])
    count = 1
    for j in range(1, len(txt)):
        # print(txt[j])
        try:
            if txt[0][i] == txt[j][i]:
                # print(txt[0][i])
                count += 1
        except:
            pass
    if count == len(txt):
        prefix_str += txt[0][i]
        # print('r->',prefix_str)
    else:
        break
print(prefix_str)

# %%

# %%
