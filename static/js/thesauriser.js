'use strict';

(function thesauriser() {
  var d = new Date();
  if (d.getMonth() != 3 || d.getDate() != 1) {
    return;
  }
  function randomise(arr) {
    return arr[Math.floor(Math.random()*arr.length)];
  }
  var spreading = document.getElementById("slogan-1");
  var the = document.getElementById("slogan-2");
  var hacker = document.getElementById("slogan-3");
  var culture = document.getElementById("slogan-4");
  spreading.innerText = randomise(["Spreading", "Casting", "Disseminating", "Dispersing", "Diffusing", "Scattering", "Unfurling", "Radiating", "Expanding", "Unrolling"]);
  the.innerText = randomise(["the", "a", "our", "their", "someone's", "lovely", "amazing", "great", "royal", "awesome"]);
  hacker.innerText = randomise(["hacker", "builder", "creator", "artist", "curious", "inquisitive", "Singaporean"]);
  culture.innerText = randomise(["civilisation", "civilization", "culture", "acculturation", "cultivation", "finish", "polish", "refinement"]);
})();
