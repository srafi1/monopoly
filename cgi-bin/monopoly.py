#! /usr/bin/python
import cgi,cgitb
cgitb.enable()
form = cgi.FieldStorage()

print "Content-type: text/html\n\n"

def main() :
	if len(form) == 8:
		print '<html><head><title>Nah man</title></head><body><h1>No players, no game</h1></body></html>'
		return
	print '''
	<html><head>
	<title>Monopoly</title>
	<script type=text/javascript src=../monopoly.js></script>
	<style type=text/css>
	body {
	font-family: Arial;
	}
	td, button {
	font-size:24;
	border:4px solid black;
	text-align:center;
	}
	</style>
	</head><body onload=setup('''+ str(len(form)-8) +''')>
	<center>
	<h1>All da munnies</h1><br>
	<table style="border-collapse:collapse;width:80%"><tr>
	'''
	
	p = []
	for i in form:
		if len(i) < 3:
			p.append(form[i].value)
	players = len(p)
	if players > 4:
		for i in range(4):
			print '<td id=',i,'>'+ p[i] +':<br>$1500<br><button onclick=pay(',i,')>Pay</button></td>'
		print '</tr><tr><td colspan=4><center><table style="border-collapse:collapse;width:100%"><tr>'
		for i in range(players - 4):
			print '<td id=',i+4,'>'+ p[i+4] +':<br>$1500<br><button onclick=pay(',i+4,')>Pay</button></td>'
		print '</tr></table></center></td></tr>'
	else:
		for i in range(players):
			print '<td id=',i,'>'+ p[i] +':<br>$1500<br><button onclick=pay(',i,')>Pay</button></td>'
		print '</tr>'
	print '</table><br><table style="border-collapse:collapse;width:50%"><tr><td id=-1 style="text-align:center">BANK:<br>$999999<br><button onclick=pay(-1)>Pay</button></td></tr></table>'
	
	for i in range(players):
		print '<p id=p'+str(i),'hidden>'+ p[i] +';'+ form['pi'+str(i+1)].value +'</p>'
	
	print "</center></body></html>"

main()