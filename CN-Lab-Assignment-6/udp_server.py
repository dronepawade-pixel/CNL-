#!/usr/bin/env python3
"""CN Lab Assignment 6 — UDP Server (both operations).
Aim (a): UpperCase -> LowerCase | Aim (b): Reverse the String
Pseudocode: START -> socket -> bind -> recvfrom -> display -> sendto -> close -> STOP
Run: ./udp_server.py [HOST] [PORT]   (defaults: 127.0.0.1 65432)
Protocol from client: "LOWER:<text>" or "REVERSE:<text>"
"""
import socket
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 65432

# 2. Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3. Bind socket to IP + port
sock.bind((HOST, PORT))
print(f"[SERVER] Listening on {HOST}:{PORT} (UDP) ... Ctrl+C to stop")

try:
    while True:
        # 4-5. Wait + receive message and client address
        data, addr = sock.recvfrom(4096)
        msg = data.decode(errors="replace")
        # 6. Display received message
        print(f"[SERVER] From {addr}: {msg!r}")

        # 7. Send reply to client address (both aims supported)
        if msg.startswith("LOWER:"):
            reply = msg[len("LOWER:"):].lower()
        elif msg.startswith("REVERSE:"):
            reply = msg[len("REVERSE:"):][::-1]
        else:
            # No prefix: return both results (covers both aims at once)
            reply = f"LOWER:{msg.lower()} | REVERSE:{msg[::-1]}"
        sock.sendto(reply.encode(), addr)
        print(f"[SERVER] Replied: {reply!r}")
except KeyboardInterrupt:
    print("\n[SERVER] Stopped.")
finally:
    # 8. Close server socket
    sock.close()
