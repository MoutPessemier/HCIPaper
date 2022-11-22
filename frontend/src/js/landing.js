const init = () => {
  fetch('http://127.0.0.1:5001/wakeUp/')
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
};

window.onload = init();
