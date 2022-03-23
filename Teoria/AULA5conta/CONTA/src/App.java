public class App {
    public static void main(String[] args) throws Exception {
        //Declara um objeto do tipo Conta
        Conta minhaConta;
        //Instanciar um objeto do tipo Conta
        minhaConta = new Conta();
        //Declarou e instanciou um objeto do tipo Conta
        Conta outraConta = new Conta();

        minhaConta.saldo = 200.0;
        minhaConta.numero = 1234;
        outraConta.saldo = 150.0;
        outraConta.numero = 5678;

        outraConta.visualizarSaldo();
        minhaConta.visualizarSaldo();

        minhaConta.transferirDinheiro(-1000, outraConta);
        minhaConta.visualizarSaldo();
        outraConta.visualizarSaldo();
    }
}