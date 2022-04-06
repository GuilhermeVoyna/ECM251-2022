public class App {
    public static void main(String[] args) throws Exception {
        Cliente c1 = new Cliente();
        
        c1.setNome("Murilo");
       // c1.setCpf("666");
        c1.setEmail("420@gmail.com");
       // c1.setConta(new Conta());
        
        System.out.println("Nome do cliente:" + c1.getNome());
        System.out.println("Email do cliente:" + c1.getEmail());
        System.out.println("Cpf do cliente:" + c1.getCpf());
        c1.getConta().visualizarSaldo();
    }
}