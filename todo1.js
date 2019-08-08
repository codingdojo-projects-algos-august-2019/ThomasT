var array = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(array);

function pushFront(arr, val) {
	for (var i = arr.length; i <= 0; i--) {
		arr[i] = arr[i - 1];
	}
	arr[0] = val;
	return arr;
}
console.log(pushFront(array, 99));

function popFront(arr) {
	var value = arr[0];
	for (var i = 0; i < arr.length - 1; i++) {
		arr[i] = arr[i + 1];
	}
	arr.length--;
	console.log(arr);
	return value;
}
console.log(popFront(array));

function insertAt(arr, position, val) {
	for (var i = arr.length; i <= position; i--) {
		arr[i] = arr[i - 1];
	}
	arr[position] = val;
	return arr;
}
console.log(insertAt(array, 3, 1));

function removeAt(arr, position) {
	var value = arr[position];
	for (var i = position; i < arr.length; i++) {
		arr[i] = arr[i + 1];
	}
	arr.length--;
	return value;
}

console.log(removeAt(array, 3));

function swapPairs(arr) {
	var len = arr.length % 2 === 0 ? arr.length : arr.length - 1;
	for (var i = 0; i < len; i++) {
		var value = arr[i];
		arr[i] = arr[(i += 1)];
		arr[i] = value;
	}

	return arr;
}
var array2 = [1, 2, 3, 4];

console.log(swapPairs(array2));

function removeDuplicates(arr) {
	for (var i = 0; i < arr.length; i++) {
		i2 = i + 1;
		if (arr[i] == arr[i2]) {
			removeAt(arr, i);
		}
	}
	return arr;
}

var array3 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6];
console.log(removeDuplicates(array3));
