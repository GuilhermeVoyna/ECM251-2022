public class Conta {

    private Usuario usuario;
    private String name;
    private String senha;


    public Conta( String name, String senha) {
        this.usuario = new Usuario();
        this.name = name;
        this.senha = senha;
    }


    public Usuario getUsuario() {
        return usuario;
    }

    
}
