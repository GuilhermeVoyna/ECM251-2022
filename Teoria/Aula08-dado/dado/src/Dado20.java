import java.util.concurrent.ThreadLocalRandom;

public class Dado20 extends Dado {

    public Dado20(String id) {
        super(id);
    }

    @Override
    public void rodar() {
        this.face =  ThreadLocalRandom.current().nextInt(1, 21);
    }
    
}
