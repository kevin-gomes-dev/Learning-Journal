/**
 * This IIFE simply sets up the intro of the home page
 * We create an h1 here to do so, in the 'content' portion
 */
(function setupHome() {
  const contentArea = document.getElementById('content');
  const intro = document.createElement('h1');
  
  intro.innerHTML = "Welcome to the home page! To see how this was setup, look at utils.js and index.js" +
  ", otherwise navigate to any page you wish to view snippets from what I've learned from lessons on Pluralsight";

  contentArea.appendChild(intro);
})();