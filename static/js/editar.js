document.addEventListener("DOMContentLoaded", function() {
    const formEditar = document.getElementById("form-editar");
    const imagemInput = document.getElementById("imagem");
    const imagePreview = document.getElementById("image-preview");
    const btnSalvar = document.getElementById("btn");
    const btnCancelar = document.querySelector(".btn-cancelar");

    formEditar.addEventListener("submit", function(e) {
        let modelo = document.getElementById("modelo").value.trim();
        let ano = parseInt(document.getElementById("ano").value);
        let preco = document.getElementById("preco").value.trim();
        let imagem = document.getElementById("imagem").value.trim();

        if (modelo === "" || ano < 1900 || ano > 2026 || preco === "" || imagem === "") {
            e.preventDefault();
            Swal.fire({
                icon: 'error',
                title: 'Ops...',
                text: 'Preencha todos os campos corretamente.',
                confirmButtonColor: '#FFA500'
            });
            return;
        }

        btnSalvar.classList.add("loading");
        btnSalvar.textContent = "Salvando...";
    });

    if (imagemInput.value) {
        imagePreview.classList.add("visible");
    }

    imagemInput.addEventListener("input", function() {
        const url = this.value.trim();
        
        if (url) {
            const img = new Image();
            img.onload = function() {
                imagePreview.src = url;
                imagePreview.classList.add("visible");
            };
            img.onerror = function() {
                imagePreview.classList.remove("visible");
            };
            img.src = url;
        } else {
            imagePreview.classList.remove("visible");
        }
    });

    let formChanged = false;
    const inputs = document.querySelectorAll("#form-editar input");
    
    inputs.forEach(input => {
        input.addEventListener("change", () => {
            formChanged = true;
        });
    });

    btnCancelar.addEventListener("click", function(e) {
        if (formChanged) {
            e.preventDefault();
            const targetUrl = this.href;
            Swal.fire({
                title: 'Descartar alterações?',
                text: "As alterações não salvas serão perdidas!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Sim, descartar',
                cancelButtonText: 'Continuar editando'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = targetUrl;
                }
            });
        }
    });
});