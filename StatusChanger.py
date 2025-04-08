import requests,time,itertools,os
print("Starting.")
token = "TOKEN HERE" # Put your token here
statuses = ["Ohio!", "Sigma", "Rizzler", "Skibidi", "Made By PotatoIsCool"] # Put your statuses here
headers = {"Authorization": token,"Content-Type": "application/json"}
PeriodCycles = itertools.cycle(statuses)
print("If it does not change make sure to check your token.\nMake sure it is correct and not outdated.")
while True:
    text = next(PeriodCycles)
    payload = {"custom_status": {"text": text}}
    requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    time.sleep(3) # how fast you want it to update
