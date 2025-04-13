'use strict';

document.addEventListener('DOMContentLoaded', function() {
    new PagefindUI({ 
      element: "#search",
      showSubResults: true,
      showImages: false,
      sort: { date: "desc" }
    });
    
    const searchContainer = document.getElementById('search');
    const searchToggle = document.getElementById('search-toggle');
    const searchIcon = searchToggle.querySelector('.search-icon');
    const closeIcon = searchToggle.querySelector('.close-icon');
    
    searchContainer.style.display = 'none';

    function closeSearch() {
      searchContainer.classList.add('fade-out');
      setTimeout(() => {
        searchContainer.style.display = 'none';
        searchContainer.classList.remove('fade-out');
        searchIcon.style.display = 'inline';
        closeIcon.style.display = 'none';
      }, 125); 
    }
    
    searchToggle.addEventListener('click', function(e) {
      e.preventDefault();
      if (searchContainer.style.display === 'none') {
        searchContainer.style.display = 'block';
        searchContainer.querySelector('input').focus();
        searchIcon.style.display = 'none';
        closeIcon.style.display = 'inline';
      } else {
        closeSearch();
      }
    });
    
    document.addEventListener('click', function(e) {
      if (!searchContainer.contains(e.target) && !searchToggle.contains(e.target)) {
        closeSearch();
      }
    });
    
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && searchContainer.style.display === 'block') {
        closeSearch();
      }
    });
});