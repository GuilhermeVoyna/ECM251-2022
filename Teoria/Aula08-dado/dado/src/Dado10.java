import java.util.concurrent.ThreadLocalRandom;

public class Dado10 extends Dado {

    public Dado10(String id) {
        super(id);
        //TODO Auto-generated constructor stub
    }
    @Override
    public void rodar() {
        this.face =  ThreadLocalRandom.current().nextInt(1, 11);
    }
    
}
