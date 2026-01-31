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