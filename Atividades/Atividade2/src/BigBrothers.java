public class BigBrothers extends Membro {

    private static String funcao="BigBrothers";
    


    public BigBrothers(String usuario, String email) {
        super(usuario, email, funcao);
    }
    
    







    @Override
    public void PostaMensgem() {
        String horario=super.horario();
        if(horario=="normal"){
            System.out.println("Sempre ajudando as pessoas membros ou não S2!");
        }
        else{
            System.out.println("...");
            boolean suspense = true;
        }
    }

    private void NovoMembro(String funcao,String usuario,String email,Membro conta){
        if(funcao=="MobileMembers"){
            new MobileMembers(usuario, email);
        }
        if(funcao=="HeavyLifters"){
            new HeavyLifters(usuario, email);
        }
        if(funcao=="ScriptGuys"){
            new ScriptGuys(usuario, email);
        }
        if(funcao=="BigBrothers"){
            new BigBrothers(usuario, email);
        }
    }
}
