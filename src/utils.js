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

