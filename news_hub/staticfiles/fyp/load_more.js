var loadingItems = false;

// Create an intersection observer instance
var observer = new IntersectionObserver(function(entries) {
  if (entries[0].isIntersecting && !loadingItems) {
    loadMoreItems();
  }
}, { threshold: 1 });

// Observe the element with the ID "load-more"
observer.observe(document.getElementById('load-more'));

function loadMoreItems() {
  var nextPageUrl = $('.pagination .next a').attr('href');

  if (!nextPageUrl) {
    // No more items available
    return;
  }

  loadingItems = true;
  $('#loading-spinner').show();

  $.ajax({
    url: nextPageUrl,
    success: function(data) {
      var $newItems = $(data).find('#card-container').children();
      $('#card-container').append($newItems);
      loadingItems = false;
      $('#loading-spinner').hide();

      // Disconnect the observer temporarily to avoid duplicate triggers
      observer.disconnect();

      // Re-observe the element with the ID "load-more"
      observer.observe(document.getElementById('load-more'));
    },
    error: function() {
      loadingItems = false;
      $('#loading-spinner').hide();
    }
  });
}
