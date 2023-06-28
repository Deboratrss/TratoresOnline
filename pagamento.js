let usouPix = false

function salvarDados(event) {
    event.preventDefault()
    let forme = document.getElementById('forme')
    const params = new URLSearchParams(window.location.search)
    const id = params.get('id')
    
    const nome = forme.nome.value
    const numero_cartao = forme.numero_cartao.value
    const data_validade = forme.data_validade.value
    const codigo_seguranca = forme.codigo_seguranca.value
    const parcelas = forme.parcelas.value

    if(nome && numero_cartao && data_validade && codigo_seguranca && parcelas){

        const body = {
            nome,
            numero_cartao,
            data_validade,
            codigo_seguranca,
            parcelas: new Number(parcelas)
        }

        fetch ('http://localhost:8000/informacoes_pagamento',{
            method: 'POST',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify(body)
        }).then(r => {
            if(r.status === 200) window.location.href = 'produto.html'
        })

    } else if (usouPix) {
        window.location.href = 'produto.html'
    }

}
function copiarPix(event){
    fetch(`http://localhost:8000/pagamento_pix`, {method:'GET'})
    .then(response => response.json()).then(
        response =>{
            navigator.clipboard.writeText(response[2][0]);
            console.log(response[2][0])

            const mensagem = document.getElementById('mensagem')
            mensagem.innerHTML = `
            <p class='sucesso'> PIX copiado com secesso!</p>
            `
            usouPix = true
        }
    )
}

document.addEventListener('DOMContentLoaded', () => {
    // pega o parametro da url
    const params = new URLSearchParams(window.location.search)
    const id = params.get('id')

    /*
        1 -> requisita os dados
        2 -> cria o elemento
        3 -> adiciona o elemento na tela
    */
  
    fetch(`http://localhost:8000/vendas/${id}`,{method: 'GET' })
    .then(response => response.json()).then(
        response => {
         console.log(response)
            const produto = document.getElementById('produto')
            produto.innerHTML = `
                <p>${response['Item']}</p>
                <p>${response['Preço unitário']}</p>
            `
        }
    )


    let forme = document.getElementById('forme')
    forme.addEventListener('submit', salvarDados)

    let buttonPix = document.getElementById('button_pix')
    buttonPix.addEventListener('click', copiarPix)
})