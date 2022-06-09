import java.util.ArrayList;
import java.util.List;

public class Sistema {
    private static String horario;

    public Sistema() {
        Sistema.horario = "normal";
    }


    static void run(){
        
        setHorario("normal");
        System.out.println("Bom dia s2");
        System.out.println("horario do dia é: "+getHorario());
        
        List<Membro> membros= new ArrayList<Membro>();

        membros.add(new BigBrothers("Muilo", "hakerSupremo@gmail.com"));

        membros.add(new MobileMembers("M4st3er","sud0c0d1g0@hotmail.com"));

        membros.add(new HeavyLifters("AMONGUS", "sememail.gmail.com"));

        membros.add(new ScriptGuys("vilinhoF0f0", "email23@yahoo.com"));

        membros.add(new ScriptGuys("revolucionario", "destruidor_da_MAsK@maua.br"));

        mostraMembro(membros);
        System.out.println();
        mensagemTodos(membros);
        mudarTurno();  // hehe
        mensagemTodos(membros);
        mudarTurno();
        membros.remove(4);
        membros.remove(2);
        mensagemTodos(membros);


        System.out.println();
    }


    public static String getHorario() {
        return horario;
    }
    private static void setHorario(String horario) {
        Sistema.horario = horario;
    }

    private static void  mudarTurno(){
        if(getHorario()=="normal"){
            setHorario("extra");
        }
        else{
            setHorario("normal");
        }
        System.out.println("\n--TURNO MUDADO--");
    }


    public static void mostraMembro(List<Membro> pokemons){
        for (Membro pokemon : pokemons) {
            System.out.println(pokemon);
        }
    }

    public static void mensagemTodos(List<Membro> membros){
        for (Membro membro : membros) {
            membro.PostaMensgem();
        }
    }
}
