const getFormValueForQuestion = name => {
  const radios = document.getElementsByName(name);
  const radio = Array.from(radios).filter(radio => radio.checked)[0];
  const sliderValue = getSliderValueForQuestion(name) || 50;
  return { value: radio.value, weight: sliderValue };
};

const getSliderValueForQuestion = name => {
  const slider = document.getElementById(`${name}-slider`);
  if (slider) {
    try {
      return parseInt(slider.value);
    } catch (error) {
      console.log(`Error parsing slider value for question ${name}:: ${error}`);
    }
  }
};

const canSubmit = () => {
  let counter = 0;
  Array.from(document.getElementsByTagName('input')).forEach(el => {
    if (el.checked) {
      counter++;
    }
  });
  return counter === 10;
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
    const q6 = getFormValueForQuestion('q6');
    const q7 = getFormValueForQuestion('q7');
    const q8 = getFormValueForQuestion('q8');
    const q9 = getFormValueForQuestion('q9');
    const q10 = getFormValueForQuestion('q10');
    const endTime = new Date().toString().split(' ')[4];
    const startTime = window.localStorage.getItem('startTime');
    const body = {
      startTime,
      endTime,
      Q1: q1,
      Q2: q2,
      Q3: q3,
      Q4: q4,
      Q5: q5,
      Q6: q6,
      Q7: q7,
      Q8: q8,
      Q9: q9,
      Q10: q10,
      formType: window.localStorage.getItem('formType'),
    };
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    };
    fetch('http://127.0.0.1:5000/getId', options)
      .then(res => res.json())
      .then(data => {
        window.localStorage.setItem('referenceId', data.id);
        window.location.href = `/pages/suggestions.html`;
      })
      .catch(error => console.log('ERROR:: ', error));
  });
};

window.onload = init();
