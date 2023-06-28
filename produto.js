function home(event){

   window.location.href = 'index.html' 
}

document.addEventListener('DOMContentLoaded', () => {

    const concluir = document.getElementById('Finalizar')
    concluir.addEventListener('click', home)    

})