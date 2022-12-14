import random


def genSk():
    return random.randint(1, 9999)


def genPk(base, exponent):
    return pow(base, exponent) % p


def bruteforce(pk):
    for i in range(10000):
        posPK = genPk(g, i)
        if posPK == pk:
            return i
    raise Exception("Could not bruteforce the sk")


def encrypt(m, pkRec):
    r = genSk()
    c1 = pow(g, r)
    c2 = int(genPk(pkRec, r) * m)
    return c1, c2


def decrypt(c1, c2, skRec):
    compKey = genPk(c1, skRec)
    return int(c2 / compKey)


g = 666  # Shared base
p = 6661  # Share prime
bobPK = 2227
aliceSK = genSk()
alicePK = genPk(aliceSK, g)


def main():
    # Ass 1.1
    (c1, c2) = encrypt(2000, bobPK)
    print("c1 value is " + str(c1))
    print("c2 value is " + str(c2))

    # Ass 1.2
    bobSK = bruteforce(bobPK)
    print("Bobs secret key is " + str(bobSK))
    print("The message from Alice is " + str(decrypt(c1, c2, bobSK)))

    # Ass 1.3
    (badc1, badc2) = encrypt(6000, bobPK)
    c1 = badc1
    c2 = badc2
    badMsg = decrypt(c1, c2, bobSK)
    print("Message " + str(badMsg) + " received from Alice")


if __name__ == "__main__":
    main()
