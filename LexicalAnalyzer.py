
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

# In[3]:


import re

type1 = ['if','int','for','while','do','return','break','continue']
type4 = ['+', '-', '*', '/', '=', '>', '<', '>=', '<=', '!=','!']
type5 = [',' , ';' , '{' , '}' , '(' , ')']

tests = """main()                                                                         
{
int  a,b;
a = 10;
           	b = a + 20;
}
"""

def Lexical_Analyzer(s):
    s = s+" "
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



# ## Syntactic Analyzer

# ###  实验二 语法分析—（1）递归下降分析法
# 对下列文法，用递归下降分析法对任意输入的符号串进行分析： 
# 
# （1）E->eBaA
# 
# （2）A->a|bAcB
# 
# （3）B->dEd|aC
# 
# （4）C->e|dC
# 
# 输出的格式如下：
# 
# (1)递归下降分析程序，编制人：姓名，学号，班级
# 
# (2)输入一以#结束的符号串：在此位置输入符号串例如：eadeaa# 
# 
# (3)输出结果：eadeaa#为合法符号串
# 
# 

# In[ ]:


input2 = "eadeaa#"
class Syntactic_Analyzer(object): # 输入一以#结束的符号串
    def __init__(self,s): # s为要分析的字符串
        self.string = s
        self.point = -1 # 此时指针指向的字符串中的字符的位置
        
    def analysis(self):
        if self.ana_E(): return True
        else: return False
    def ana_E(self): # E->eBaA
        if self.next_char(): return False
        if (self.string[self.point] != 'e'):return False
        
        if not self.ana_B():
            return False
        
        if self.next_char(): return False
        if (self.string[self.point] != 'a'):
            return False
        
        if not self.ana_A():
            return False
        
        return True
    
    def ana_A(self): # A->a|bAcB
        if self.next_char(): return False
        if (self.string[self.point] == 'a'): return True
        if (self.string[self.point] != 'b'): return False
        
        if not self.ana_A():return False
        
        if self.next_char(): return False
        if (self.string[self.point] != 'c'): return False
        
        if not self.ana_B():return False
        
        return True
    
    def ana_B(self): # B->dEd|aC
        if self.next_char(): return False
        if (self.string[self.point] == 'd'):
            if not self.ana_E():return False
            if self.next_char(): return False
            if (self.string[self.point] == 'd'):
                return True
        elif (self.string[self.point] == 'a'):
            if not self.ana_C():return False
            else:
                return True
        else:
            return False
        
    def ana_C(self): # C->e|dC
        if self.next_char():return False
        if (self.string[self.point] == 'e'):
            return True
        if (self.string[self.point] != 'd'):
            return False
        if not self.ana_C(): return False
        return True
    
    def next_char(self): # self.point + 1 并判断字符串是否结束
        self.point = self.point + 1
        if self.point == len(self.string):
            return True
        if self.string[self.point] == '#':
            return True
        else:
            return False


# 对下列文法，用LL（1）分析法对任意输入的符号串进行分析：
#（1）E->TG
#（2）G->+TG|-TG
#（3）G->ε
#（4）T->FS
#（5）S->*FS|/FS
#（6）S->ε
#（7）F->(E)
#（8）F->i

import pandas as pd
class LL_1:
    def __init__(self,str):
        self.table = pd.read_csv('./LL1Table.csv',index_col='char')
        #print(self.table)
        #print(self.table.loc['E','('])
        self.rest_input = list(str)
        self.rest_input.append('#')
        self.stack = ['#','E']
        #print(self.rest_input,self.stack)
        self.step = 0 # for info_output
        self.output = pd.DataFrame(columns=['stack','str','generate'])
        self.output.index.name = 'step'
    def run(self):
        continue_flag = 1
        for idx,input_char in enumerate(self.rest_input):
            while continue_flag:
                stack_char = self.stack.pop()
                if stack_char == input_char and stack_char =='#':
                    self.info_output(idx, stack_char, 'finish')
                    break
                if stack_char == input_char:
                    self.info_output(idx, stack_char)
                    break
                if pd.isna(self.table.loc[stack_char,input_char]):
                    self.info_output(idx,stack_char,'error')
                    continue_flag = 0
                    break
                elif self.table.loc[stack_char,input_char] == 'empty':
                    self.info_output(idx,stack_char, self.table.loc[stack_char, input_char])
                    pass
                else:
                    self.info_output(idx,stack_char, self.table.loc[stack_char, input_char])
                    temple = self.table.loc[stack_char,input_char]
                    temple = list(temple)[::-1]
                    for char in temple:self.stack.append(char)
            continue_flag = 1
        #print(self.output)
        return str(self.output)

    def info_output(self,index,stack_char,rightchar=''):
        self.step = self.step + 1
        if rightchar != 'error' and rightchar!='finish' and rightchar!='':
            rightchar = stack_char+'->'+rightchar
        self.output.loc[self.step] = [''.join(self.stack)+stack_char,''.join(self.rest_input[index:]),rightchar]

if __name__=="__main__":
    LLStr = 'i+i'
    L = LL_1(LLStr)
    s =L.run()
    print(s)
    #t=Lexical_Analyzer(tests)
    #print(t)
    #synaticAna = Syntactic_Analyzer(input2)
    #result = synaticAna.analysis()
    #print(result)
    pass

