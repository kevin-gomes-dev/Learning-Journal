 'use strict';
 let pageList = [
  'index',
  'operators',
  'variables-types',
  'obj-proto-class',
  'func',
  'arrays'
];

// Immediately Invoked Function Expression (IIFE) to setup links on each page
/**
 * This function simply sets up the layout of the links to all the pages in this learning journal.
 * It does so by inserting <a> elements within the div for pages and br tags in between
 * Pages can be added via changing the listOfPages
 */
(function setupPages(pageList) {
  let pagesDiv = document.getElementById('pages');
  // Assume each html file is in the same directory
  pageList.forEach((page) => {
    let link = document.createElement('a');
    link.href = './' + page + '.html';
    link.innerHTML = page;
    pagesDiv.appendChild(link);
    pagesDiv.appendChild(document.createElement('br'));
  });
  
})(pageList);

/**
 * This function allows us to display anything by adding an element to the page.
 * Each time this is called, another element is added to the page.
 * Optionally, we can add the tag (type of element), default is h4.
 * Optionally, we can add the id of the element, default is empty.
 * Assumes a "content" div but we could easily change this if we want
 * to create the div and set its id.
 * @param {any} stuff The stuff we wish to display on the screen.
 * @param {string} element The HTML element we want to enclose the stuff in.
 * @param {string} id The ID to use to refer to this element.
 */
function show(stuff,element = 'h3',id = undefined) {
  let contentArea = document.getElementById('content');
  let newElement = document.createElement(element);
  if (id) {newElement.id = id};
  newElement.innerHTML = stuff;
  contentArea.appendChild(newElement);
  return stuff;
}