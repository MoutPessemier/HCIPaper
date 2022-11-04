const generateCards = (container, json) => {
  // <div class="card">
  //   <img src="#" class="card-img-top" alt="#" />
  //   <div class="card-body">
  //     <h5 class="card-title">Card title</h5>
  //     <p class="card-text">
  //       Some quick example text to build on the card title and make up the bulk of the card's content.
  //     </p>
  //   </div>
  // </div>
  //TODO: add text and attributes to the correct elements
  const card = document.createElement('div');
  const cardImg = document.createElement('img');
  const cardBody = document.createElement('div');
  const cardTitle = document.createElement('h5');
  const cardText = document.createElement('p');

  cardBody.appendChild(cardTitle);
  cardBody.appendChild(cardText);

  card.appendChild(cardImg);
  card.appendChild(cardBody);

  container.appendChild(card);
};

const init = () => {
  // this needs to happen as soon as the backend sends over the result via a get method
  const cardsContainer = document.getElementById('cards-container');
  generateCards(cardsContainer, '');
};

window.onload = init();
