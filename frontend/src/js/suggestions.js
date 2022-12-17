import * as bootstrap from 'bootstrap';

const dogIds = {
  Ara: '1gl06jI6yeRuq9GQ8Rs3hguHu1esxf07p',
  Bailey: '1rGHvLGfgdmZ8lBMnJLcxKaiOk6IgsN_j',
  Bayka: '1nhlIoOcxW7y5mSE7J02oaEqjTnyvicJr',
  Bessie: '1XIZOTKprHcLit5UK26LLZHFw74HvWA8B',
  Bibi: '1W8TH3fn1EqJNFsiJrsH5PqoxIScqGaA9',
  Biegel: '1INwHCu6Pul6W3dk13eoqnTSyNU1oA8e4',
  Boelie: '1E_s2_-udropNhRxagnQaTkd7XjDk5YIh',
  Dario: '1NOx1VIAriU_bLRxSqCy16wijlT39xZ7h',
  Didi: '1DzfrRQDo0jQ9pO8O-iwLitOidUVmpi2j',
  Henkie: '13EliVTo8aJHOq691NsfjuE4U8H4QEmXn',
  Herman: '1Q70hOl41YUbpOfgEqPxtjMd28A7sl1yt',
  Imara: '1OLblcDKYLzseQzkKpjn6jaryYDBG9-ml',
  Junior: '1UOPMJpCCx6z5oli3ph7AOnJ-nvLpaifi',
  Kita: '1Vh3IY2cQPH_z06mdvsdY2sqUmfANAd4Y',
  Max: '14lD754dc8QadkQLYzzdciXXccSvs9Al0',
  Mini: '17KGW-NJS7aRKaSX-X-ulNVmB6Wzgncem',
  Molly: '1sycVfzlMh_-7SsTae4e_yvk-xPmqVkX8',
  Rita: '1ewFvykzoAqcOVbu4LjSCFNY2K-0pHBn0',
  Rosa: '1ppFmgKin77_X4ixls9GWw8yV9AybsfmI',
  Ryna: '1NYa-GjsUssc2a-hrLI3rcqehpEwLtCOu',
  Skippy: '1rvfDOsitH05_-Ueigw8UhQfteKzBTAfz',
  Sky: '1G4plAIZyJur5LYxe3yraz66i50pAWaOR',
  Storm: '1iNJpTANHJKm-X4V8BGXUu02Fm6f9Ts9I',
  Thor: '11Lt2SKW1usQhZVhmH4vU3JOjD3Cdo0Jy',
  Tipsie: '1-mQ4LWNg5ICwLEGdvP21I0JCWm3AE7yR',
  Vicky: '1QvFXeL9z59m9stQ2Qv2YFqb7aNrpQ5Ni',
  Zita: '1GTvFxdFuZ1j95WysZL16g4Uful4pCGfc',
  Zora: '1eLKPY7xLCFnDlPxifA-mDnuC0TdvmvTC',
  Zuma: '1zpqUR6NFUqgDSHLjvLfaOwbZawivk84U',
};

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
  cardImg.setAttribute('src', `https://drive.google.com/uc?export=view&id=${dogIds[`${dog.name}`]}`);

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

const getOpenQuestionValue = name => {
  const txtarea = document.getElementById(name);
  return txtarea.value || '';
};

const init = () => {
  const cardsContainer = document.getElementById('cards-container');
  const modalContainer = document.getElementById('modal-container');
  // fetch(
  //   'http://127.0.0.1:3490/fmmi9/getRecommendation?' +
  //     new URLSearchParams({
  //       id: window.localStorage.getItem('referenceId'),
  //     })
  // )
  fetch(
    'https://augment.cs.kuleuven.be/fmmi9/getRecommendation?' +
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
      const a1 = document.getElementById('dog1');
      a1.innerHTML = data.recommendations[0].name;
      a1.setAttribute('href', data.recommendations[0].link);
      a1.classList.add('inline');
      const a2 = document.getElementById('dog2');
      a2.innerHTML = data.recommendations[1].name;
      a2.setAttribute('href', data.recommendations[1].link);
      a2.classList.add('inline');
      const a3 = document.getElementById('dog3');
      a3.innerHTML = data.recommendations[2].name;
      a3.setAttribute('href', data.recommendations[2].link);
      a3.classList.add('inline');
      const a4 = document.getElementById('dog4');
      a4.innerHTML = data.recommendations[3].name;
      a4.setAttribute('href', data.recommendations[3].link);
      a4.classList.add('inline');
    })
    .catch(err => console.log(err));

  const backBtn = document.getElementById('back');
  backBtn.addEventListener('click', e => {
    window.localStorage.setItem('startTime', new Date().toString().split(' ')[4]);
    const formType = window.localStorage.getItem('formType');
    window.location.href = `/pages/formType${formType}.html`;
  });
  const thanksP = document.getElementById('thanks');
  const submitBtn = document.getElementById('submit');
  const checkDogs = document.getElementById('check-dogs');
  submitBtn.addEventListener('click', e => {
    const finalTime = new Date().toString().split(' ')[4];
    const body = {
      finalTime,
      ID: window.localStorage.getItem('referenceId'),
      Q1: getSliderValueForQuestion(1),
      Q2: getSliderValueForQuestion(2),
      Q3: getSliderValueForQuestion(3),
      openVraag: getOpenQuestionValue('txtarea'),
    };
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    };
    //fetch('http://127.0.0.1:3490/fmmi9/giveResearch', options)
    fetch('https://augment.cs.kuleuven.be/fmmi9/giveResearch', options)
      .then(res => res.json())
      .then(data => {
        submitBtn.classList.add('hidden');
        backBtn.classList.remove('hidden');
        thanksP.classList.remove('hidden');
        checkDogs.classList.remove('hidden');
      })
      .catch(err => console.log(err));
  });
};

window.onload = init();
