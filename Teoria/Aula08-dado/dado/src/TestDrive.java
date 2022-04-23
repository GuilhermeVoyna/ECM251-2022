public class TestDrive{ 
       
    public static void executar(){
        Dado d1 = new Dado("1234");
        System.out.println("Dado criado:" + d1);
        System.out.println("Face atual:" + d1.faceAtual());    
        //Sorteia uma face
        d1.rodar();
        System.out.println("Face atual:" + d1.faceAtual());
    }
}
