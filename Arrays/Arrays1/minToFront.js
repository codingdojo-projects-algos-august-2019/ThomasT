var array = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(array);

function pushFront(arr, val) {
	for (var i = arr.length; i >= 0; i--) {
		arr[i] = arr[i - 1];
	}
	arr[0] = val;
	return arr;
}

function removeAt(arr, position) {
	var value = arr[position];
	for (var i = position; i < arr.length; i++) {
		arr[i] = arr[i + 1];
	}
	arr.length--;
	return value;
}

function minToFront(arr) {
	var min = arr[0];
	var position = 0;
	for (var i = 0; i < arr.length; i++) {
		if (min > arr[i]) {
			min = arr[i];
			position = i;
		}
	}
	var value = removeAt(arr, position);
	pushFront(arr, value);
	return arr;
}
var array4 = [5, 2, 7, 1, 4, 3];
console.log('minToFront', minToFront(array4));
