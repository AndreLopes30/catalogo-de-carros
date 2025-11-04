const filtro = document.getElementById('filtro');
const cards = document.querySelectorAll('#cards .card');
const lixo = document.getElementById("lixo")

filtro.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        const busca = filtro.value.toLowerCase().trim();
        let encontrado = false;

        cards.forEach(card => {
            const modelo = card.querySelector('.modelo').textContent.toLowerCase();
            const ano = card.querySelector('.ano')?.textContent.toLowerCase() || "";
            const preco = card.querySelector('.preco').textContent.toLowerCase();

            if (modelo.includes(busca) || ano.includes(busca) || preco.includes(busca)) {
                card.style.removeProperty('display');
                encontrado = true;
            } else {
                card.style.display = 'none';
            }
        });
        if (!encontrado) {
            const frase = document.createElement('p');
            frase.textContent = 'Nenhum carro encontrado';
            frase.id = 'mensagem-erro';
            frase.style.position = 'fixed';
            frase.style.top = '50%';
            frase.style.left = '50%';
            frase.style.transform = 'translate(-50%, -50%)';
            frase.style.color = 'red';
            frase.style.fontSize = '24px';
            frase.style.fontWeight = 'bold';
            frase.style.backgroundColor = 'white';
            frase.style.padding = '20px';
            frase.style.border = '2px solid red';
            frase.style.borderRadius = '8px';
            frase.style.zIndex = '9999';
            document.body.appendChild(frase);
    }
}
});


lixo.addEventListener("click", function(e) {
    e.preventDefault();
    filtro.value = '';
    cards.forEach(card => {
        card.style.removeProperty('display');
    });
});
