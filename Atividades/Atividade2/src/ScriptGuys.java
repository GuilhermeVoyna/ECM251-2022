public class ScriptGuys extends Membro {

    private static String funcao="ScriptGuys";

    public ScriptGuys(String usuario, String email) {
        super(usuario, email, funcao);
    }
    @Override
    public void PostaMensgem() {
        String horario=super.horario();
        if(horario=="normal"){
            System.out.println("Prazer em ajudar novos amigos de código!");

            String bebida = "cafe_CoffeShop";
        }
        else{
            System.out.println("QU3Ro_S3us_r3curs0s.py");

            String bebida = "achocolatados";
        }
    }
}
