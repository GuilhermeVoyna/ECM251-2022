public class Atividade1 {//20.00089-8
                         //Guilherme Martins
    public static void run(){
        Usuario u1 = new Usuario("Valter", "Carro");
        System.out.println(u1.Testar()+u1.getNome());
        Usuario u2 = new Usuario("Leo", "Moto");
        System.out.println(u2.Testar()+u2.getNome());

        troca(u1,u2);
    }

    public static void troca(Usuario u1,Usuario u2){
        String Iu1 = u1.getItens();
        String Iu2 = u2.getItens();

        u2.setItens(Iu1);
        System.out.println(u2.Testar()+u2.getNome());
        u1.setItens(Iu2);
        System.out.println(u1.Testar()+u1.getNome());
    }
}
