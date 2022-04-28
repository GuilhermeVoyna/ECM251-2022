public class Usuario {
    
    private String nome;
    private String itens;
    private Veiculos veiculos;

    public Usuario(String nome, String itens) {
        this.nome = nome;
        this.itens = itens;
        this.veiculos = new Veiculos(itens);
    }

    public String getNome() {
        return nome;
    }

    public String getItens() {
        return itens;
    }

    public void setItens(String itens) {
        this.itens = itens;
    }


    @Override
    public String toString() {
        return "Usuario [itens=" + itens 
        + ", nome=" + nome + "]";
    }

    public String Testar() {

        return veiculos.getId()+";"+veiculos.getTipo();
    }





    
}
