async function carregarClientes(somenteRisco = false) {

    const resp = await fetch(`/clientes?somente_risco=${somenteRisco}`);
    const clientes = await resp.json();

    const tabela = document.getElementById("tabela");
    tabela.innerHTML = "";

    clientes.forEach(c => {
        tabela.innerHTML += `
          <tr>
            <td>${c.cliente}</td>
            <td>${(c.probabilidade * 100).toFixed(0)}%</td>
            <td>${c.classe}</td>
            <td><button onclick='verDetalhes(${JSON.stringify(c)})'>Ver</button></td>
          </tr>
        `;
    });
}

function verDetalhes(cliente){
    let html = `<h3>${cliente.cliente}</h3>`;
    html += `<p><b>Classe:</b> ${cliente.classe}</p>`;
    html += `<p><b>Risco:</b> ${(cliente.probabilidade * 100).toFixed(0)}%</p>`;

    if(cliente.riscos.length){
        html += "<h4 style='color:#dc3545'>Fatores de Risco</h4><ul>";
        cliente.riscos.forEach(m => html += `<li>${m}</li>`);
        html += "</ul>";
    }

    if(cliente.protecao.length){
        html += "<h4 style='color:#198754'>Fatores de Proteção</h4><ul>";
        cliente.protecao.forEach(m => html += `<li>${m}</li>`);
        html += "</ul>";
    }

    document.getElementById("detalhes").innerHTML = html;
    document.getElementById("modal").style.display = "block";
}

function fecharModal(){
    document.getElementById("modal").style.display = "none";
}
