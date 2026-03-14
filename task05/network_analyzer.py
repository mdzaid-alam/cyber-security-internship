from scapy.all import sniff, IP, conf
import sys
import datetime

def process_packet(packet):
    """Process a single captured packet"""
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if packet.haslayer(IP):
            ip_layer = packet[IP]
            print("\n📦 New Packet Captured")
            print(f"⏰ Time: {timestamp}")
            print(f"➡️ Source IP: {ip_layer.src}")
            print(f"⬅️ Destination IP: {ip_layer.dst}")
            print(f"📡 Protocol: {ip_layer.proto}")

            if packet.haslayer('TCP'):
                print(f"🔌 Source Port: {packet['TCP'].sport}")
                print(f"🔌 Destination Port: {packet['TCP'].dport}")
            elif packet.haslayer('UDP'):
                print(f"🔌 Source Port: {packet['UDP'].sport}")
                print(f"🔌 Destination Port: {packet['UDP'].dport}")

            print("=" * 50)
    except Exception as e:
        print(f"Error processing packet: {e}")

def main():
    print("🔍 Starting Basic Network Packet Analyzer...")
    print("Capturing 1 packet only...\n")

    try:
        sniff(filter="ip", prn=process_packet, store=False, count=1)  # only capture 1 packet
    except KeyboardInterrupt:
        print("\n🛑 Capture stopped.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if "No libpcap provider available" in str(e):
            print("\n⚠️ Npcap is not installed!")
            print("Please install Npcap from: https://npcap.com/#download")
            print("Then restart your computer and run this script as administrator.")
    finally:
        sys.exit(0)

if __name__ == "__main__":
    main()
