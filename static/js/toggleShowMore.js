(function toggleShowMore() {
  const SECOND = 10 * 100;
  const TWENTY_FOUR_HOURS = 24 * 60 * 60 * SECOND;
  const TWO_WEEKS = 2 * 7 * TWENTY_FOUR_HOURS;
  const HIDE_TEXT = 'Hide';
  const VISUALLY_HIDDEN_CLASS_NAME = 'visually-hidden';
  const HIDDEN_CLASS_NAME = 'item-hidden';
  const NOW = new Date();
  const NO_EVENTS_NOTICE = (function() {
    const div = document.createElement('div');
    div.innerText = 'No events';
    return div;
  })();

  // Store events beyond two weeks to be toggled
  const eventsByListIndex = [];

  const lists = document.querySelectorAll('.events > .list');
  const buttons = document.querySelectorAll('.events-button');

  lists.forEach((list, index) => {
    const futureEvents = [];
    list.querySelectorAll('.item').forEach(event => {
      const dateString = event.querySelector('time').getAttribute('datetime');
      const date = new Date(dateString);

      // Remove events that have already occured (with buffer)
      const isPastEvent = NOW - date > TWENTY_FOUR_HOURS / 4;
      if (isPastEvent) {
        event.remove();
      }

      // Hide events that are more than two weeks ahead
      const isWithinTwoWeeks = date - NOW < TWO_WEEKS;
      if (!isWithinTwoWeeks) {
        event.classList.add(HIDDEN_CLASS_NAME, VISUALLY_HIDDEN_CLASS_NAME);
        futureEvents.push(event);
      }
    });

    if (!futureEvents.length) {
      list.parentNode.appendChild(NO_EVENTS_NOTICE);
      buttons[index].remove();
    }
    eventsByListIndex[index] = futureEvents;
  });

  buttons.forEach(function(button, index) {
    const initialText = button.textContent;
    button.addEventListener('click', function click(ele) {
      // Toggle text of button
      const elementText =
        ele.target.textContent === initialText ? HIDE_TEXT : initialText;
      ele.target.textContent = elementText;

      // Toggle visibility of events
      const events = eventsByListIndex[index];
      events.forEach((event, index) => {
        event.classList.toggle(VISUALLY_HIDDEN_CLASS_NAME);
        setTimeout(() => {
          event.classList.toggle(HIDDEN_CLASS_NAME);
        }, 30 * index);
      });
    });
  });
})();
