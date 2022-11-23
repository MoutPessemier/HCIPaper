import * as bootstrap from 'bootstrap';

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
  cardText.innerHTML = dog.summary;

  const cardFooter = document.createElement('div');
  cardFooter.classList.add('card-footer');

  const modalBtn = document.createElement('button');
  modalBtn.classList.add('btn');
  modalBtn.classList.add('btn-primary');
  modalBtn.classList.add('btnm');
  modalBtn.setAttribute('type', 'button');
  modalBtn.setAttribute('data-bs-toggle', 'modal');
  modalBtn.setAttribute('data-bs-target', `#dogModal${dog.name}`);
  modalBtn.innerHTML = `Meer info over ${dog.name}`;

  const modal = new bootstrap.Modal(document.getElementById(`dogModal${dog.name}`), { focus: true, keyboard: true });
  modalBtn.addEventListener('click', e => {
    modal.toggle();
  });

  imgContainer.appendChild(cardImg);

  cardBody.appendChild(cardTitle);
  cardBody.appendChild(cardText);

  cardFooter.appendChild(modalBtn);

  card.appendChild(imgContainer);
  card.appendChild(cardBody);
  card.appendChild(cardFooter);

  container.appendChild(card);
};

const generateModal = (container, dog) => {
  const modal = document.createElement('div');
  modal.classList.add('modal');
  modal.classList.add('fade');
  modal.setAttribute('id', `dogModal${dog.name}`);
  modal.setAttribute('tabindex', '-1');
  modal.setAttribute('aria-labelledby', `dogModalLabel${dog.name}`);
  modal.setAttribute('aria-hidden', 'true');

  const modalDialog = document.createElement('div');
  modalDialog.classList.add('modal-dialog');
  modalDialog.classList.add('modal-dialog-scrollable');

  const modalContent = document.createElement('div');
  modalContent.classList.add('modal-content');

  const modalHeader = document.createElement('div');
  modalHeader.classList.add('modal-header');

  const title = document.createElement('h1');
  title.classList.add('modal-title');
  title.classList.add('fs-5');
  title.setAttribute('id', `dogModalLabel${dog.name}`);
  title.innerHTML = dog.name;

  const closeBtn = document.createElement('button');
  closeBtn.classList.add('btn-close');
  closeBtn.setAttribute('type', 'button');
  closeBtn.setAttribute('data-bs-dismiss', 'modal');
  closeBtn.setAttribute('aria-label', 'Close');

  modalHeader.appendChild(title);
  modalHeader.appendChild(closeBtn);

  const modalBody = document.createElement('div');
  modalBody.classList.add('modal-body');
  modalBody.setAttribute('id', `modalBody${dog.name}`);
  modalBody.innerHTML = dog.description;

  modalContent.appendChild(modalHeader);
  modalContent.appendChild(modalBody);

  modalDialog.appendChild(modalContent);

  modal.appendChild(modalDialog);

  container.appendChild(modal);
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
  const modalContainer = document.getElementById('modal-container');
  fetch(
    'http://127.0.0.1:5001/getRecommendation?' +
      new URLSearchParams({
        id: window.localStorage.getItem('referenceId'),
      })
  )
    .then(res => res.json())
    .then(data => {
      data.recommendations.forEach(dog => {
        generateModal(modalContainer, dog);
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
