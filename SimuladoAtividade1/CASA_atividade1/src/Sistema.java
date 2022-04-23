public class Sistema {
    public void run(){


        
        Usuario U1 = new Usuario("U1", "123", "420@gmail.com");
        Conta conta1 = new Conta("123", U1, 1000.0);

        Usuario U2 = new Usuario("U2", "111", "anime@gmail.com");
        Conta conta2 = new Conta("111", U2, 250.0);

        Usuario U3 = new Usuario("U3", "543", "alow@gmail.com");
        Conta conta3 = new Conta("543", U3, 3000.0);
        

        System.out.println(conta1);
        System.out.println(conta2);
        System.out.println(conta3);


        String QRC1=conta1.QRcode(250); // tranferir para conta
        conta2.pagamento(QRC1, conta1);
        conta3.pagamento(QRC1, conta1);
        conta2.pagamento(QRC1, conta1);
        String QRC2=conta2.QRcode(1000);
        conta3.pagamento(QRC2, conta2);


       System.out.println("\n----\ntentando transferir\n----\n");

       System.out.println(conta1);
       System.out.println(conta2);
       System.out.println(conta3);

       

    }
//--------------------------------------------------------------------------------------------------------------------------------------------------


    
}