

# Element interface
class Packet:
    def accept(self, visitor):
        pass

# Concrete Element: DataPacket
class DataPacket(Packet):
    def accept(self, visitor):
        visitor.visit_data_packet(self)

# Concrete Element: ControlPacket
class ControlPacket(Packet):
    def accept(self, visitor):
        visitor.visit_control_packet(self)


# Network class
class Network:
    def __init__(self):
        self.packets = []

    def add_packet(self, packet):
        self.packets.append(packet)

    def process_packets(self, visitor):
        for packet in self.packets:
            packet.accept(visitor)


# Visitor interface
class PacketVisitor:
    def visit_data_packet(self, data_packet):
        pass

    def visit_control_packet(self, control_packet):
        pass


# Concrete Visitor: PacketDecoder
class PacketDecoder(PacketVisitor):
    def visit_data_packet(self, data_packet):
        # Decode data packet
        print("Decoding data packet")

    def visit_control_packet(self, control_packet):
        # Decode control packet
        print("Decoding control packet")

# Concrete Visitor: PacketEncryptor
class PacketEncryptor(PacketVisitor):
    def visit_data_packet(self, data_packet):
        # Encrypt data packet
        print("Encrypting data packet")

    def visit_control_packet(self, control_packet):
        # Encrypt control packet
        print("Encrypting control packet")

# Concrete Visitor: PacketCompressor
class PacketCompressor(PacketVisitor):
    def visit_data_packet(self, data_packet):
        # Compress data packet
        print("Compressing data packet")

    def visit_control_packet(self, control_packet):
        # Compress control packet
        print("Compressing control packet")



# Client code
if __name__ == '__main__':
    # Create a network instance
    network = Network()

    # Add packets to the network
    data_packet = DataPacket()
    control_packet = ControlPacket()

    network.add_packet(data_packet)
    network.add_packet(control_packet)

    # Process packets using visitors
    decoder = PacketDecoder()
    network.process_packets(decoder) 

    encryptor = PacketEncryptor()
    network.process_packets(encryptor)


    compressor = PacketCompressor()
    network.process_packets(compressor)