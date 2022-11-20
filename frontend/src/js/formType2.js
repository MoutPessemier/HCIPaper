const getFormValueForQuestion = name => {
  const radios = document.getElementsByName(name);
  const radio = Array.from(radios).filter(radio => radio.checked)[0];
  const sliderValue = getSliderValueForQuestion(name) || 50;
  return { value: radio.value, weight: sliderValue };
};

const getSliderValueForQuestion = name => {
  const slider = document.getElementById(`${name}-slider`);
  if (slider) {
    return slider.value;
  }
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
    const q1 = getFormValueForQuestion('q1');
    const q2 = getFormValueForQuestion('q2');
    const q3 = getFormValueForQuestion('q3');
    const q4 = getFormValueForQuestion('q4');
    const q5 = getFormValueForQuestion('q5');
    const endTime = new Date().toString().split(' ')[4];
    const startTime = localStorage.getItem('startTime');
    const body = {
      startTime,
      endTime,
      Q1: q1,
      Q2: q2,
      Q3: q3,
      Q4: q4,
      Q5: q5,
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

window.onload = init();
