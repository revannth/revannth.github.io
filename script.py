#script.py - Takes image names from a file and replaces them in the source attribute
import pprint
import lxml.html as LH
with open(r'/Users/vedalasrinivas/Desktop/python_automate/index.html',"r") as f:
	html_string = f.read()

root = LH.fromstring(html_string)
with open('ccd_pics/names.txt','r')  as f:
	result = [line.strip() for line in f]
i=0
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(result)
#pprint("%s",result)
pp.pprint(html_string)

for el in root.iter('img'):
    el.attrib['src'] = str(result[i])
    i+=1
with open(r'/Users/vedalasrinivas/Desktop/python_automate/names.txt',"r") as f:
    result1 = [line.strip() for line in f]
i=0
for el in root.iter('h1'):
	el.text = str(result1[i])
	i+=1
print(LH.tostring(root, pretty_print=True))
with open(r'/Users/vedalasrinivas/Desktop/python_automate/index.html',"w") as f:
	f.write(LH.tostring(root,pretty_print=True))
