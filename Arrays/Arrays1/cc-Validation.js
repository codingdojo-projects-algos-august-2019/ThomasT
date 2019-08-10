function isCreditCardValid(digitArr) {
	var lastNum = digitArr[digitArr.length - 1];
	var sum = 0;
	digitArr.length--;
	for (var i = 0; i < digitArr.length; i++) {
		if (i % 2 != 0) {
			digitArr[i] *= 2;
		}
		if (digitArr[i] > 9) {
			digitArr[i] -= 9;
		}
	}
	for (var i = 0; i < digitArr.length; i++) {
		sum += digitArr[i];
	}
	sum += lastNum;
	if (sum % 10 == 0) {
		return true;
	} else {
		return false;
	}
}
console.log(isCreditCardValid([5, 1, 8, 7, 2, 6, 3, 5, 8, 1]));
