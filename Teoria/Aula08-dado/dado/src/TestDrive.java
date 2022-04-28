public class TestDrive{ 
       
    public static void executar(){
        Dado d1 = new Dado("1234");
        System.out.println("Dado criado:" + d1);
        System.out.println("Face atual:" + d1.faceAtual());    
        //Sorteia uma face
        d1.rodar();
        System.out.println("Face atual:" + d1.faceAtual());

        Dado d6 = new DadoD6("6");
        System.out.println("Dado criado:" + d6);
        System.out.println("Face atual:" + d6.faceAtual());    
        //Sorteia uma face
        d6.rodar();
        System.out.println("Face atual:" + d6.faceAtual());

        Dado d20 = new Dado20("20");
        System.out.println("Dado criado"+d20);
        System.out.println("Face atual:" + d20.faceAtual());    
        d20.rodar();
        System.out.println("Face atual:" + d20.faceAtual());   

        Dado d10 = new Dado10("10");
        System.out.println("Dado criado"+d10);
        System.out.println("Face atual:" + d10.faceAtual());    
        d10.rodar();
        System.out.println("Face atual:" + d10.faceAtual());   






    }
}
