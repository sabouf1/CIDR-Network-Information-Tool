import tkinter as tk
from tkinter import messagebox
import ipaddress

def get_network_info(cidr_block):
    network = ipaddress.ip_network(cidr_block)
    
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    subnet_mask = network.netmask
    usable_ip_range = (network.network_address + 1, network.broadcast_address - 1)
    total_addresses = network.num_addresses
    
    return {
        "CIDR Block": str(network),
        "Network Address": str(network_address),
        "Broadcast Address": str(broadcast_address),
        "Subnet Mask": str(subnet_mask),
        "Usable IP Range": (str(usable_ip_range[0]), str(usable_ip_range[1])),
        "Total IP Addresses": total_addresses
    }

def show_network_info():
    cidr_input = entry.get()
    
    try:
        info = get_network_info(cidr_input)
        info_text.config(state=tk.NORMAL)
        info_text.delete(1.0, tk.END)
        for key, value in info.items():
            info_text.insert(tk.END, f"{key}: {value}\n")
        info_text.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the main window
root = tk.Tk()
root.title("Network Information")

# Create and place widgets
label = tk.Label(root, text="Enter a CIDR Block:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Network Info", command=show_network_info)
button.pack()

info_text = tk.Text(root, height=10, width=50)
info_text.config(state=tk.DISABLED)
info_text.pack()

root.mainloop()
