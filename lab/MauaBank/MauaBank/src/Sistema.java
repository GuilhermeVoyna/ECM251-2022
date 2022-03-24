public class Sistema {
    public void run(){

    Cliente cliente = new Cliente("NANDO", "1234", "alo@maua.br");
        Conta conta = new Conta(cliente,1234);
        System.out.println(conta);
    }
}
