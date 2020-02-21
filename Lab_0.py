from struct import *

class NutellaPacket:
    # init function -> id, secret_code, package_size,nutella_eater
    def __init__(self, id_, secret_code, package_size, nutella_eater):
        self.id_ = id_
        self.secret_code = secret_code
        self.package_size = package_size
        self.nutella_eater = nutella_eater

    def serialize(self, first_size, second_size):
        # ! -> network byte order
        # I -> id -> unsigned int
        # len(string) + s -> char []
        # i -> int
        var = pack("!I"+str(first_size)+"si"+str(second_size)+"s", self.id_, self.secret_code.encode("ascii"),
                   self.package_size, self.nutella_eater.encode("ascii"))
        # another way to pack strings
        var2 = pack("!I"+str(first_size)+"si"+str(second_size)+"s", self.id_, bytes(self.secret_code, "ascii"),
                          self.package_size, bytes(self.nutella_eater, "ascii"))
        #print(var2)
        x = unpack("!I"+str(first_size)+"si"+str(second_size)+"s", var)
        print("pack: \n", var)
        print("list: \n", list(var))
        print("unpack: \n", x)
        return list(var)


networks = "Networks"
#networks = list(networks)
print(networks)
eater = "Hagar Barakat"
#eater = list(eater)
print(eater)
nutella = NutellaPacket(1111, networks, 4096, eater)
pack_output = nutella.serialize(len(networks), len(eater))
#print(pack_output)


