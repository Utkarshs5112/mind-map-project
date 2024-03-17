document.getElementById('btnSwitch').addEventListener('change',()=>{
    if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
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

document.addEventListener('DOMContentLoaded', function() {
    var toggleSwitch = document.getElementById('color-toggle');
    var imageContainer = document.querySelector('.col-sm-10');

    toggleSwitch.addEventListener('change', function() {
        if (toggleSwitch.checked) {
            imageContainer.style.backgroundImage = "url('./images/blackboard.png')";
        } else {
            imageContainer.style.backgroundImage = "url('./images/whiteboard.png')";
        }
    });
});


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


