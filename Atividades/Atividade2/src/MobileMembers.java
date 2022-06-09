public class MobileMembers extends Membro {

    private static String funcao="MobileMembers";

    public MobileMembers(String usuario, String email) {
        super(usuario, email, funcao);
    }

   
    @Override
    public void PostaMensgem() {
        String horario=super.horario();
        if(horario=="normal"){
            System.out.println("Happy Coding!");
        }
        else{
            System.out.println("Happy_C0d1ng. Maskers");
        }
    }

    
}
