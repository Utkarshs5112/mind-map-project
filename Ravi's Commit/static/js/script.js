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



