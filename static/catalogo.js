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

// pegar elementos
const sortBtn = document.getElementById("sortBtn");
const sortMenu = document.getElementById("sortMenu");

// abrir/fechar menu
sortBtn.addEventListener("click", () => {
  sortMenu.style.display = (sortMenu.style.display === "block") ? "none" : "block";
});

// fechar se clicar fora
document.addEventListener("click", (e) => {
  if (!sortBtn.contains(e.target) && !sortMenu.contains(e.target)) {
    sortMenu.style.display = "none";
  }
});

// capturar escolha
document.querySelectorAll("#sortMenu input").forEach((radio) => {
  radio.addEventListener("change", (e) => {
    const valor = e.target.value;
    console.log("Ordenar por:", valor);

    // aqui depois a gente chama a função que reordena os cards
    // tipo: ordenarCards(valor);
  });
});
