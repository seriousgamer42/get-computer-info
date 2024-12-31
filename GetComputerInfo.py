import os
import platform
import subprocess
import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime

class SystemInfoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("System Information Tool")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create buttons
        ttk.Button(main_frame, text="Get System Info", command=self.get_info).grid(row=0, column=0, pady=5)
        ttk.Button(main_frame, text="Save to File", command=self.save_info).grid(row=0, column=1, pady=5)
        
        # Create text area with scrollbar
        self.text_area = tk.Text(main_frame, height=30, width=80)
        scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scrollbar.set)
        
        self.text_area.grid(row=1, column=0, columnspan=2, pady=5)
        scrollbar.grid(row=1, column=2, sticky='ns')
        
        self.system_info = {}

    def run_powershell_command(self, command):
        try:
            result = subprocess.check_output(["powershell", "-Command", command], shell=True).decode()
            return result.strip()
        except:
            return "Information not available"

    def bytes_to_gb(self, bytes_str):
        try:
            bytes_num = float(bytes_str)
            gb = bytes_num / (1024 ** 3)
            return f"{gb:.2f} GB"
        except:
            return "N/A"

    def format_storage_info(self, storage_info):
        lines = storage_info.split('\n')
        if len(lines) < 2:
            return "Storage information not available"

        formatted_output = "Drive | Free Size | Total Space\n"
        formatted_output += "-" * 40 + "\n"

        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                drive = parts[0]
                free = self.bytes_to_gb(parts[1])
                size = self.bytes_to_gb(parts[2])
                formatted_output += f"{drive} | {free} | {size}\n"

        return formatted_output

    def get_info(self):
        self.text_area.delete(1.0, tk.END)
        self.system_info = {}
        
        # Operating System
        self.text_area.insert(tk.END, "Operating System:\n")
        os_info = platform.system() + " " + platform.version()
        self.text_area.insert(tk.END, f"{os_info}\n\n")
        self.system_info['Operating System'] = os_info

        # Motherboard
        self.text_area.insert(tk.END, "Motherboard:\n")
        mobo_info = self.run_powershell_command('Get-WmiObject Win32_BaseBoard | Format-List -Property Manufacturer,Product,SerialNumber')
        self.text_area.insert(tk.END, f"{mobo_info}\n\n")
        self.system_info['Motherboard'] = mobo_info

        # CPU
        self.text_area.insert(tk.END, "CPU:\n")
        cpu_info = self.run_powershell_command('Get-WmiObject Win32_Processor | Select-Object -ExpandProperty Name')
        self.text_area.insert(tk.END, f"{cpu_info}\n\n")
        self.system_info['CPU'] = cpu_info

        # RAM
        self.text_area.insert(tk.END, "RAM:\n")
        ram_info = self.run_powershell_command('Get-CimInstance Win32_PhysicalMemory | Measure-Object -Property Capacity -Sum | Select-Object -ExpandProperty Sum')
        ram_gb = f"Total RAM: {int(ram_info) / (1024**3):.2f} GB" if ram_info.isdigit() else "N/A"
        self.text_area.insert(tk.END, f"{ram_gb}\n\n")
        self.system_info['RAM'] = ram_gb

        # Storage
        self.text_area.insert(tk.END, "Storage:\n")
        storage_raw = self.run_powershell_command('Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID,FreeSpace,Size | Format-Table -HideTableHeaders')
        storage_formatted = self.format_storage_info(storage_raw)
        self.text_area.insert(tk.END, f"{storage_formatted}\n\n")
        self.system_info['Storage'] = storage_formatted

        # GPU
        self.text_area.insert(tk.END, "GPU:\n")
        gpu_info = self.run_powershell_command('Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name')
        self.text_area.insert(tk.END, f"{gpu_info}\n\n")
        self.system_info['GPU'] = gpu_info

        # Network Interfaces
        self.text_area.insert(tk.END, "Network Interfaces:\n")
        network_info = self.run_powershell_command('Get-CimInstance Win32_NetworkAdapter | Where-Object { $_.NetConnectionStatus -eq 2 } | Select-Object -ExpandProperty Name')
        self.text_area.insert(tk.END, f"{network_info}\n")
        self.system_info['Network Interfaces'] = network_info

    def save_info(self):
        if self.system_info:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"system_info_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump(self.system_info, f, indent=4)
            self.text_area.insert(tk.END, f"\nSaved to {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemInfoGUI(root)
    root.mainloop()
