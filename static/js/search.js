'use strict';

document.addEventListener('DOMContentLoaded', function() {
    new PagefindUI({ 
      element: "#search",
      showSubResults: true,
      showImages: false,
      sort: { date: "desc" }, // sort by date descending
      translations: {
        placeholder: "Search anything from NUS Hackers...",
        zero_results: "Couldn't find [SEARCH_TERM]. Try searching for something else.",
    }
      
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
      }, 125); // 125ms to prevent flicker behaviour
    }
    
    // toggle from search icon
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
      // Check if the click is outside the search container when not on mobile, and click was due to 'more results' button
      if (!searchContainer.contains(e.target) && !searchToggle.contains(e.target) && 
      window.innerWidth >= 768 && !e.target.classList.contains('pagefind-ui__button')) {
        closeSearch();
      }
    });
    
    // close search on escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && searchContainer.style.display === 'block') {
        closeSearch();
      }
    });

    const mobileExitButton = searchContainer.querySelector('.mobile-search-exit');
    
    if (mobileExitButton) {
        mobileExitButton.addEventListener('click', function(e) {
            e.preventDefault();

            // force pagefind to clear results
            document.getElementsByClassName('pagefind-ui__search-clear')[0].click();

            closeSearch();
        });
    }
});