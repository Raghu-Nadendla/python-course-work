class Flipkart:
    discount = 10
    products = {"iphone":100000,"laptop":50000}

    @classmethod
    def display(cls):
        print(cls.products)

    def info(self,name,phone):
        self.name = name
        self.phone = phone
        print(f"Hello {name}, Your details are saved")

    @staticmethod
    def banner():
        print(f'{Flipkart.discount}% discount is going on, buy now!!!!!!!!!!')


swathi = Flipkart()
swathi.banner()
swathi.info("swathi","9876543210")
swathi.display()

eswar = Flipkart()
eswar.banner()
eswar.info("eswar","8765432109")
eswar.display()


dhanasree = Flipkart()
dhanasree.banner()
dhanasree.info("dhanasree","7654321098")
dhanasree.display()