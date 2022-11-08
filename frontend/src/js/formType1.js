const getFormValueForQuestion = name => {
  const radios = document.getElementsByName(name);
  const radio = Array.from(radios).filter(radio => radio.checked)[0];
  return radio.value;
};

const canSubmit = () => {
  let counter = 0;
  Array.from(document.getElementsByTagName('input')).forEach(el => {
    if (el.checked) {
      counter++;
    }
  });
  return counter === 5;
};

const init = () => {
  const submitBtn = document.getElementById('submit');
  const container = document.getElementById('container');
  container.addEventListener('change', e => {
    if (canSubmit()) {
      submitBtn.setAttribute('aria-disabled', 'false');
      submitBtn.classList.remove('disabled');
    } else {
      submitBtn.setAttribute('aria-disabled', 'true');
      submitBtn.classList.add('disabled');
    }
  });
  submitBtn.addEventListener('click', e => {
    const q1v = getFormValueForQuestion('q1');
    const q2v = getFormValueForQuestion('q2');
    const q3v = getFormValueForQuestion('q3');
    const q4v = getFormValueForQuestion('q4');
    const q5v = getFormValueForQuestion('q5');
    const endTime = new Date().toString().split(' ')[4];
    const startTime = localStorage.getItem('startTime');
    const body = {
      startTime,
      endTime,
      Q1: { value: q1v, weight: 50 },
      Q2: { value: q2v, weight: 50 },
      Q3: { value: q3v, weight: 50 },
      Q4: { value: q4v, weight: 50 },
      Q5: { value: q5v, weight: 50 },
    };
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    };
    // TODO: test end point
    fetch('', options)
      .then(res => {
        console.log(res);
        //TODO: set reference id in localStorage
        //document.localStorage.setAttribute('referenceId', res);
        window.location.href = `/pages/suggestions.html`;
      })
      .catch(res => console.log(res));
  });
};

window.onload = () => init();
