document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('form');
  const lojaSelect = document.getElementById('lojaSelect');
  const cargoSelect = document.getElementById('cargoSelect');
  const mensagemRetorno = document.getElementById('mensagemRetorno');
  const formularioCompleto = document.getElementById('formularioCompleto');

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    console.log("Botão foi criado!")

    const loja = lojaSelect.value;
    const cargo = cargoSelect.value;

    if (!loja || !cargo) {
      mensagemRetorno.textContent = 'Por favor, selecione loja e cargo.';
      mensagemRetorno.style.color = 'red';
      return;
    }

    mensagemRetorno.innerHTML = `
      <strong>Loja:</strong> ${loja}<br>
      <strong>Cargo:</strong> ${cargo}<br>
      <span style="color:green">Dados recebidos! Pronto para próxima etapa.</span>
    `;

    formularioCompleto.style.display = 'block';
    // opcional: ocultar o formulário anterior
    // form.style.display = 'none';
  });
});

