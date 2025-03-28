function vendas() {
    meta = 20000;
    vendas = 25000;

    if (vendas < meta) {
        console.log("Meta não atingida");
    }else {
        if (vendas > meta * 2) {
            bonus = 0.07 * vendas
        }else {
            bonus = 0.03 * vendas
        }
    console.log(`Seu bonus foi de R$${bonus}`)
    }
}

function categorias() {
    categoria = Math.floor(Math.random() * 5) + 1;
    preco = 0

    if (categoria == 1) {
        preco = 10
    }else if (categoria == 2) {
        preco = 18
    }else if (categoria == 3) {
        preco = 23
    }else if (categoria == 4) {
        preco = 26
    }else if (categoria == 5) {
        preco = 31
    }else{
        return console.log("Categoria invalida")
    }

    console.log(`O preço do produto é R$:${preco}`)
}

// vendas()
categorias()