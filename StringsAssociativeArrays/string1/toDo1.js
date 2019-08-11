function removeAt(arr, position) {
	var value = arr[position];
	for (var i = position; i < arr.length; i++) {
		arr[i] = arr[i + 1];
	}
	arr.length--;
	return value;
}

function removeBlanks(str) {
	var arr = str.split('');
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] == ' ') {
			removeAt(arr, i);
		}
	}
	return arr.join('');
}

console.log(removeBlanks(' Pl ayTha tF u nkyM usi c '));

function getDigits(str) {
	var arr = [];
	for (var i = 0; i < str.length; i++) {
		var x = parseInt(str[i]);
		if (!isNaN(x)) {
			arr.push(parseInt(str[i]));
		}
	}
	return arr.join('');
}

console.log(getDigits('0s1a3y5w7h9a2t4?6!8?0'));

function acronyms(str) {
	var arr = str.split(' ');
	var newArr = [];
	for (var i = 0; i < arr.length; i++) {
		newArr.push(arr[i][0]);
	}
	return newArr.join('').toUpperCase();
}

console.log(acronyms(" there's no free lunch - gotta pay yer way. "));
console.log(acronyms("Live from New York, it's Saturday Night!"));

function countNonSpace(str) {
	var count = 0;
	for (var i = 0; i < str.length; i++) {
		if (str[i] != ' ') {
			count++;
		}
	}
	return count;
}
console.log(countNonSpace('Honey pie, you are driving me crazy'));

function removeShorterStrings(arr, val) {
	for (var i = arr.length - 1; i >= 0; i--) {
		console.log(i, arr[i], arr[i].length);
		if (arr[i].length < val) {
			removeAt(arr, i);
		}
	}
	return arr;
}
console.log(
	removeShorterStrings(
		['Honey', 'pie,', 'you', 'are', 'driving', 'me', 'crazy'],
		4
	)
);
