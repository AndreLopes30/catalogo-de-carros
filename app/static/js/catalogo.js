if (!encontrado) {
    const msgExistente = document.getElementById('mensagem-erro');
    if (msgExistente) {
        msgExistente.remove();
    }
    
    const frase = document.createElement('p');
    frase.textContent = 'Nenhum carro encontrado';
    frase.id = 'mensagem-erro';
    frase.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: red;
        font-size: 24px;
        font-weight: bold;
        background-color: white;
        padding: 20px;
        border: 2px solid red;
        border-radius: 8px;
        z-index: 9999;
    `;
    document.body.appendChild(frase);
}

function confirmarExclusao(id, modelo) {
    console.log("Acionado exclusão para ID:", id);
    Swal.fire({
        title: 'Excluir ' + modelo + '?',
        text: "O veículo sairá do catálogo permanentemente!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d11a2a',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sim, excluir!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            const formulario = document.getElementById('delete-form-' + id);
            if (formulario) {
                formulario.submit();
            } else {
                console.error("Formulário não encontrado para o ID:", id);
            }
        }
    });
}