"use strict";
// Use strict ensures the following:
/*
 * Cannot use variable without var or let or const keywords
 * Cannot use reserved words like eval or arguments for variables
 * Cannot delete a variable
 * Cannot delete a function
 * Controls what "this" means in certain contexts
 */
show("Look at operators.js to see how this page is setup.", "h1");
// Switch statement
const grade = "C";
show(`Switch statement: ${switchGrade(grade)}`);

// Here is the object we will use when needing 1.
let sampleObj = {
  name: "Kevin",
  age: "26",
  likes: "Self-expression",
  dislikes: "Repression",
  siblings: 4,
  isAdult: function () {
    return this.age >= 18;
  },
  testThis: function () {
    return JSON.stringify(this);
  },
};

// for in/for of loops
show(forInLoop(sampleObj));
show(forOfLoop(sampleObj));

// Math operators
show(mathOperators(0));

// Logic operators
show(shortCircuit());

// Exception handling
show(exceptionHandling());

// Exception throwing and catching
show(exceptionCatching());

// Typeof and Instanceof operators
show(typeAndInstance("someString", 32, { type: "obj", why: "because" }));

// Testing "this"
show(
  `What is "this"? Use console to test button! In global scope: ${this} ` +
    whatIsThis()
);

// Testing spread operator
show(spread());

show(`That's all folks!`, "h1");

// BOOKMARK

/**
 * This function does a switch statement to show a different message depending on grade.
 * @param {string} grade The letter grade we got.
 * @returns {string} A msg based on our grade.
 */
function switchGrade(grade) {
  let result = "";
  switch (grade) {
    case "A":
      result = "You got an A!";
      break;
    case "B":
      result = "You got a B!";
      break;
    case "C":
      result = "You got a C!";
      break;
    case "D":
      result = "You got a D!";
      break;
    default:
      result = "You...did not pass. :(";
      break;
  }
  return result;
}

/**
 * This function uses a forIn loop to iterate through an object.
 * @param {Object} obj The object we will iterate on.
 * @returns {string} The result object in string form
 */
function forInLoop(obj) {
  let result = {};
  for (const key in obj) {
    if (Object.hasOwnProperty.call(obj, key)) {
      result[key] = obj[key];
    }
  }
  return "forIn loop: " + JSON.stringify(result);
}

/**
 * This function uses a forOf loop to iterate through an object.
 * @param {Object} obj The object we will iterate on.
 * @returns {string} The result string
 */
function forOfLoop(obj) {
  let result = {};
  for (const key of Object.keys(obj)) {
    result[key] = obj[key];
  }
  return "forOf loop: " + JSON.stringify(result);
}

/**
 * This function does a bunch of math operators on a number
 * and executes a ternary operator to check its value
 * @param {number} num The number to do math operators on
 * @returns {string} Resulting string
 */
function mathOperators(num) {
  let result = "";
  num += 3;
  num -= 2;
  num *= 3;
  num /= 2;
  num **= 3;
  // Concatenate (thus incorrect or buggy result)
  result += "Concat: " + num + "23";
  // Ternary Operator
  result +=
    num > 100 ? " Number was greater than 100" : " Number was less than 100";
  result += " after the operations.";
  return result;
}

/**
 * This function attempts a condition with && to note the 2nd part won't
 * happen if the first part isn't true. Hence, short circuit or lazy
 * @returns {string} Resulting string to see whether condition was true or not
 */
function shortCircuit() {
  let result = "Short Circuit conditions: ";
  if (show(!sampleObj.isAdult()) && show("2nd part of if")) {
    return result + "Both of the if expressions showed above";
  }
  return result + "Notice what parts of the conditions showed above...";
}

/**
 * This shows very simple exception handling
 * @returns {string} The string to show which blocks we hit
 */
function exceptionHandling() {
  let result = "Exception Handling: ";
  try {
    result += "||In try block.|| ";
    x = 29;
    console.log(`This shouldn't be executed...`);
  } catch (error) {
    result += `In catch block. Error is: ${error}|| `;
  } finally {
    result += `Either way, we hit the finally block.||`;
  }
  return result;
}

/**
 * Does exception throwing
 * @returns Resulting string at end
 */
function exceptionThrowing() {
  let result = "";
  try {
    x = 9;
  } catch (e) {
    throw {
      message: "Example message of thrown custom error: " + e.message,
      name: "SomeUniqueException",
    };
  }
  return result;
}

/**
 * Does exception catching using the function that threw an exception
 * @returns {string} Resulting string
 */
function exceptionCatching() {
  let result = "Exception Catching and Throwing: ";
  try {
    exceptionThrowing();
  } catch (e) {
    result += "e.message: " + e.message + " e.name: " + e.name;
  }
  return result;
}

/**
 * This function tests types of items passed and asks each one
 * if it is an instance of Object.
 * @param  {...any} items Any amount of any items to use for the tests
 * @returns {string} Resulting string to say what results were
 */
function typeAndInstance(...items) {
  let result = "Types and Instances: ";
  items.forEach((item) => {
    result += `Type of ${item} is ${typeof item}. `;
    result += `Is ${item} an instance of Object? ${item instanceof Object}. `;
  });
  return result;
}

/**
 * This function tests various ways of using "this". Assumes 'use strict'
 * @returns {string} Resulting string
 */
function whatIsThis() {
  let result = "";
  result += `In function: ${this} `;
  result += `In object: ${sampleObj.testThis()} `;

  // Testing event handlers:
  let contentArea = document.getElementById("content");
  let btn = document.createElement("button");
  btn.textContent = "Pass to function from event handler in HTML";
  btn.onclick = function () {
    console.log(`This in event: ${this}`);
  };
  contentArea.appendChild(btn);

  // Call and Apply
  let sampleObj2 = { age: 20 };
  result += `In .call of a method of object: ${sampleObj.testThis.call(
    sampleObj2
  )} `;
  result += `In .apply: ${sampleObj.testThis.apply(sampleObj2)} `;

  // Constructor functions
  function Person(name, age) {
    this.name = name;
    this.age = age;

    this.testThis = function () {
      return JSON.stringify(this);
    };
  }

  result += `In constructor: ${new Person("sam", 92).testThis()}`;
  return result;
}

/**
 * Uses spread operator
 * @returns {string} Resulting string
 */
function spread() {
  let result = "Spread operator: ";
  let str = "string";
  let prims = [1, "string", true, BigInt(2), null, undefined];
  let objs = [
    { age: 2, name: "sam" },
    { age: 12, name: "paul" },
  ];

  result += `Spread with string: [${[...str]}] `;
  result += `Copy array of prims: [${[...prims]}] `;
  result += `Copy array of objs: [${[...objs]}] `;
  result += `Concat 2 arrays: [${[1, 2].concat([3, 4])}] `;

  function paramSpread(...items) {
    return items;
  }

  result += `Pass parameters: ${paramSpread(2, 3, 4)} `;
  let shallowCopy = { ...sampleObj };
  result += `Shallow copy: ${JSON.stringify(shallowCopy)}`;
  return result;
}