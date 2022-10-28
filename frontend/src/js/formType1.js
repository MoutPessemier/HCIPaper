const init = () => {
  const form = document.getElementById('form');
  const submitBtn = document.getElementById('submit');
  submitBtn.addEventListener('click', e => {
    e.preventDefault();
    const endTime = new Date().toString().split(' ')[4];
    // form.submit();
  });
};

window.onload = () => init();
