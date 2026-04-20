class Arxitektor:
    def __init__(self, ism, tajriba):
        self.ism = ism
        self.tajriba = tajriba

    def ishlaydi(self):
        return f"{self.ism} ishlaydi"

class GoogleArxitektor(Arxitektor):
    def __init__(self, ism, tajriba):
        super().__init__(ism, tajriba)

    def google_tajribasi(self):
        return f"{self.ism} Google tajribasiga ega"

class MetaArxitektor(Arxitektor):
    def __init__(self, ism, tajriba):
        super().__init__(ism, tajriba)

    def meta_tajribasi(self):
        return f"{self.ism} Meta tajribasiga ega"

class ArxitektorDasturchi(Arxitektor):
    def __init__(self, ism, tajriba):
        super().__init__(ism, tajriba)

    def arxitektor_dasturchi(self):
        return f"{self.ism} arxitektor-dasturchi"

class GoogleArxitektorDasturchi(GoogleArxitektor, ArxitektorDasturchi):
    def __init__(self, ism, tajriba):
        GoogleArxitektor.__init__(self, ism, tajriba)
        ArxitektorDasturchi.__init__(self, ism, tajriba)

    def google_tajribasi(self):
        return f"{self.ism} Google tajribasiga ega arxitektor-dasturchi"

    def ishlaydi(self):
        return f"{self.ism} Google tajribasiga ega arxitektor-dasturchi ishlaydi"

class MetaArxitektorDasturchi(MetaArxitektor, ArxitektorDasturchi):
    def __init__(self, ism, tajriba):
        MetaArxitektor.__init__(self, ism, tajriba)
        ArxitektorDasturchi.__init__(self, ism, tajriba)

    def meta_tajribasi(self):
        return f"{self.ism} Meta tajribasiga ega arxitektor-dasturchi"

    def ishlaydi(self):
        return f"{self.ism} Meta tajribasiga ega arxitektor-dasturchi ishlaydi"

google_arxitektor_dasturchi = GoogleArxitektorDasturchi("Ali", "Google")
meta_arxitektor_dasturchi = MetaArxitektorDasturchi("Vali", "Meta")

print(google_arxitektor_dasturchi.google_tajribasi())
print(google_arxitektor_dasturchi.ishlaydi())

print(meta_arxitektor_dasturchi.meta_tajribasi())
print(meta_arxitektor_dasturchi.ishlaydi())
