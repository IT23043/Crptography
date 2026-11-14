"""
Minimal OSI 7-Layer Simulator
==============================
A simple, minimal, and clean simulation of the 7-layer OSI model.
Demonstrates encapsulation (Sender: L7 -> L1) and decapsulation (Receiver: L1 -> L7).
Runnable directly in CMD.
"""

import time

def text_to_binary(text):
    """Converts a string of text into binary representation."""
    return " ".join(format(ord(c), "08b") for c in text)

def simulate_osi(message, src_ip="192.168.1.10", dst_ip="192.168.1.20", src_port=8080, dst_port=80):
    print("\n" + "=" * 65)
    print("                 OSI 7-LAYER SIMULATION")
    print("=" * 65)

    # ---------------- 1. SENDER (ENCAPSULATION) ----------------
    print("\n--- [SENDER: ENCAPSULATION (Layer 7 -> Layer 1)] ---")
    time.sleep(0.2)

    # Layer 7: Application
    l7_data = message
    print(f"[Layer 7 - Application]   User Data prepared: '{l7_data}'")
    time.sleep(0.2)

    # Layer 6: Presentation
    l6_data = f"[UTF-8 Encoded] {l7_data}"
    print(f"[Layer 6 - Presentation]  Data Formatted / Encoded: '{l6_data}'")
    time.sleep(0.2)

    # Layer 5: Session
    session_id = "SESSION-101"
    l5_data = f"[{session_id}] {l6_data}"
    print(f"[Layer 5 - Session]       Session Established: '{l5_data}'")
    time.sleep(0.2)

    # Layer 4: Transport (Segment)
    l4_segment = f"[Port:{src_port}->{dst_port} | Seq:1] <{l5_data}>"
    print(f"[Layer 4 - Transport]     Segment (Ports added): '{l4_segment}'")
    time.sleep(0.2)

    # Layer 3: Network (Packet)
    l3_packet = f"[IP:{src_ip}->{dst_ip} | TTL:64] <{l4_segment}>"
    print(f"[Layer 3 - Network]       Packet (IPs added): '{l3_packet}'")
    time.sleep(0.2)

    # Layer 2: Data Link (Frame)
    src_mac = "9C:67:D6:81:B0:7D"
    dst_mac = "E4:5D:51:32:B1:9C"
    l2_frame = f"[MAC:{src_mac}->{dst_mac}] <{l3_packet}> [FCS:CRC32]"
    print(f"[Layer 2 - Data Link]     Frame (MACs & FCS added): '{l2_frame}'")
    time.sleep(0.2)

    # Layer 1: Physical (Bits)
    raw_bits = text_to_binary(message)
    bits_preview = raw_bits[:45] + ("..." if len(raw_bits) > 45 else "")
    print(f"[Layer 1 - Physical]      Bits Stream on Wire: {bits_preview}")
    time.sleep(0.4)

    # ---------------- 2. TRANSMISSION ----------------
    print("\n>>> Transmitting raw bits across physical medium (Cable/Channel) >>>\n")
    time.sleep(0.5)

    # ---------------- 3. RECEIVER (DECAPSULATION) ----------------
    print("--- [RECEIVER: DECAPSULATION (Layer 1 -> Layer 7)] ---")
    time.sleep(0.2)

    # Layer 1: Physical
    print(f"[Layer 1 - Physical]      Received raw electrical bits -> reassembled frame.")
    time.sleep(0.2)

    # Layer 2: Data Link
    print(f"[Layer 2 - Data Link]     Verified CRC32 trailer. Stripped MAC header [{dst_mac}].")
    time.sleep(0.2)

    # Layer 3: Network
    print(f"[Layer 3 - Network]       Verified Destination IP [{dst_ip}]. Stripped IP header.")
    time.sleep(0.2)

    # Layer 4: Transport
    print(f"[Layer 4 - Transport]     Reassembled segment. Stripped port header -> sent to Port {dst_port}.")
    time.sleep(0.2)

    # Layer 5: Session
    print(f"[Layer 5 - Session]       Validated {session_id}. Session synchronized.")
    time.sleep(0.2)

    # Layer 6: Presentation
    print(f"[Layer 6 - Presentation]  Decoded UTF-8 data back into original format.")
    time.sleep(0.2)

    # Layer 7: Application
    print(f"[Layer 7 - Application]   Delivered message to user application: '{message}'")
    time.sleep(0.2)

    print("=" * 65)
    print("Transmission Successful: All 7 layers completed.\n")

def main():
    print("=" * 65)
    print("          Minimal OSI 7-Layer Simulation (CMD)")
    print("=" * 65)
    print("Type any text message to watch it travel through all 7 OSI layers.")
    print("Type 'q' or press Ctrl+C to exit.\n")

    while True:
        try:
            msg = input("Enter message: ").strip()
            if not msg:
                continue
            if msg.lower() in ["q", "quit", "exit"]:
                print("Exiting simulator.")
                break

            simulate_osi(msg)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting simulator.")
            break

if __name__ == "__main__":
    main()
