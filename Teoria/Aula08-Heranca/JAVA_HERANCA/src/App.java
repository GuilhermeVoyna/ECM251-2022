public class App {
    public static void main(String[] args) throws Exception {
        // Ninja jiraya = new Ninja("Jiraya", "Familia", new String[]{"Corte Vertical", "Corte Horizontal"});
        // System.out.println("Treinamento:"+jiraya.train());
        // System.out.println(jiraya);
        AcademicStudent naruto = new AcademicStudent("Naruto", "Uzumaki", new String[]{"Jutsu dos clones da sombra", "Rasengan", "Chamar Kurama"});
        System.out.println(naruto.train());
        System.out.println(naruto.play());
        
        Genin ninja = new Genin("Nome", "Konoha", new String[]{"Jutsu1", "Jutsu2"}, "Coletar items");
        System.out.println(ninja.goToMission());
        System.out.println(ninja.train());

        Chuunin ninja2 = new Chuunin("Yamato", "Konohagakure", new String[]{"Jutsu1", "Jutsu2"}, "Coletar items");
        System.out.println(ninja2.goToMission());
        System.out.println(ninja2.train());

        Jounin ninja3 = new Jounin("Kakashi", "Hatake", new String[]{"Jutsu1", "Jutsu2"}, "Coletar items");
        System.out.println(ninja3.goToMission());
        System.out.println(ninja3.train());
    }
}