const buttonAdicionarLivro = $("#buttonAdicionarLivro");
const buttonCriarAluno = $("#buttonCriarAluno");


const limparFormAdicionarAluno = () => {
  const camposForm = {
    "nome": $("#formControlNomeAluno"),
    "email": $("#formControlEmailAluno"),
    "senha": $("#formControlSenhaAluno")
  }

  for (const [key, value] of Object.entries(camposForm)) {
    value.val("");
  }
}


const limparFormAdicionarLivro = () => {
  const camposForm = {
    "nome": $("#formControlNomeLivro"),
    "quantidade_estoque": $("#formControlQuantidadeEmEstoqueLivro"),
    "paginas": $("#formControlPaginasLivro"),
  }

  for (const [key, value] of Object.entries(camposForm)) {
    value.val("");
  }

  $('#formControlAutorLivro')[0].selectize.clear();
  $('#formControlGeneroLivro')[0].selectize.clear();

  let newInputFileLivro = `<input class="form-control" name="imagem" type="file" accept="image/png, image/jpeg" id="formControlImagemLivro">`
  $("#formControlImagemLivro").replaceWith(newInputFileLivro);
}

buttonCriarAluno.on("click", (e) => {
  limparFormAdicionarAluno();
});

buttonAdicionarLivro.on("click", (e) => {
  for (let elements of [$("#formControlAutorLivro"), $("#formControlGeneroLivro")]) {
    elements.selectize({
      sortField: "text",
    });
  }
  limparFormAdicionarLivro();
});

$("#buttonAdicionarAutor").on("click", (e) => {
  $("#formControlNomeAutor").val("");
});

$("#buttonAdicionarGenero").on("click", (e) => {
  $("#formControlNomeGenero").val("");
});

const showToast = (color, title, body) => {
  $("#myToastContainer").append(`
    <div class="myOwnToast toast text-bg-${color}" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="toast-header">
        <strong class="me-auto">${title}</strong>
        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
      <div class="toast-body">
      ${body}
      </div>
    </div>
  `);

  $(".myOwnToast").toast("show");
}

const quantidadeAutores = Number($(`input[name="quantidadeAutores"]`).val());
const quantidadeGeneros = Number($(`input[name="quantidadeGeneros"]`).val());

const criarGeneroStatus = Number($("#criarGeneroStatus").html());
const criarAutorStatus = Number($("#criarAutorStatus").html());
const criarLivroStatus = Number($("#criarLivroStatus").html());
const criarAlunoStatus = Number($("#criarAlunoStatus").html());

if (!quantidadeAutores || !quantidadeGeneros) {
  showToast("danger", "Adicionar Livro", "Foi encontrado uma dependência de registros de autores e gêneros! <br> Não será possível adicionar um livro.");
}

switch (criarGeneroStatus) {
  case 200:
    showToast("success", "Adicionar Gênero", "Gênero adicionado com sucesso!"); break;
  case 400:
    showToast("danger", "Adicionar Gênero", "CONFLITO!<br>Campo vazio ou gênero já existente!"); break;
  default:
    break;
}

switch (criarAutorStatus) {
  case 200:
    showToast("success", "Adicionar Autor", "Autor adicionado com sucesso!"); break;
  case 400:
    showToast("danger", "Adicionar Autor", "CONFLITO!<br>Campo vazio ou autor já existente!"); break;
  default:
    break;
}

switch (criarLivroStatus) {
  case 200:
    showToast("success", "Adicionar Livro", "Livro adicionado com sucesso!"); break;
  case 400:
    showToast("danger", "Adicionar Autor", "CONFLITO!<br>Campos vazios ou livro já existente!"); break;
  default:
    break;
}

switch (criarAlunoStatus) {
  case 200:
    showToast("success", "Adicionar Aluno", "Aluno adicionado com sucesso!"); break;
  case 400:
    showToast("danger", "Adicionar Aluno", "CONFLITO!<br>Campos vazios, nome de usuário existente ou email existente!"); break;
  default:
    break;
}
