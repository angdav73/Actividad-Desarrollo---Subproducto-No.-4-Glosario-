// ======================================
// BUSCADOR
// ======================================

const buscador = document.getElementById("buscador");

buscador.addEventListener("input", function () {

    const texto = buscador.value.toLowerCase();

    const tarjetas = document.querySelectorAll(".card");

    tarjetas.forEach(function (tarjeta) {

        const termino = tarjeta.dataset.termino;

        if (termino.includes(texto)) {

            tarjeta.style.display = "block";

        } else {

            tarjeta.style.display = "none";

        }

    });

});



// ======================================
// FILTRO POR CATEGORÍA
// ======================================

function filtrarCategoria(categoria) {

    const tarjetas = document.querySelectorAll(".card");

    tarjetas.forEach(function (tarjeta) {

        if (
            categoria === "Todos" ||
            tarjeta.dataset.categoria === categoria
        ) {

            tarjeta.style.display = "block";

        } else {

            tarjeta.style.display = "none";

        }

    });

}



// ======================================
// MODAL
// ======================================

function mostrarEjemplo(termino, ejemplo, fuente) {

    document.getElementById("modal-titulo").textContent = termino;

    document.getElementById("modal-ejemplo").textContent = ejemplo;

    document.getElementById("modal-fuente").textContent = fuente;

    document.getElementById("modal").style.display = "flex";

}


function cerrarModal() {

    document.getElementById("modal").style.display = "none";

}



// ======================================
// CERRAR MODAL AL HACER CLIC AFUERA
// ======================================

window.onclick = function(event) {

    const modal = document.getElementById("modal");

    if (event.target === modal) {

        modal.style.display = "none";

    }

}