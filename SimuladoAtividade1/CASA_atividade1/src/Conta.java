public class Conta {
    //Atributos da nossa classe

    private Usuario usuario;
    private String numero;
    private double saldo;

    //Construtor
    public Conta(String numero, Usuario usuario,Double saldo){

        this.usuario=usuario;
        this.numero = numero;
        this.saldo = saldo;
    }


    //Métodos da classe
    public String getNumero() {
        return numero;
    }
    public Usuario getUsuario() {
        return usuario;
    }

    public String visualizarSaldo(){
        return String.format("R$%.2f", saldo);
    }

    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }

    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }

    public boolean transferirDinheiro(double valor, Conta destino){
        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }

}