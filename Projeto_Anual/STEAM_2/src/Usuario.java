public class Usuario {
    private Carteira carteira;
    private Biblioteca biblioteca;


    public Usuario() {
        this.carteira = new Carteira();
        this.biblioteca=new Biblioteca();
    }

    public Carteira getCarteira() {
        return carteira;
    }

    

   
    
}
