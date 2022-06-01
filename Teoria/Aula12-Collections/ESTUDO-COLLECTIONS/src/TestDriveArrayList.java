import java.util.ArrayList;

public class TestDriveArrayList {
    public static void main(String[] args){

        ArrayList canetas = new ArrayList<Caneta>();

        canetas.add(new Caneta("Azul", 0.7));
        canetas.add(new Caneta("Vermelha", 1.0));
        
        //Metodo 1
        for(int i=0; i<canetas.size(); i++ ){
            System.out.println("Cor da caneta: "+((Caneta)canetas.get(i)).cor);
        }

        for(int i=0; i<canetas.size(); i++ ){
            System.out.println("Cor da caneta: "+canetas.get(i).getClass(1));
        }
        //Metodo 2
       //for (Caneta caneta : canetas) {
        //   System.out.println("Cor da caneta: "+caneta.cor);
       //}
        
    }
    
}
