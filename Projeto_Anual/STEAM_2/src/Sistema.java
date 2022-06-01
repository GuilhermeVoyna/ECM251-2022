import JOGOS.EnumGenero;

public class Sistema {

    public static void run(){
        System.out.println("INICIADO\n");

        Conta c1 = new Conta( "name", "senha");
        Conta c2 = new Conta( "name", "senha");

        System.out.println(c1.getUsuario());
        System.out.println(c2.getUsuario());

        System.out.println(c1.getUsuario().getCarteira());
        System.out.println(c2.getUsuario().getCarteira());

        System.out.println(c1.getUsuario().getCarteira().getSaldo());
        c1.getUsuario().getCarteira().setSaldo(1000);
        System.out.println(c1.getUsuario().getCarteira().getSaldo());
        System.out.println(c2.getUsuario().getCarteira().getSaldo());

        


        System.out.println();
        
        System.out.println("\nFINALIZADO");
    }

}
