alert("Vamos jogar um Jogo, O número Secreto!\nBoa sorte!");

let numeroSecreto = Math.floor(Math.random() * 100 + 1);

console.log(numeroSecreto);

var resposta = prompt("De 1 a 100 qual é o número secreto?");


console.log("A sua resposta foi " + resposta);

    for( let ntentativas = 10; ntentativas >= 0;  ntentativas --) {

       console.log( "Entrou no for: " + ntentativas);

        if (resposta < 1 || resposta > 100){
        alert("ATENÇÃO - Informe apenas números entre 1 e 100!");
        }

        else if (numeroSecreto == resposta){
            alert("Parabéns você acertou!");
            break;
        }
        else if (resposta < numeroSecreto){
            alert("Tente um número MAIOR, você ainda tem " + ntentativas + " tentativas."); 
        }
        else {
            alert("Tente um número MENOR você ainda tem " + ntentativas + " tentativas.");
        } 
        var resposta = prompt("Informe novamente um número entre 0 e 100.");
    }

alert("Game Over, até a Próxima");

console.log( "Saiu do for: " + ntentativas);