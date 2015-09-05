import csv

data = []
with open("3rd grade words.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data.append(row)

#print data

print "<table>"
for row in data:
    print "<tr>"
    for item in [x for x in row if x != ""]:
		print "<td>"
		print """\t<audio src='""" + item + """.mp3' id='"""+ item + """'> """
		print """\t</audio>"""
		print """\t<div id='""" + item + """_text' onClick="document.getElementById('""" + item + """').play();">""" + item + """</div>"""
		print "</td>"
    print "</tr>"
    
print "</table>"
