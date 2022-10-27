import java.util.ArrayList;

public class TestDriveArrayList {
    public static void main(String[] args) {
        // Cria um ArrayList para as Canetas
        ArrayList<Caneta> canetas = new ArrayList<Caneta>();
        //Adiciona uma caneta
        canetas.add(new Caneta("Azul", 0.7));
        canetas.add(new Caneta("Vermelha", 1.0));


        // Estudo do método size
        System.out.println("Size agora: " + canetas.size() + "\n");
        
        // Remove um objeto de um índice
        //canetas.remove(0);


        // Passar por todos os elementos do array
        // Método 1
        System.out.println("Método 1\n");
        for(int i = 0; i < canetas.size(); i++){
            System.out.println("Cor da Caneta: " + canetas.get(i).cor);
        }

        // Método 2
        System.out.println("\nMétodo 2\n");
        for(Caneta caneta : canetas){
            System.out.println("Cor da Caneta: " + caneta.cor);
        }
        
    }
}
