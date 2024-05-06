let pButton = document.getElementById('news-check-button')
pButton.addEventListener('click', show_loading)

function show_loading(){
        if (document.getElementById('news-input-area').value.trim() == ''){
            return ;
        }
    document.getElementById('loader').style.display = 'flex'
}