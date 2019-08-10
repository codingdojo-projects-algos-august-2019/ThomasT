var array = [1, 2, 3, 4, 5];

function reverseArr(arr) {
	for (
		var i = 0, j = arr.length - 1;
		i <= Math.floor(arr.length / 2);
		i++, j--
	) {
		var temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	console.log(arr);
}

// reverseArr(array);

function rotateArr(arr, shiftBy) {
	if (shiftBy > 0) {
		for (var j = 0; j < shiftBy; j++) {
			var temp = arr[arr.length - 1];
			for (var i = arr.length - 1; i >= 0; i--) {
				arr[i] = arr[i - 1];
			}
			arr[0] = temp;
		}
	} else {
		for (var j = 0; j > shiftBy; j--) {
			var temp = arr[0];
			for (var i = 0; i < arr.length; i++) {
				arr[i] = arr[i + 1];
			}
			arr[arr.length - 1] = temp;
		}
	}
	console.log(arr);
}

// rotateArr(array, -1);
// rotateArr(array, 1);

function filterRange(arr, min, max) {
	var newArr = [];
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] >= min && arr[i] <= max) {
			newArr[newArr.length] = arr[i];
		}
	}
	console.log(newArr);
	return newArr;
}
// filterRange(array, 1, 4);

function concatArray(arr1, arr2) {
	var newArr = [];
	for (var i = 0; i < arguments.length; i++) {
		for (var j = 0; j < arguments[i].length; j++) {
			newArr[newArr.length] = arguments[i][j];
		}
	}
	console.log(newArr);
}
concatArray([1, 2], ['a', 'b']);

function skylineHeights(arr) {
	var newArr = [];
	for (var i = 0; i < arr.length; i++) {
		if (newArr.length == 0) {
			if (arr[i] > 0 && arr[i]) {
				newArr[newArr.length] = arr[i];
			}
		} else {
			if (arr[i] > 0 && arr[i] > newArr[newArr.length - 1]) {
				newArr[newArr.length] = arr[i];
			}
		}
	}
	console.log(newArr);
}

skylineHeights([0, 5, 1, 6, 2, 5, 9, 9]);
