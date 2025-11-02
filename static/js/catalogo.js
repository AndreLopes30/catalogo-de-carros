const filtro = document.getElementById('filtro');
const cards = document.querySelectorAll('#cards .card');
const lixo = document.getElementById("lixo")

filtro.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        const busca = filtro.value.toLowerCase().trim();

        cards.forEach(card => {
            const modelo = card.querySelector('.modelo').textContent.toLowerCase();
            const ano = card.querySelector('.ano')?.textContent.toLowerCase() || "";
            const preco = card.querySelector('.preco').textContent.toLowerCase();

            if (modelo.includes(busca) || ano.includes(busca) || preco.includes(busca)) {
                card.style.removeProperty('display');
            } 
            else {
                card.style.display = 'none';
            }
        });
    }
})

lixo.addEventListener("click", function(e) {
    e.preventDefault();
    filtro.value = '';
    cards.forEach(card => {
        card.style.removeProperty('display');
    });
});
