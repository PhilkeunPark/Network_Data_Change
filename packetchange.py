import pydivert

print("start")

with pydivert.WinDivert("tcp and tcp.PayloadLength > 0") as w:

    for packet in w:

        if packet.is_outbound:
            data1 = packet.tcp.payload
            data2 = data1.replace(b'Accept-Encoding: gzip', b'Accept-Encoding:     ')
            packet.tcp.payload = data2
        if packet.is_inbound:
            data1 = packet.tcp.payload
            data2 = data1.replace(b'Michael', b'Gilbert')
            packet.tcp.payload = data2

        w.send(packet, recalculate_checksum=True)
