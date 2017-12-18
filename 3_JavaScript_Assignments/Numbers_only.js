
function numbersonly(arr){
    var newarr = [];
    for (var i = 0; i < arr.length; i++) {
        if(typeof(arr[i]) == "number"){
            newarr.push(arr[i])
        }
    }
    console.log(newarr);
    return newarr;
}
numbersonly([1, "apple", -3, "orange", 0.5]);
