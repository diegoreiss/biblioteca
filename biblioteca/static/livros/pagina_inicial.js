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

const showToast = (color, title, body) => {
  const myToast = $("#myToast");

  if (myToast) {
    myToast.remove();
  }

  $("body").append(`
  <div id="myToast" class="toast-container position-fixed bottom-0 end-0 p-3">
    <div id="liveToast" class="toast text-bg-${color}" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="toast-header">
        <strong class="me-auto">${title}</strong>
        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
      <div class="toast-body">
      ${body}
      </div>
    </div>
  </div>
  `);

  const toastLiveExample = $("#liveToast");
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
  toastBootstrap.show();
}


const quantidadeAutores = Number($(`input[name="quantidadeAutores"]`).val());
const quantidadeGeneros = Number($(`input[name="quantidadeGeneros"]`).val());

if (!quantidadeAutores || !quantidadeGeneros) {
  showToast("danger", "Adicionar Livro", "Sem autores e gêneros encontrados! <br> Não será possível adicionar um livro.");
}
