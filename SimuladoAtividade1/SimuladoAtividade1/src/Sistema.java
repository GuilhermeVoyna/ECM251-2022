public class Sistema {
    public void run(){

        Usuarios U1 = new Usuarios("U1", "123", "420@gmail.com");
        Conta conta1 = new Conta("1234", U1, 1000);

        Usuarios U2 = new Usuarios("U2", "111", "anime@gmail.com");
        Conta conta2 = new Conta("1234", U2, 250);

        Usuarios U3 = new Usuarios("U1", "543", "alow@gmail.com");
        Conta conta3 = new Conta("1234", U3, 3000);



        


    }
    public void pagamento(Conta contaRecebe,Double valor,String QRcode) {

        String [] destino= QRcode.split(";");
      

        contaRecebe.transferirDinheiro(valor, destino[1]);
            
    }
}