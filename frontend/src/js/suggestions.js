const generateCards = (container, dog) => {
  const card = document.createElement('div');
  card.classList.add('card');

  const imgContainer = document.createElement('div');
  imgContainer.classList.add('img-container');

  const cardImg = document.createElement('img');
  cardImg.classList.add('card-img-top');
  cardImg.classList.add('img-fluid');
  cardImg.classList.add('dog-img');
  cardImg.setAttribute('alt', `Image of dog ${dog.name}`);
  cardImg.setAttribute('src', dog.imgURL);

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

  imgContainer.appendChild(cardImg);

  card.appendChild(imgContainer);
  card.appendChild(cardBody);

  container.appendChild(card);
};

const init = () => {
  const cardsContainer = document.getElementById('cards-container');
  fetch(
    'http://127.0.0.1:5001/get_recommendation?' +
      new URLSearchParams({
        id: window.localStorage.getItem('referenceId'),
      })
  )
    .then(res => res.json())
    .then(data => {
      console.log(data.recommendations);
      data.recommendations.forEach(dog => {
        generateCards(cardsContainer, dog);
      });
    })
    .catch(err => console.log(err));

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
