const init = () => {
  const aBtn = document.getElementById('start-btn');
  aBtn.onclick = () => {
    const formType = Math.floor(Math.random() * 3) + 1;
    const startTime = new Date().toString().split(' ')[4];
    window.localStorage.setItem('startTime', startTime);
    window.location.href = `/formType${formType}.html`;
  };
};

window.onload = () => init();
