const buttonAdicionarLivro = $("#buttonAdicionarLivro");

const limparFormAdicionarLivro = () => {
  const camposForm = {
    "nome": $("#formControlNomeLivro"),
    "autor": $("#formControlAutorLivro"),
    "quantidade_estoque": $("#formControlQuantidadeEmEstoqueLivro"),
    "paginas": $("#formControlPaginasLivro")
  }

  for (const [key, value] of Object.entries(camposForm)) {
    value.val("");
  }
}

buttonAdicionarLivro.on("click", (e) => {
  for (let elements of [$("#formControlAutorLivro"), $("#formControlGeneroLivro")]) {
    elements.selectize({
      sortField: "text",
    });
  }
  limparFormAdicionarLivro();
});
