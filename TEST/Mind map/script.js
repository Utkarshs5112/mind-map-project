const colorToggle = document.getElementById('color-toggle');
const timeline =  document.getElementById('contents');

colorToggle.addEventListener('change', function() {
  if (this.checked) {
    timeline.style.backgroundColor = 'black';
    timeline.style.Color = 'white';

  } else {
    timeline.style.backgroundColor = 'none';
    timeline.style.color='black';
  }
});

  // Get the button and popup message
var button = document.getElementById("myButton");
var popup = document.getElementById("popupMsg");

// Function to show the popup
function showPopup() {
  popup.style.display = "block";
}

// Function to hide the popup
function closePopup() {
  popup.style.display = "none";
}

// Event listener for button click
button.addEventListener("click", showPopup);


const popover = new bootstrap.Popover('.popover-dismiss', {
  trigger: 'focus'
})