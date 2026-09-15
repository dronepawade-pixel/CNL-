#!/bin/bash
# CN Lab Assignment 6 — double-click launcher (macOS .command)
# Opens in Terminal, auto-starts UDP server, then runs UDP client.
cd "$(dirname "$0")"

echo "=== CN Lab Assignment 6: UDP Socket Programming ==="
echo "(a) UPPER->lower  |  (b) Reverse String"
echo

# Free port 65432 if a previous server is stuck
lsof -ti :65432 | xargs kill -9 2>/dev/null

# Start server in background
python3 ./udp_server.py 127.0.0.1 65432 &
SERVER_PID=$!
sleep 1

# Stop server when this window closes / client exits
cleanup() { kill $SERVER_PID 2>/dev/null; }
trap cleanup EXIT INT TERM

# Run client in foreground (interactive)
python3 ./udp_client.py 127.0.0.1 65432

# Cleanup + keep window readable after exit
cleanup
trap - EXIT INT TERM
echo
read -p "Done. Press Enter to close this window... "
