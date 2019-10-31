// Unleash bats if batman is deleted
const batmanObserver = new MutationObserver(mutationHandler);
const body = document.querySelector("body");
const batman = document.querySelector("#batman");
batmanObserver.observe(body, { childList: true });

function mutationHandler(mutations) {
  mutations.forEach((mutation) => {
    mutation.removedNodes.forEach((node) => {
      if (node.id === "batman") {
        const batNumbers = Math.floor(Math.random() * 50) + 10;
        for (let i = 0; i < batNumbers; i++) {
          body.appendChild(createBat());
        }
      }
    });
  });
}

function createBat() {
  const batContainer = document.createElement("div");
  batContainer.classList.add("x");
  const bat = document.createElement("img");
  bat.setAttribute("src", "/img/batman.svg");
  bat.classList.add("y");
  batContainer.appendChild(bat);
  batContainer.style.animation = `x ${Math.random() * 10}s linear infinite alternate`;
  bat.style.animation = `y ${Math.random() * 10}s linear infinite alternate`;
  return batContainer;
}