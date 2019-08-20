function getValue(str) {
	var num = 0;
	switch (str) {
		case 'I':
			num = 1;
			break;
		case 'V':
			num = 5;
			break;
		case 'X':
			num = 10;
			break;
		case 'L':
			num = 50;
			break;
		case 'C':
			num = 100;
			break;
		case 'D':
			num = 500;
			break;
		case 'M':
			num = 1000;
			break;
		default:
			num = 0;
	}
	return num;
}

function convertRomanNumeral(str) {
	str = str.toUpperCase();

	var num = 0;
	for (var i = 0; i < str.length; i++) {
		num1 = getValue(str[i]);
		num2 = getValue(str[i + 1]);
		num3 = getValue(str[i + 2]);
		if (num1 == 0 || num2 == 0) {
			break;
		} else if (num1 < num2 && !isNaN(num2)) {
			num += num2 - num1;
		} else {
			if (num2 > num3) {
				num += num1;
			}
		}
	}
	return num;
}

console.log(convertRomanNumeral('IM'));
