const generateCards = (container, dog) => {
  const card = document.createElement('div');
  card.classList.add('card');

  const cardImg = document.createElement('img');
  cardImg.classList.add('card-img-top');
  cardImg.setAttribute('alt', `Image of dog ${dog.name}`);
  cardImg.setAttribute('src', dog.imageURL);

  const cardBody = document.createElement('div');
  cardBody.classList.add('card-body');

  const cardTitle = document.createElement('h5');
  cardTitle.classList.add('card-title');
  cardTitle.innerHTML = dog.name;

  const cardText = document.createElement('p');
  cardText.classList.add('card-text');
  cardText.innerHTML = dog.description;

  cardBody.appendChild(cardTitle);
  cardBody.appendChild(cardText);

  card.appendChild(cardImg);
  card.appendChild(cardBody);

  container.appendChild(card);
};

const init = () => {
  const cardsContainer = document.getElementById('cards-container');
  fetch('')
    .then(data => data.json())
    .then(dogs => {
      dogs.forEach(dog => {
        generateCards(cardsContainer, dog);
      });
    });

  const submitBtn = document.getElementById('submit');
  submitBtn.addEventListener('click', e => {
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      //TODO: get values
      //body: JSON.stringify(),
    };
    fetch('', options)
      .then(data => {
        if (!data) {
          throw Error(data.status);
        }
        return data.json();
      })
      //TODO: update
      .then(update => {});
  });
};

window.onload = init();
