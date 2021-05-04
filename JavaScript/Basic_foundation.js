//get 1 to 255
function creatArray(num) {
    var newArray = [];
    for (var i = 1; i <= num; i++) {
        newArray.push(i);
    }
    return(newArray);
}
creatArray(255);

//sum of even nmber 1 to 1000
var sum = 0;

function sumeven(num) {
    for (let i = 2; i <= num; i += 2) {
        sum = sum + i;
    }
    return(sum);
}
sumeven(1000);

//sum of odd number 1 to 5000
var sum = 0;

function sumodd(num) {
    for (let i = 1; i <= num; i += 2) {
        sum = sum + i;
    }
    return(sum);
}
sumodd(5000);

//Iterate an array

var arr = [3, 20, 15, 70, 100];
var sum = 0;

function sumArray() {

    for (let i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
    }
    return(sum);

}
sumArray();

//max 
var arr = [6, -7, 67, -409, 2090, -1001, 3008];
var max = 0;

function biggest() {

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return(max);
}

biggest();

//average 

var arr = [50, 99, 67, 139, 890, 698, 233];
var avg = 0;
var sum = 0;

function average() {
    for (let i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
    }
    avg = (sum / arr.length);
    return(avg.toFixed(2));
}

average();

//array odd

function creatArray(num) {
    var newArray = [];
    for (var i = 1; i <= num; i++) {
        if (i % 2 != 0) {
            newArray.push(i);
        }
    }
    return(newArray);
}
creatArray(50);

//Greater than Y

var arr = [438, -7, 67, -409, 698, 329, 1000];
var Y = 400;
var bigger_num = 0;

function bigger_y() {

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > Y) {
            bigger_num = bigger_num + 1;
        }
    }
    return(bigger_num);
}

bigger_y();

//square 

var arr = [2, 10, 13, 15, 19, 25, 33];


function square() {

    for (let i = 0; i < arr.length; i++) {
        arr[i] = Math.pow(arr[i], 2);
    }
    return(arr);
}

square();

// Negatives

var arr = [-2, 10, 13, -15, 19, -25, 33];

function negative() {
    for (var i = 0; i <= arr.length; i++) {
        if (arr[i] < 0) {
            arr[i] = 0;
        }
    }
    console.log(arr);
}
negative();

//max min avg

var arr = [10, -10, 50, 16];

function creatArray() {
    var newArray = [];
    var max = 0;
    var min = 0;
    var avg = 0;
    var sum = 0;

    for (var i = 0; i <= arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];

        } else if (arr[i] < min) {

            min = arr[i];
        }
    }
    for (let i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
    }
    avg = (sum / arr.length);
    newArray.push(max);
    newArray.push(min);
    newArray.push(avg);
    console.log(newArray);
}
creatArray();

//swap 

var arr = [3, 20, 15, -70];

function swapArray() {
    [arr[0], arr[3]] = [arr[3], arr[0]]
    console.log(arr);
}
swapArray();

// negative = dojo

var arr = [6, -20, -15, 90];

function swapArray() {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arr[i] = "Dojo";
        }
    }
    console.log(arr);
}
swapArray();