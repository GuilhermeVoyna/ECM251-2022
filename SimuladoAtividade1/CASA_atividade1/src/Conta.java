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

    public String toString() {
        return ("Usuario: " + this.usuario.getNome() + "\nID: " + this.numero + "\nSaldo: " + this.saldo + "\n");
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
        if(!sacar(valor)){
            System.out.println("SALDO insuficiente");
            return false;
        } 
        if(!destino.depositar(valor)) return false;
        return true;
    }

    public String QRcode(double valor){
            
        
        String  idConta  = Conta.this.getNumero();//pegar id conta pagante

        String nome = Conta.this.getUsuario().getNome();// pega o nome do que vai receber

       return  idConta+";"+nome+";"+valor;
       

    }

    public void pagamento(String QRcode,Conta recebe) {

        String [] destino= QRcode.split(";");  
        Double valor = Double.parseDouble(destino[2]);
        
       

        boolean QRCver=verificarQRC(QRcode,recebe);//verifica o qrcode
        if(QRCver){
        boolean saldo = Conta.this.transferirDinheiro(valor, recebe); // verifica o saldo caso o qrc seja aprovado
            if(saldo){
                System.out.println("APROVADO");
        }
            else System.out.println("Reprovado");
        }
        

        
    }

    private boolean verificarQRC(String QRcode,Conta recebe) {

        String [] destino= QRcode.split(";");     
          //destino[0]// id Conta pagante 
         // destino[1] // Conta que ira receber o dinheiro 
         //destino[2]// valor a ser pago 

        if(destino[0].equals(recebe.getNumero())&&destino[1].equals(recebe.getUsuario().getNome())){
            System.out.println("QRC verificado");
            return true;
        }
        System.out.println("ERRO no QRC");
        return false;
    }

}