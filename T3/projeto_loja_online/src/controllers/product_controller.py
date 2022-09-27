
from src.models.product import Product

class ProductController:
    def __init__(self):
        self._products = [
            Product("Elden Ring", 300.00, "https://www.cdkeypt.pt/wp-content/uploads/elden-ring-featured-300x300-3.jpg"),
            Product("Minecraft", 60.00, "https://bk.ibxk.com.br/2018/11/programas/8125222104324541.png"),
            Product("Minecraft2", 600.00, "https://bk.ibxk.com.br/2018/11/programas/8125222104324541.png"),
            Product( "Cyberpunk 2077", 199.00, "https://sm.ign.com/t/ign_br/game/c/cyberpunk-/cyberpunk-2077_tdqt.300.jpg"),
            Product( "Torradeira Gamer", 999.99, "https://static.turbosquid.com/Preview/2019/05/10__06_10_12/sig.jpgAC951368-0425-45F7-AC83-A201FB210758Res300.jpg"),
            Product( "Fone Gamer", 799.00, "https://cdn.awsli.com.br/300x300/2132/2132264/produto/14670788833df2d6eb8.jpg"),
            Product( "Tenes Gamer", 199.00, "https://i.ebayimg.com/thumbs/images/g/6UIAAOSw5UZY-GDm/s-l300.jpg"),
            Product( "Mouse Gamer", 199.00, "https://cdn.awsli.com.br/300x300/1422/1422163/produto/59461688/38bb8f8f04.jpg"),
        ]

    def get_product(self,index):
        return self._products[index]