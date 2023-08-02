const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

const nums2 = [5, 6, 7, 8, 9];
const expected2 = "5-9";

const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
const expected3 = "1-3, 7, 9, 15-17";


function bookIndex(nums) {
  var joinedStr = "";
  var separator1 = ", ";
  var separator2 = "-";
  var tempArr = [];
  var consecStr = "";
  for (var i = 0; i < nums.length; i++) {
    // Checks if nums starts with a consec, if not pushes to joined str
    if (nums[i] == nums[nums.length-1]){
        joinedStr += nums[i];
    } else if (nums[i] - 1 == nums[i - 1] && nums[i] + 1 != nums[i + 1]) {
        tempArr.push(nums[i]);
        consecStr += tempArr[0];
        consecStr += separator2;
        consecStr += tempArr[tempArr.length-1];
        joinedStr += consecStr;
        joinedStr += separator1
        consecStr = ""
        tempArr = []
    } else if (nums[i + 1] == nums[i] + 1) {
        tempArr.push(nums[i]);
    } else {
        joinedStr += nums[i];
        joinedStr += separator1;
    }
  }
    return joinedStr
}



console.log(bookIndex(nums1));
console.log(bookIndex(nums2));
console.log(bookIndex(nums3));


