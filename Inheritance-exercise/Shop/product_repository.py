from product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for pr in self.products:
            if pr.name == product_name:
                return pr

    def remove(self, product_name: str):
        pr = self.find(product_name)
        if pr:
            self.products.remove(pr)
        return self.products

    def __repr__(self):
        result = [f"{p.name}: {p.quantity}" for p in self.products]
        return '\n'.join(result)


n_pr = ProductRepository()

print(n_pr.products)

pr = Product("Fanta", 10)
n_pr.add(pr)
pr = Product("Cheese", 50)
n_pr.add(pr)
pr = Product("Salad", 20)
n_pr.add(pr)

print(n_pr.products)

k = n_pr.find("Salad")
print(k.name, k.quantity)
k.increase(20)
print(k.name, k.quantity)