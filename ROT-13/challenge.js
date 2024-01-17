const rl = require('readline')

/*
Explaination:
Input (s): String 
Output: String

Since we are using rotation 13. It means very char will be rotated as 
Encrypted: N O P Q R S T U V W X Y Z A B C D E F G H I J K L M. 

For every char check for its corresponding rotated-13 val

I may store all values and their corresponding val in a table form (object)

loop thtough the string and pick each corresponding encrupted vals val

*/

const Rotate13 = (s) => {
    // I made a variable to store results
  let rotatedString = "";

  // Because we are not rotating the char by Nth postion but 13 position, I have stored every rotated encrypted value
  const encruptedVals = {
    A: "N",
    B: "O",
    C: "P",
    D: "Q",
    E: "R",
    F: "S",
    G: "T",
    H: "U",
    I: "V",
    J: "W",
    K: "X",
    L: "Y",
    M: "Z",
    N: "A",
    O: "B",
    P: "C",
    Q: "D",
    R: "E",
    S: "F",
    T: "G",
    U: "H",
    V: "I",
    W: "J",
    X: "K",
    Y: "L",
    Z: "M",
  };

  // Looping through all value of the string to check each encryped val from the saved vals
  for (let i = 0; i < s.length; i++) {
    // Check if current val is alphabet ?
    if (encruptedVals[s[i].toUpperCase()]) { 
        // Fetch the current val corresponding val from the encryped table and add as result
       rotatedString +=
         s[i].toUpperCase() === s[i]
           ? encruptedVals[s[i].toUpperCase()]
           : encruptedVals[s[i].toUpperCase()].toLowerCase();
    } else {
      rotatedString += s[i];
    }
  }

  console.log(rotatedString); 
  return rotatedString
};

// Time complexity: O (n)
// Space Complexity: O (1)

// Function to accept input from user
let readline = rl.createInterface({
    input: process.stdin,
    ouput: process.stdout
})

// Get answer and encrypt it
readline.question('Enter a string to be encrypted:', (answer)=>{
    Rotate13(answer)
    readline.close()
})


