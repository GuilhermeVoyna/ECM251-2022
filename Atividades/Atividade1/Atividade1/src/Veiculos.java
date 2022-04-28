import java.util.concurrent.ThreadLocalRandom;

public class Veiculos {

    

    String tipo;
    Integer id;
   
    
    
 


    public Veiculos(String tipo) {
        this.tipo = tipo;
        this.id = ThreadLocalRandom.current().nextInt(10000, 100000); // aleatorio de 1000 ate 9999;;
    }


    @Override
    public String toString() {
        return "Veiculos [id=" + id + ", tipo=" + tipo + "]";
    }


    public String getTipo() {
        return tipo;
    }


    public void setTipo(String tipo) {
        this.tipo = tipo;
    }


    public int getId() {
        return id;
    }



    
}
