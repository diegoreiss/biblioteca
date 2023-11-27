const buttonAdicionarLivro = document.querySelector("#buttonAdicionarLivro");

const limparFormAdicionarLivro = () => {
  const camposForm = {
    "nome": document.querySelector("#formControlNomeLivro"),
    "autor": document.querySelector("#formControlAutorLivro"),
    "quantidade_estoque": document.querySelector("#formControlQuantidadeEmEstoqueLivro"),
    "paginas": document.querySelector("#formControlPaginasLivro")
  }

  for (const [key, value] of Object.entries(camposForm)) {
    value.value = "";
  }
}

buttonAdicionarLivro.addEventListener("click", (e) => {
  limparFormAdicionarLivro();
});
