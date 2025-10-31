const filtro = document.getElementById('filtro');
const cards = document.querySelectorAll('#cards .card');

filtro.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        const busca = filtro.value.toLowerCase().trim();

        cards.forEach(card => {
            const modelo = card.querySelector('.modelo').textContent.toLowerCase();
            const ano = card.querySelector('.ano').textContent.toLowerCase();
            const preco = card.querySelector('.preco').textContent.toLowerCase();
            if (modelo.includes(busca)) {
                card.style.display = 'block';
            } 
            else if (ano.includes(busca)) {
                card.style.display = 'block';
            } 
            else if (preco.includes(busca)) {
                card.style.display = 'block';
            } 
            else {
                card.style.display = 'none';
            }
        });
    }
});

