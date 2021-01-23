input_text = '''77
58
25
92
14
154
105
112
147
63
84
109
24
129
49
102
130
128
134
88
95
70
80
4
153
17
145
122
39
117
93
65
3
2
139
101
148
37
27
1
87
64
23
59
42
146
43
151
116
46
115
118
131
94
19
33
12
107
10
7
73
78
53
11
135
79
60
32
141
31
140
98
136
72
38
152
30
74
106
50
13
26
155
67
20
66
91
56
34
125
52
51
18
108
57
81
119
71
144'''

number_list = [int(n) for n in input_text.split('\n')]
from collections import defaultdict
diff_dict = defaultdict(int)
# add nearest socket
number_list.append(0)
# add adaptor rating
number_list.append(max(number_list)+3)
sorted_list = sorted(number_list)

for i in range(1, len(number_list)):
    diff_dict[sorted_list[i] - sorted_list[i-1]] += 1

# Part 1
print(diff_dict[1] * diff_dict[3])

# Part 2
tracker = defaultdict(int)  # index = jolt, value = num of ways from start to this jolt
tracker[0] = 1
for jolt in sorted_list:
    tracker[jolt] += tracker[jolt-1] + tracker[jolt-2] + tracker[jolt-3]
print(tracker[sorted_list[-1]])