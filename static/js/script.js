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




