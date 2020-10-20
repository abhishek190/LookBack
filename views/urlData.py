import sys
import requests
import bs4
res=requests.get(sys.argv[1])
soup=bs4.BeautifulSoup(res.text,'html.parser')
h1=soup.select('div .problemindexholder .problem-statement .header .title')
h2=soup.select('div .problemindexholder .problem-statement .header .time-limit')
h3=soup.select('div .problemindexholder .problem-statement .header .memory-limit')
h4=soup.select('div .problemindexholder .problem-statement .header .input-file')
h5=soup.select('div .problemindexholder .problem-statement .header .output-file')
h6=soup.select('div .problemindexholder .problem-statement div')
h7=soup.select('div .problemindexholder .problem-statement .sample-test .input  ')
h8=soup.select('div .problemindexholder .problem-statement .sample-test .output ')

problemStatment=h6[10].getText()
InputStatment=h6[11].getText()
OutputStatment=h6[13].getText()
SampleTestInput=h7
SampleTestOutput=h8
# InputStatment=InputStatment.replace("$$$","").replace("\\rightarrow","->").replace(".",".\n").replace(":",":\n").replace(";",";\n").replace('\\le',"<=").replace('\\cdot',".").replace('\\text{',"").replace('OR }',"OR")
# OutputStatment=OutputStatment.replace("$$$","").replace("\\rightarrow","->").replace(".",".\n").replace(":",":\n").replace(";",";\n").replace('\\le',"<=").replace('\\cdot',".").replace('\\text{',"").replace('OR }',"OR")
# SampleTest=SampleTest.replace("$$$","").replace("\\rightarrow","->").replace(".",".\n").replace(":",":\n").replace(";",";\n").replace('\\le',"<=").replace('\\cdot',".").replace('\\text{',"").replace('OR }',"OR")
print(h1[0].getText())
print(h2[0].getText())
print(h3[0].getText())
print(h4[0].getText())
print(h5[0].getText())
print(problemStatment)
print(InputStatment)
print(OutputStatment)
print(SampleTestInput)
print(SampleTestOutput)
