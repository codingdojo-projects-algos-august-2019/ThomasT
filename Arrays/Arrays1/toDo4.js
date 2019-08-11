function shuffle(arr) {
	for (var i = arr.length - 1; i >= 0; i--) {
		var randomIndex = Math.floor(Math.random() * i);
		temp = arr[i];
		arr[i] = arr[randomIndex];
		arr[randomIndex] = temp;
	}
	return arr;
}

console.log('Shuffle', shuffle([1, 2, 3, 4, 5, 6]));

function removeRange(arr, start, end) {
	for (var i = end; i >= start; i--) {
		arr[i] = arr[i + 1];
		arr.length--;
	}
	return arr;
}

console.log(removeRange([20, 30, 40, 50, 60, 70], 2, 4));

function insertAt(arr, position, val) {
	for (var i = arr.length; i >= position; i--) {
		arr[i] = arr[i - 1];
	}
	arr[position] = val;
	return arr;
}

function intermediateSums(arr) {
	var sum = 0;
	var i = 0;
	while (i <= arr.length) {
		if (i % 10 == 9) {
			sum += arr[i];
			insertAt(arr, 10, sum);
			i++;
			sum = 0;
		} else if (arr.length == i) {
			arr[arr.length] = sum;
			i++;
		} else {
			sum += arr[i];
		}
		i++;
	}
	return arr;
}

console.log(
	'intermediateSums:',
	intermediateSums([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
);

function doubleTrouble(arr) {
	for (var i = arr.length * 2 - 1; i > 0; i--) {
		position = Math.ceil((i + 1) / 2) - 1;
		arr[i] = arr[position];
	}
	return arr;
}
console.log('doubleTrouble:', doubleTrouble([4, 'Ulysses', 42, false]));

function zipIt(arr1, arr2) {
	var totalLength = -1;
	var maxLength = arguments[0].length;
	for (var i = 0; i < arguments.length; i++) {
		totalLength += arguments[i].length;
		if (maxLength < arguments[i].length) {
			maxLength = arguments[i].length;
		}
	}
	var i = maxLength - 1;
	while (i >= 0) {
		for (var j = arguments.length - 1; j >= 0; j--) {
			if (arguments[j][i] != undefined) {
				arguments[0][totalLength] = arguments[j][i];
				totalLength--;
			}
		}
		i--;
	}
	return arguments[0];
}
console.log('zipIt:', zipIt([1, 2, 3, 4], [10, 20, 30, 40]));
