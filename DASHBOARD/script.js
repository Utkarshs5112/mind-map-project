const colorToggle = document.getElementById('color-toggle');
const timeline =  document.getElementById('col');

colorToggle.addEventListener('change', function() {
  if (this.checked) {
    timeline.style.backgroundImage = 'none';
  } else {
    timeline.style.backgroundImage = '.css/images/mag3.png';
  }
});

  var popup = document.getElementById("popup");
  popup.style.display = (popup.style.display == "none") ? "block" : "none";
