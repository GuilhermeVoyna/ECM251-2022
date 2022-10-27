public class Caneta {
    // Características da caneta - seus atributos
    String modelo;
    String cor;
    double ponta;
    boolean tampada;
    int carga;
    final int CARGA_INICIAL = 100;

    void iniciarCaneta(String cor, String modelo, double ponta, boolean tampada) {
        this.cor = cor;
        this.modelo = modelo;
        this.ponta = ponta;
        this.carga = CARGA_INICIAL;
        this.tampada = tampada;
    }

    // Comportamoentos da caneta - seus Métodos
    void escrever(String texto) {
        if(this.tampada == false){
            for(int i =0; i < texto.length(); i++){
                if(this.carga > 0){
                    System.out.print(texto.charAt(i));
                    this.carga--;
                }else{
                    System.out.println("\nCaneta sem carga");
                    break;
                }
            }
            System.out.println();
        }else{
            System.out.println("Caneta tampada");
        }
            
    }

    String mostrarDados() {
        return "Modelo: " + this.modelo +
                " - Cor: " + this.cor +
                " - Ponta: " + this.ponta +
                " - Carga: " + this.carga +
                "- Tampada: " + this.tampada;
    }

    boolean destamparCaneta(){
        return this.tampada = false;
    }
}