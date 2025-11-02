document.getElementById("form").addEventListener("submit", function(e) {
    let modelo = document.getElementById("modelo").value.trim();
    let ano = parseInt(document.getElementById("ano").value);
    let preco = parseFloat(document.getElementById("preco").value);

    if (modelo === "" || ano < 1900 || ano > 2025 || preco < 0) {
        e.preventDefault();
        Swal.fire({
            icon: 'error',
            title: 'Ops...',
            text: 'Preencha todos os campos corretamente.',
        });
    }
});


