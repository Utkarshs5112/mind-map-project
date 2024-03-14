const colorToggle = document.getElementById('color-toggle');
const timeline = document.getElementById('timeline');

colorToggle.addEventListener('change', function() {
  if (this.checked) {
    timeline.style.backgroundColor = 'red';
  } else {
    timeline.style.backgroundColor = 'blue';
  }
});
