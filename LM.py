import subprocess
import os
import time
import datetime

# Hämta IP-adresser från filen config.txt
with open("config.txt", "r") as f:
    ip_list = [line.strip() for line in f]

# Loopa oändligt för att pinga IP-adresser var 5:e sekund
print("Logger startad")
print(datetime.datetime.now())

while True:
    with open("ping_resultat.txt", "a") as f:
        f.write("\n")
        for ip in ip_list:
            # Kör ping-kommando och få utdata med hjälp av subprocess
            ping_process = subprocess.Popen(["ping", "-n", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, error = ping_process.communicate()

            # Analysera utdata för att se om ping-svar var lyckat eller misslyckat
            if "Received = 1" in out.decode():
                ping_result = "Lyckades"
                # Få svarstid från ping-kommando
                time_result = out.decode().split("time=")[1].split(" ")[0]
            else:
                ping_result = "Misslyckades"
                time_result = "N/A"
            
            # Skriv resultat till fil
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Tid: {current_time} - IP-adress: {ip} - Ping resultat: {ping_result} - Svarstid: {time_result}\n")
    
    # Vänta 5 sekunder innan nästa pingning
    time.sleep(10)
