import java.util.concurrent.ThreadLocalRandom;

public class Sistema {
    public static void rodar(){
        //Usuario escolhe a jogada
        Jogada jogada1 = new Tesoura();
        //Sorteio da jogada para o PC
        Jogada jogada2 = sortearJogada();
        //Avaliação das jogadas
        String resultado = avaliaJogadas(jogada1, jogada2);
        //Exibição do resultado
        System.out.println("Resultado:" + resultado);
    }

    private static Jogada sortearJogada() {
        Jogada jogadas[] = new Jogada[5];
        jogadas[0] = new Pedra();
        jogadas[1] = new Papel();
        jogadas[2] = new Tesoura();
        jogadas[3] = new Spocke();
        jogadas[4] = new Lagarto();
        return jogadas[ThreadLocalRandom.current().nextInt(jogadas.length)];
    }

    private static String avaliaJogadas(Jogada jogada1, Jogada jogada2) {
        if(jogada1.verificarVenceu(jogada2))
            return jogada1.getArt();
        if(jogada2.verificarVenceu(jogada1))
            return jogada2.getArt();
        return "";
    }
}
