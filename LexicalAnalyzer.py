
# coding: utf-8

# # CompilersPrinciples 
# ## 词法分析器 （课程实验）

# ## 实验要求
# 识别保留字：if、int、for、while、do、return、break、continue； 单词种别码为1。
# 
# 其他的都识别为标识符；                            单词种别码为2。
# 
# 常数为无符号整形数；                             单词种别码为3。
# 
# 运算符包括：+、-、*、/、=、>、<、>=、<=、!=              单词种别码为4。
# 
# 分隔符包括：,、;、{、}、(、)；                       单词种别码为5。
# 

# In[41]:


import re

type1 = ['if','int','for','while','do','return','break','continue']
type4 = ['+', '-', '*', '/', '=', '>', '<', '>=', '<=', '!=','!']
type5 = [',' , ';' , '{' , '}' , '(' , ')']


# In[42]:


tests = """main()                                                                         
{
int  a,b;
a = 10;
           	b = a + 20;
}
"""


# In[43]:


def Lexical_Analyzer(s):
    pattern1 = r'[a-zA-Z]' # 识别字母
    pattern2 = r'[0-9]' # 识别数字
    output = []
    thisword = ''
    lasttype = -1
    thistype = -1
    for char in s:
        if re.match(r'\s',char): # 匹配到空白符
            thistype = 0
            if thistype != lasttype and thisword:
                if thisword in type1:
                    output.append((1,thisword))
                else:
                    output.append((lasttype,thisword))
                thisword = ''
            lasttype = 0
        elif re.match(pattern1,char): # 匹配到字母
            thistype = 2
            if thistype != lasttype and thisword:
                if thisword in type1:
                    output.append((1,thisword))
                else:
                    output.append((lasttype,thisword))
                thisword = ''
            thisword += char
            lasttype = 2     
        elif re.match(pattern2,char): # 匹配到数字
            thistype = 3
            if thistype != lasttype and thisword:
                if thisword in type1:
                    output.append((1,thisword))
                elif lasttype == 1:
                    output.append((2,thisword))
                else:
                    output.append((lasttype,thisword))
                thisword = ''
            thisword += char
            lasttype = 3
        elif char in type4: # 匹配到类型4的字符
            thistype = 4
            if thistype != lasttype and thisword:
                if thisword in type1:
                    output.append((1,thisword))
                elif lasttype == 1:
                    output.append((2,thisword))
                else:
                    output.append((lasttype,thisword))
                thisword = ''
            thisword += char
            lasttype = 4
        elif char in type5: # 匹配到类型5的字符
            thistype = 5
            if thisword:
                if thisword in type1:
                    output.append((1,thisword))
                elif lasttype == 1:
                    output.append((2,thisword))
                else:
                    output.append((lasttype,thisword))
                thisword = ''
            thisword += char
            lasttype = 5
    return output


# In[44]:


if __name__=="__main__":
    t=Lexical_Analyzer(tests)
    print(t)

