function parensValid(str) {
	var open = 0,
		close = 0;
	for (var i = 0; i < str.length; i++) {
		if (str[i] == '(') {
			open++;
		}
		if (str[i] == ')' && open !== close) {
			close++;
		}
	}
	if (open == close) {
		return true;
	} else {
		return false;
	}
}

console.log(parensValid('Y(3(p)p(3)r)s'));
console.log(parensValid('N(0(p)3'));
console.log(parensValid('N(0)t ))0(k'));

function braceValid(str) {
	var open1 = 0,
		open2 = 0,
		open3 = 0,
		close1 = 0,
		close2 = 0,
		close3 = 0;

	for (var i = 0; i < str.length; i++) {
		switch (str[i]) {
			case '(':
				open1++;
				break;
			case '[':
				open2++;
				break;
			case '{':
				open3++;
				break;
			case ')':
				if (open1 > close1) {
					close1++;
				}
				break;
			case ']':
				if (open2 > close2) {
					close2++;
				}
				break;
			case '}':
				if (open3 > close3) {
					close3++;
				}
				break;
			default:
				break;
		}
	}
	if (open1 == close1 && open2 == close2 && open3 == close3) {
		return true;
	} else {
		return false;
	}
}

console.log(braceValid('W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!'));
console.log(braceValid('D(i{a}l[ t]o)n{e'));
console.log(braceValid('A(1)s[O (n]0{t) 0}k'));
