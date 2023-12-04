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

const criarEmprestimoStatus = Number($('#criarEmprestimoStatus').html());
const devolverLivroEmprestadoStatus = Number($('#devolverLivroEmprestadoStatus').html());

switch (criarEmprestimoStatus) {
  case 200:
    showToast("success", "Realizar Empréstimo", "Empréstimo realizado com sucesso!"); break;
  case 400:
    showToast("danger", "Realizar Empréstimo", "Talvez você já tenha esse empréstimo!"); break;
  default:
    break;
}

switch (devolverLivroEmprestadoStatus) {
  case 200:
    showToast("success", "Realizar Devolução", "Devolução realizada com sucesso!"); break;
  case 400:
    showToast("danger", "Realizar Devolução", "Talvez você já tenha devolvido esse livro!"); break;
  default:
    break;
}