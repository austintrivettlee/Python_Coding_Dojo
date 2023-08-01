/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";
/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str) {
  var trimmedString = str.trim()
  var output = ""
  var emptyArr = []
  for(var i = 0; i < trimmedString.length; i++){
      if ( i == 0 && trimmedString[i] != " ") {
        emptyArr.push(trimmedString[i])
      }
      else if (trimmedString[i] == " "){
        continue
      }
      else if (trimmedString[i-1] == " " && trimmedString[i] != " "){
        emptyArr.push(trimmedString[i])
      }
      
  }
    output += emptyArr.join("")  
    
    return output.toUpperCase();
  }


console.log(acronymize(str1));
console.log(acronymize(str2));
console.log(acronymize(str3));
console.log(acronymize(str4));
