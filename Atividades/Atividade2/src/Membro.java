public abstract class Membro implements Interface {
    private String usuario,email,funcao;

    public Membro(String usuario, String email, String funcao) {
        this.usuario = usuario;
        this.email = email;
        this.funcao = funcao;
    }

    public String getUsuario() {
        return usuario;
    }

    public String getEmail() {
        return email;
    }

    public String getFuncao() {
        return funcao;
    }
    String horario(){
        return Sistema.getHorario();
    }

    @Override
    public String toString() {
        return "Membro [email=" + email + ", usuario=" + usuario + ", funcao=" + funcao+"]";
    }

    
}
