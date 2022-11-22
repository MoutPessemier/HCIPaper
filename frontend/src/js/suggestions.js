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

const getSliderValueForQuestion = name => {
  const slider = document.getElementById(`satQ${name}`);
  if (slider) {
    try {
      return parseInt(slider.value);
    } catch (error) {
      console.log(`Error parsing slider value for question ${name}:: ${error}`);
    }
  }
};

const init = () => {
  const cardsContainer = document.getElementById('cards-container');
  fetch(
    'http://127.0.0.1:5001/getRecommendation?' +
      new URLSearchParams({
        id: window.localStorage.getItem('referenceId'),
      })
  )
    .then(res => res.json())
    .then(data => {
      data.recommendations.forEach(dog => {
        generateCards(cardsContainer, dog);
      });
    })
    .catch(err => console.log(err));

  const backBtn = document.getElementById('back');
  backBtn.addEventListener('click', e => {
    const formType = window.localStorage.getItem('formType');
    window.location.href = `/pages/formType${formType}.html`;
  });

  const submitBtn = document.getElementById('submit');
  submitBtn.addEventListener('click', e => {
    const finalTime = new Date().toString().split(' ')[4];
    const body = {
      finalTime,
      ID: window.localStorage.getItem('referenceId'),
      Q1: getSliderValueForQuestion(1),
      Q2: getSliderValueForQuestion(2),
      Q3: getSliderValueForQuestion(3),
    };
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    };
    fetch('http://127.0.0.1:5001/giveResearch', options)
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(err => console.log(err));
  });
};

window.onload = init();
