const colorToggle = document.getElementById('color-toggle');
const timeline =  document.getElementById('contents');

colorToggle.addEventListener('change', function() {
  if (this.checked) {
    timeline.style.backgroundColor = 'grey';
    timeline.style.color='white';
    
  }
  else{
    timeline.style.backgroundColor = 'white';
    timeline.style.color ='black';
  }
});

function show(websiteNumber) {
  var iframes = document.querySelectorAll('iframe');
  for (var i = 0; i < iframes.length; i++) {
      if (i + 1 === websiteNumber) {
          iframes[i].classList.add('active');
      } else {
          iframes[i].classList.remove('active');
      }
  }
}

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


$(document).ready(function(){
  $('[data-toggle="popover"]').popover();
});

document.getElementById('btnSwitch').addEventListener('change',()=>{
  if (document.documentElement.getAttribute(('data-bs-theme') == 'dark')) {
      document.documentElement.setAttribute('data-bs-theme','light')
  }
  else {
      document.documentElement.setAttribute('data-bs-theme','dark')
  }
})

document.getElementById("startButton").addEventListener('click', () =>
{
      var link = document.getElementById("startButton").getAttribute("href")
      window.open(link)
}
)

// Function to fetch data from clues.json served by Flask
async function fetchData() {
  try {
      const response = await fetch('clues.json');
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error fetching data:', error);
  }
}

async function populateTable() {
  const jsonData = await fetchData();
  const tableBody = document.getElementById("table-body");
  jsonData.clues.forEach(clue => {
      const row = tableBody.insertRow();
      row.insertCell(0).textContent = clue.clue;
      row.insertCell(1).textContent = clue.date;
      row.insertCell(2).textContent = clue.category;
  });
}

populateTable();