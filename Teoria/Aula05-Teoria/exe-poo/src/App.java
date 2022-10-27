public class App {
    public static void main(String[] args) throws Exception 
    {
        //Declara um objeto do tipo conta
        Conta minhaConta;
        //Instanciar um objeto do tipo conta
        minhaConta = new Conta();
        //Declarou e instanciou um objeto do tipo conta
        Conta outraConta = new Conta();

        minhaConta.saldo = 200.0;
        minhaConta.numero = 1234;
        outraConta.saldo = 150.00;
        outraConta.numero = 5678;

        System.out.println("Saldo na minha conta: ");
        minhaConta.visualizarSaldo();
        System.out.println("Saldo na outra conta: ");
        outraConta.visualizarSaldo();

        minhaConta.transferirDinheiro(-100, outraConta);

        System.out.println("Saldo na minha conta: ");
        minhaConta.visualizarSaldo();
        System.out.println("Saldo na outra conta: ");
        outraConta.visualizarSaldo();
    }
}
