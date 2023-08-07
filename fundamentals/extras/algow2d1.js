
function makeFrequencyTable(arr) {
    var output = {}
    for(var i = 0; i < arr.length; i++){
        if (output[arr[i]]){
            output[arr[i]] += 1 
        } else
        output[arr[i]] = 1
    }
    return output
}

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

function nonMatchingInt(arr) {
    const dict = makeFrequencyTable(arr);

    for (let i = 0; i < arr.length; i++) {
        if ((dict[arr[i]] % 2) !== 0) {
            return arr[i];
        }
    }
}

console.log(nonMatchingInt(nums1), "should equal", expected1);
console.log(nonMatchingInt(nums2), "should equal", expected2);
console.log(nonMatchingInt(nums3), "should equal", expected3);
console.log(nonMatchingInt(nums4), "should equal", expected4);