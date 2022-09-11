'use strict';
// Use strict ensures the following:
/*
 * Cannot use variable without var or let or const keywords
 * Cannot use reserved words like eval or arguments for variables
 * Cannot delete a variable
 * Cannot delete a function
 * Controls what "this" means in certain contexts
 */

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

// Intro text
show("Look at vars.js to see how this page is setup.", "h1");

// Template Literal
show(tempLit('sampleString'));

// Tagged template literal
show(taggedTempLit());

// Let VS Const
show(letVsConst());

// Destructure functionality
show(destruct());

// Symbols
show(symbols());

/**
 * This just returns a template literal
 * @param {string} string The sample string to display
 * @returns {string} String
 */
function tempLit(string) {
  return `Template Literal: Param passed was ${string}`;
}

/**
 * This is the tagger function that tags a template literal,
 * making each value in it italic
 * @param {string} strings The strings being passed
 * @param  {...any} values The values evaluated in the temp literal
 * @returns {string} Resulting string with modifications made to values
 */
function italics(strings, ...values) {
  let result = "";
  // For every string in the literal:
  /*
    * If we are passed the first one (since the first is always a string)
      * Add <i> and </i> around the evaluated values[i-1] (starts at 0)
    * Add the original string at index i (starts at 0)
  */
 // Then return result string
  for (let i = 0; i < strings.raw.length; i++) {
    if (i > 0) {
      result += `<i>${values[i-1]}</i>`;
    }
    result += strings.raw[i]
  }
  return result;
}

/**
 * This reutnrs a tagged template literal using 'italics'
 * @returns {string} Template literal tagged with italics
 */
function taggedTempLit() {
  let str1 = 'italic';
  let str2 = 'expression';
  let str3 = 'evaluated';
  return italics `Tagged Template Literal: This template lit
   is ${str1} for every ${str2} that is ${str3}`;
}

/**
 * Shows constraints between let and const. We do not show scope,
 * but scope is of course block scope.
 * @returns {string} Resulting string after all try catch blocks have been done
 */
function letVsConst() {
  let x = 3, y = 3;
  const mul = 4;
  const constObj = {name: 'paul',age: 22};
  let result = `Let VS Const: Original vars are 
  x: ${x}, y: ${y}, mul: ${mul}, constObj: ${JSON.stringify(constObj)} `;
  // Try changing x and y
  try {
    result += `Attempting to change x and y: `;
    x = 4;
    y = 6;
    result += `x: ${x}, y: ${y} `;
  }
  catch (e) {
    result += e + ' ';
  }
  // Try changing mul
  try {
    result += `Attempting to change const mul: `;
    mul = 4;
    result += `mul: ${mul} `;
  }
  catch (e) {
    result += e + ' '
  }
  // Try changing constObj
  try {
    result += `Attempting to change const constObj: `;
    constObj = {name: 'sam',age: 22};
    result += `constObj: ${JSON.stringify(constObj)} `;
  }
  catch (e) {
    result += e + ' ';
  }
  // Try changing property of constObj
  try {
    result += `Attempting to change property of obj referenced by const constObj: `;
    constObj.age = 9;
    result += `constObj.age: ${constObj.age} `;
  }
  catch (e) {
    result += e + ' ';
  }
  return result;
}

/**
 * This function uses destructing to create variables from an array
 * It also uses default values and spread operator for other items
 * @returns {string} Result
 */
function destruct() {
  let result = 'Destructure: ';
  let a = [23,'sam'];
  let [id = "NO-ID",name = "NO-NAME",age = "NO-AGE",...others] = a;
  result += `id: ${id}, name: ${name}, age: ${age}, ...others: ${others}`;
  return result;
}

/**
 * This function uses Symbols and tests some aspects of using them.
 * @returns {string} Result
 */
function symbols() {
  let result = 'Symbols: ';
  let sym1 = Symbol.for('test');
  let sym2 = Symbol('test');
  let sym3 = Symbol.for('test');
  result += `${sym1.toString()}, ${sym2.toString()}, ${sym3.toString()} `;
  result += `1 and 2 =? ${sym1===sym2}. 1 and 3 =? ${sym1===sym3} `;

  let obj = {name: 'Barry',[sym1]: 90};
  // Note we can use sym1 or sym3 since they are the same
  result += `Hidden property: ${obj[sym3]}`;
  return result;
}
