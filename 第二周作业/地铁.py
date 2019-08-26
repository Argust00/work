# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:03:02 2019

@author: Argust
"""

import requests 
import re

def getHTMLNum(url):
    try:
        headers = {"User-Agent" : "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        demo=r.text        
        return demo
    except:
        return ""

def getHTMLNam(url):
    try:
        headers = {"User-Agent" : "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        demo=r.text        
        return demo
    except:
        return ""
    
    



url='https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81/408485?fr=aladdin'
response=getHTMLNum(url)
pattern=re.compile(r'<td width="204" align="center" valign="middle" colspan="1" rowspan="2"><a target=_blank href="(\S+)"( data-lemmaid="897830")*>(\w+)</a>([（）\w]*)</td><td width="203" align="center" valign="middle"')
lt=re.findall(pattern,response)
# =============================================================================


lt1=[]
subname=[]
subname1=[]
sub=[]
ls='https://baike.baidu.com'
for i in lt:
    ls1=ls+str(i[0])
    
    lt1.append(ls1)
    subname.append(i[2])
    subname1.append(i[3])
for i in range(len(subname)):
    sub.append(str(subname[i])+str(subname1[i]))

lt2=re.findall('<tr><td align="center" valign="middle" colspan="1" rowspan="1">(\w+)</td>',getHTMLNam(str(lt1[0])))
for i in range(len(lt2)):
    lt2[i]="北京地铁"+lt2[i]+"站"

lt3=re.findall('<tr><th>(\w+)</th><td width="72" align="middle" valign="center">',getHTMLNam(str(lt1[1])))     
lt3.pop(0)
for i in range(len(lt3)):
    lt3[i]="北京地铁"+lt3[i]+"站"

lt4=re.findall('<tr><td align="center" valign="middle" colspan="1" rowspan="1">(\w+)</td><td align="center" valign="middle"',getHTMLNam(str(lt1[2])))
lt4[:24]=[]
for i in range(len(lt4)):
    lt4[i]="北京地铁"+lt4[i]+"站"

lt5=re.findall('<tr><td align="center" valign="middle"><div class="para" label-module="para">(\w+)</div>',getHTMLNam(str(lt1[3])))
for i in range(len(lt5)):
    lt5[i]="北京地铁"+lt5[i]+"站"

lt6=re.findall('<tr><th>(\w+)</th><td>',getHTMLNam(str(lt1[4])))
for i in range(len(lt6)):
    lt6[i]="北京地铁"+lt6[i]+"站"

lt7=re.findall('<tr><th>(\w+)</th><td width="110" align="center" valign="middle"',getHTMLNam(str(lt1[5])))
lt7.pop(0)
for i in range(len(lt7)):
    lt7[i]="北京地铁"+lt7[i]+"站"

lt8_1=re.findall('<tr><th width="11.">(\w+)</th>',getHTMLNam(str(lt1[6])))
lt8_1.pop(0)
lt8_2=re.findall('<tr><th width="120">(\w+)</th>',getHTMLNam(str(lt1[7])))
lt8=lt8_1+lt8_2
for i in range(len(lt8)):
    lt8[i]="北京地铁"+lt8[i]+"站"

lt9=re.findall('<tr><th>(\w+)</th>',getHTMLNam(str(lt1[8])))
for i in range(len(lt9)):
    lt9[i]="北京地铁"+lt9[i]+"站"

lt10=re.findall('<tr><td width="57" align="middle" valign="center">(\w+)</td>',getHTMLNam(str(lt1[9])))
for i in range(len(lt10)):
    lt10[i]="北京地铁"+lt10[i]+"站"

lt11=re.findall('<tr><th align="center" valign="middle">(\w+)</th><td width="72" align="center" valign="middle">',getHTMLNam(str(lt1[10])))
for i in range(len(lt11)):
    lt11[i]="北京地铁"+lt11[i]+"站"

lt12_1=re.findall('<tr><th align="center" valign="middle">(\w+)</th><td width="88" align="center" valign="middle">',getHTMLNam(str(lt1[11])))
lt12_1.pop(0)
lt12_2=re.findall('<tr><th align="center" valign="middle">(\w+)</th><td width="110" align="center" valign="middle">',getHTMLNam(str(lt1[12])))
lt12=lt12_1+lt12_2
for i in range(len(lt12)):
    lt12[i]="北京地铁"+lt12[i]+"站"

lt13=re.findall('<tr><th align="center" valign="middle">(\w+)</th><td width="88" align="center" valign="middle">',getHTMLNam(str(lt1[13])))
lt13.pop(0)
for i in range(len(lt13)):
    lt13[i]="北京地铁"+lt13[i]+"站"

lt14=re.findall('<tr><th>(\w+)</th><td ',getHTMLNam(str(lt1[14])))
for i in range(len(lt14)):
    lt14[i]="北京地铁"+lt14[i]+"站"

lt15=re.findall('<tr><th align="center" valign="middle">(\w+)</th><td width="110" align="center" valign="middle">',getHTMLNam(str(lt1[15])))
for i in range(len(lt15)):
    lt15[i]="北京地铁"+lt15[i]+"站"

lt16=re.findall('<tr><th width="98">(\w+)</th><td width="139" align="center" valign="middle">',getHTMLNam(str(lt1[16])))
for i in range(len(lt16)):
    lt16[i]="北京地铁"+lt16[i]+"站"

lt17=re.findall('" data-lemmaid="\d+">(\w+)</a>[\s(</div>)]*</td><td width="130" align="center" valign="middle" colspan="1" rowspan="1">',getHTMLNam(str(lt1[17])))
for i in range(len(lt17)):
    lt17[i]="北京地铁"+lt17[i]
    
lt18=re.findall('</td></tr><tr><th align="center" valign="middle">(\w+)</th><td width="110" align="center" valign="middle">',getHTMLNam(str(lt1[18])))
for i in range(len(lt18)):
    lt18[i]="北京地铁"+lt18[i]+"站"

lt19=re.findall('<tr><td width="130" align="center" valign="top">(\w+)</td>',getHTMLNam(str(lt1[19])))
for i in range(len(lt19)):
    lt19[i]="北京地铁"+lt19[i]
    
lt20=re.findall('<tr><th( width="184")?>(\w+)</th><td width="109"',getHTMLNam(str(lt1[20])))

for i in range(len(lt20)):
    lt20[i]=lt20[i][1]
for i in range(len(lt20)):
    lt20[i]="北京地铁"+lt20[i]+"站"

sub[6]="北京地铁8号线"
sub.pop(7)
sub[10]="北京地铁14号线"
sub.pop(11)
lb1=[lt2,lt3,lt4,lt5,lt6,lt7,lt8,lt9,lt10,lt11,lt12,lt13,lt14,lt15,lt16,lt17,lt18,lt19,lt20]
subway_line={}
for i in range(len(sub)):
    subway_line[sub[i]]=lb1[i]
























