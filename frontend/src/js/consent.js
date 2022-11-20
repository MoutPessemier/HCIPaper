const init = () => {
  const checkbox = document.getElementById('consent');
  const aBtn = document.getElementById('consent-btn');
  checkbox.addEventListener('change', e => {
    if (e.target.checked) {
      aBtn.setAttribute('aria-disabled', 'false');
      aBtn.classList.remove('disabled');
      aBtn.onclick = () => {
        const formType = Math.floor(Math.random() * 3) + 1;
        window.localStorage.setItem('formType', formType);
        const startTime = new Date().toString().split(' ')[4];
        window.localStorage.setItem('startTime', startTime);
        window.location.href = `/pages/formType${formType}.html`;
      };
    } else {
      aBtn.setAttribute('aria-disabled', 'true');
      aBtn.classList.add('disabled');
    }
  });
};

window.onload = () => init();
