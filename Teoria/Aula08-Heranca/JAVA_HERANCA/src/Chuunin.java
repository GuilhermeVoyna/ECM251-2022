public class Chuunin extends Ninja{

    public Chuunin(String name, String family, String[] jutsus, String mission) {
        super(name, family, jutsus);
        this.mission = mission;
    }
    private String mission;

    public String goToMission(){
        return String.format("%s esta indo na missao %s", getName(), mission);
    }
    
    @Override
    public String train(){
        return String.format("%s esta treinando o jutsu %s!", getName(), getJutsus()[0]);
    }
}
