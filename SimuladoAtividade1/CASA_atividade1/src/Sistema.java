public class Sistema {
    public void run(){


        
        Usuario U1 = new Usuario("U1", "123", "420@gmail.com");
        Conta conta1 = new Conta("1234", U1, 1000.0);
        Usuario U2 = new Usuario("U2", "111", "anime@gmail.com");
        Conta conta2 = new Conta("1234", U2, 250.0);

        Usuario U3 = new Usuario("U1", "543", "alow@gmail.com");
        Conta conta3 = new Conta("1234", U3, 3000.0);

        
        QRcode(conta1, conta2, 10);
            


    }


    public void pagamento(Conta contaRecebe,Double valor,String QRcode) {

        String [] destino= QRcode.split(";");
        String d = destino[1];

        contaRecebe.transferirDinheiro(valor,(Conta) d);
            
    }

    public String QRcode(Conta nContaPagante, Conta Ureceber, double valor){
            
        
        String  idConta  = nContaPagante.getNumero();//pegar id conta
        String nome = Ureceber.getUsuario().getNome();

    
       return  idConta+";"+nome+";"+valor;
    }
}