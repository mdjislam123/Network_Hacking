import psutil

nics = psutil.net_if_stats()

for nic in nics:
    print(f"{nic}\n")
