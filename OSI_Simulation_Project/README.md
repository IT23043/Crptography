# Minimal OSI 7-Layer Simulation

A clean, minimal, and straightforward Python script that simulates how data moves through the **7 layers of the OSI model** in CMD.

## What it does
* **Sender (Encapsulation - L7 to L1):** Shows how headers and trailers are added to user data (Data → Segment → Packet → Frame → Bits).
* **Medium Transmission:** Simulates sending raw bits across the physical link.
* **Receiver (Decapsulation - L1 to L7):** Strips headers step-by-step and delivers the final message to the destination application.

---

## How to Run in CMD

Open Command Prompt in this folder and run:

```cmd
python main.py
```

Or double-click:
```cmd
run.bat
```

---

## Example Output

```text
Enter message: Hello OSI

=================================================================
                 OSI 7-LAYER SIMULATION
=================================================================

--- [SENDER: ENCAPSULATION (Layer 7 -> Layer 1)] ---
[Layer 7 - Application]   User Data prepared: 'Hello OSI'
[Layer 6 - Presentation]  Data Formatted / Encoded: '[UTF-8 Encoded] Hello OSI'
[Layer 5 - Session]       Session Established: '[SESSION-101] [UTF-8 Encoded] Hello OSI'
[Layer 4 - Transport]     Segment (Ports added): '[Port:8080->80 | Seq:1] <...>'
[Layer 3 - Network]       Packet (IPs added): '[IP:192.168.1.10->192.168.1.20 | TTL:64] <...>'
[Layer 2 - Data Link]     Frame (MACs & FCS added): '[MAC:9C:67:...->E4:5D:...] <...> [FCS:CRC32]'
[Layer 1 - Physical]      Bits Stream on Wire: 01001000 01100101 01101100 01101100 01101111...

>>> Transmitting raw bits across physical medium (Cable/Channel) >>>

--- [RECEIVER: DECAPSULATION (Layer 1 -> Layer 7)] ---
[Layer 1 - Physical]      Received raw electrical bits -> reassembled frame.
[Layer 2 - Data Link]     Verified CRC32 trailer. Stripped MAC header [E4:5D:51:32:B1:9C].
[Layer 3 - Network]       Verified Destination IP [192.168.1.20]. Stripped IP header.
[Layer 4 - Transport]     Reassembled segment. Stripped port header -> sent to Port 80.
[Layer 5 - Session]       Validated SESSION-101. Session synchronized.
[Layer 6 - Presentation]  Decoded UTF-8 data back into original format.
[Layer 7 - Application]   Delivered message to user application: 'Hello OSI'
=================================================================
Transmission Successful: All 7 layers completed.
```
