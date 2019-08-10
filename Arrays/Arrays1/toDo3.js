function removeNegatives(arr) {
	for (var i = arr.length - 1; i >= 0; i--) {
		if (arr[i] < 0) {
			if (i == arr.length - 1) {
				arr.length--;
			} else {
				for (var j = i; j < arr.length; j++) {
					arr[j] = arr[j + 1];
				}
				arr.length--;
			}
		}
	}
	return arr;
}
console.log('Remove Negatives:', removeNegatives([-1, 5, 78, 3, -9, 4, -2]));

function second2Last(arr) {
	if (arr.length > 2) {
		return arr[arr.length - 2];
	} else {
		return null;
	}
}

console.log('Second to Last:', second2Last([-1, 5, 78, 3, -9, 4, -2]));

function secondLargest(arr) {
	if (arr.length > 0) {
		var sortedArr = insertionSort(arr);
		return sortedArr[sortedArr.length - 2];
	} else {
		return null;
	}
}
console.log('Second Largest:', secondLargest([42, 1, 4, Math.PI, 7, 9]));

function nth2Last(arr, num) {
	if (arr.length > num) {
		return arr[arr.length - num];
	} else {
		return null;
	}
}

console.log('Nth-to-Last:', nth2Last([5, 2, 3, 6, 4, 9, 7], 3));

function nthLargest(arr, num) {
	sortedArr = insertionSort(arr);
	if (sortedArr.length >= num) {
		return sortedArr[sortedArr.length - num];
	} else {
		return null;
	}
}

function insertionSort(arr) {
	for (var i = 0; i < arr.length; i++) {
		var min = i;
		for (var j = i; j < arr.length; j++) {
			if (arr[min] > arr[j]) {
				min = j;
			}
		}
		var temp = arr[i];
		arr[i] = arr[min];
		arr[min] = temp;
	}
	// console.log('insert', arr);
	return arr;
}

console.log('nth-Largest:', nthLargest([5, 2, 3, 6, 4, 9, 7], 3));
