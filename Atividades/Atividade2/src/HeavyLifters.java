public class HeavyLifters extends Membro {

    private static String funcao="HeavyLifters";

    public HeavyLifters(String usuario, String email) {
        super(usuario, email, funcao);
    }

    @Override
    public void PostaMensgem() {
        String horario=super.horario();
        if(horario=="normal"){
            System.out.println("Podem contar conosco!");
        }
        else{
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
        }
    }
}
