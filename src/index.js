(function setupHome() {
  let contentArea = document.getElementById('content');
  let intro = document.createElement('h1');
  
  intro.innerHTML = "Welcome to the home page! To see how this was setup, look at utils.js and index.js" +
  ", otherwise navigate to any page you wish to view snippets from what I've learned from lessons on Pluralsight";

  contentArea.appendChild(intro);
})();