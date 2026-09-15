#!/usr/bin/env python3
"""CN Lab Assignment 6 — UDP Client (both operations).
Pseudocode: START -> socket -> input -> sendto -> recvfrom -> display -> close -> STOP
Run: ./udp_client.py [HOST] [PORT]   (defaults: 127.0.0.1 65432)
"""
import socket
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 65432

# 2. Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)
print(f"[CLIENT] Server {HOST}:{PORT} | type 'exit' to quit.")

try:
    while True:
        # 3. Input message + operation (covers both aims)
        op = input("\nChoose operation — 1: UPPER->lower (a), 2: Reverse (b): ").strip()
        if op.lower() == "exit":
            break
        text = input("Enter string: ")
        if text.lower() == "exit":
            break
        if op == "1":
            payload = f"LOWER:{text}"
        elif op == "2":
            payload = f"REVERSE:{text}"
        else:
            print("Invalid choice. Enter 1 or 2 (or 'exit').")
            continue
        # 4. Send message to server IP + port
        sock.sendto(payload.encode(), (HOST, PORT))
        # 5. Receive reply from server
        data, _ = sock.recvfrom(4096)
        # 6. Display server reply
        print(f"[CLIENT] Server reply: {data.decode(errors='replace')}")
except socket.timeout:
    print("[CLIENT] No reply (timeout). Is the server running?")
except KeyboardInterrupt:
    print("\n[CLIENT] Stopped.")
finally:
    # 7. Close client socket
    sock.close()
