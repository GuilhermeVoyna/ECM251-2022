import JOGOS.EnumGenero;

public class Jogo {
    public final String nome;
    public final EnumGenero genero;
    // adicionar uma lista com linguas disponiveis
    public float preco;

    public Jogo(String nome, EnumGenero genero, float preco) {
        this.nome = nome;
        this.genero = genero;
        this.preco = preco;
    }


     public String getNome() {
        return nome;
    }
    public EnumGenero getGenero() {
        return genero;
    }
    public float getPreco() {
        return preco;
    }


    @Override
    public String toString() {
        return "Jogo [nome=" + nome + ", genero=" + genero + ", preco=" + preco + "]";
    }


}

    
