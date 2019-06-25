import time

process_display = 0
processtext = 0
processline = 0
onepercent = 0.2066115702479339
loading = f'[----------------------]'

while True:
  print(f'{loading} {round(processtext)}%', end='\r')
  processtext = processtext + onepercent
  processline = processline + onepercent
  if processline == 4.545454545454546:
    loading = loading.replace('-', '#', 1)
    processline = 0
  time.sleep(0.01)

  if int(processtext) == 100 :     
    print(f'{loading} {int(processtext)}%')   
    break
