var players = [];
var tformat = 'name:<br>$money<br><img src=../img/image.png width=80><br><button onclick=btnfxn(index)>btnfxn</button>';
var payer = '';
var paid = '';

function setup(n) {
	for (var i = 0; i < n; i++) {
		var p = document.getElementById('p'+i).innerHTML;
		var semind = p.search(';');
		players[i] = {
			name: p.substring(0,semind),
			money: 1500,
			img: p.substring(semind+1, p.length)
		}
	}
	render('pay');
}

function render(newbtn) {
	for (var i = 0; i < players.length; i++) {
		var rep = tformat.replace('name', players[i].name).replace('index', i).replace('money', players[i].money).replace('btnfxn',newbtn).replace('btnfxn',newbtn).replace('image', players[i].img);
		document.getElementById(i).innerHTML = rep;
	}
	var rep = tformat.replace('name', 'BANK').replace('index', -1).replace('$money', 'ALL DA MUNNIES').replace('btnfxn',newbtn).replace('btnfxn',newbtn).replace('image', 'monopoly');
	document.getElementById(-1).innerHTML = rep;
}

function pay(player) {
	payer = player;
	render('receive');
}

function receive(player) {
	paid = player;
	var amt = parseInt('0' + prompt('How much money?'));
	if (payer == -1 || paid == -1) {
		if (paid == -1 && payer == -1) {
			render('pay');
			return;
		} else if (payer != -1) players[payer].money -= amt; 
		else if (paid != -1) players[paid].money += amt;
	} else {
		alert(players[payer].name + ' paid ' + players[paid].name + ' $' + amt);
		players[payer].money -= amt;
		players[paid].money += amt;
	}
	render('pay');
}