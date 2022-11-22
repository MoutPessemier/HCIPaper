const init = () => {
  fetch('http://127.0.0.1:5001/wakeUp')
    .then(res => res.json())
    .then(data => console.log('Backend Status:: ' + data.status))
    .catch(error => console.log('Backend Status:: ' + error));
};

window.onload = init();
