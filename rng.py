class MyCryptoRNG:
    def __init__(self, seed: int):
        self.m = 2147483647           # 2^31 - 1
        self.a = 1103515245
        self.c = 12345
        self.state = seed             # X0

    def next_int(self) -> int:
        """
        Bir sonraki rastgele tam sayıyı üretir.
        """
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def next_float(self) -> float:
        """
        [0, 1) aralığında rastgele reel sayı üretir.
        """
        return self.next_int() / self.m


# Örnek kullanım
if __name__ == "__main__":
    rng = MyCryptoRNG(seed=987654321)

    for _ in range(5):
        print(rng.next_int())
