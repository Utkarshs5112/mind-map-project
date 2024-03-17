function showSignUp() {
    document.getElementById("loginForm").style.display = "none";
    document.getElementById("signupForm").style.display = "block";
  }

  function showLogin() {
    document.getElementById("signupForm").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
  }

  let toggle = document.getElementById('darkmode')
  let para = document.getElementById('desc')
  let para1 = document.querySelector('.section')
  let isDark = false;

  toggle.addEventListener('click', () => {
    if(isDark === false)
    {
        toggle.style.backgroundColor = "black"
        toggle.style.color = "white"
        toggle.textContent = "BLACK"
        para1.style.backgroundColor = "black"
        para.style.backgroundColor = "black"
        para.style.color = "white"
        isDark = true;
    }
    else if(isDark === true)
    {
        toggle.textContent = "WHITE"
        toggle.style.backgroundColor = "white"
        toggle.style.color = "black"
        para1.style.backgroundColor = "white"
        para.style.backgroundColor = "white"
        para.style.color = "black"
        isDark = false;
    }
  });