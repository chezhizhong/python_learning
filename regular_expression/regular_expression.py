"""
本脚本将整理正则表达式的相关内容
"""

"""
预定于字符 \d \s \w \D \S \W
\d  匹配所有的数字  0-9
\D  匹配所有的非数字  ^\d
\w  包含下划线字符 a-zA-Z0-9_
\W  代表非正常字符  特殊字符
\s  空白字符  制表符  换行符
\S  非\s
.  代表换行符外的一切字符
^ 取反   \D  ==  ^\d  如果以该字符开头表示以后面的字符开头
- 代表区间   a-d == abcd
元字符 []  匹配一个字符，括号内的字符是或者的关系
() 代表分组
重复匹配
{n} 表示前面的字符重复n次
{n, m} 表示前面的字符至少出现n次，最多出现m次  贪婪匹配
{n, m}? 表示前面的字符至少出现n次，最多出现m次  非贪婪匹配
{n,}  表示前面的字符出现n次到任意次
? 表示前面的字符出现0次或1次 {0,1}  会出现空字符
+ 表示前面的字符至少1次 {1,}
* 表示前面的字符出现0次或任意次
转义符  \* == *
反向引用
位置引用
"""

import re
result = re.findall(r'd\w+d', 'dxxxxxxxdxxxxxxxxxxxxxd')
print(result)
result = re.findall(r'd\w+?d', 'dxxxxxxxdxxxxxxxxxxxxxd')
print(result)
html_str = """
<td>python</td><td>$123</td><td>1231234@qq.com</td>
"""
result = re.findall(r'<td>.+</td>', html_str)
print(result)
result = re.findall(r'<td>.+?</td>', html_str)
print(result)
result = re.findall(r'<td>(.+?)</td>', html_str)
print(result)

word_str = """
'hello'  "python"  'love" "nana'
"""
result = re.findall(r"('|\")(\w+)(\1)", word_str)  # \1表示和最前面的字符一样
print(result)
result = re.findall(r"(\d)(\1{2,})", "111222")
print(result)


result = re.findall(r"^\d{11}", "12345678900")
print(result)
result = re.findall(r"^\d{11}$", "12345678900")
print(result)
result = re.findall(r"^\d{11}$", "12345678900dd")
print(result)
