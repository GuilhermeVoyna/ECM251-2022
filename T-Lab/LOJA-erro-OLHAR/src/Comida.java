public class Comida extends Produto {

    public final EnumCategoriaComida comida;
    public final EnumAlergicos alergicos;
    public final EnumPimenta EnumPimenta;
    
    public Comida(double preco, String nome, int quantidade, String descricao, EnumCategoriaComida comida,
            EnumAlergicos alergicos, EnumPimenta enumPimenta) {
        super(preco, nome, quantidade, descricao);
        this.comida = comida;
        this.alergicos = alergicos;
        EnumPimenta = enumPimenta;
    }







        
    }