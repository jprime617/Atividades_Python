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

vendas()