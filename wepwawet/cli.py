from wepwawet.scanners.lookup import nslookup
from wepwawet.scanners.shodan import ask_shodan

def main():

  print("""
  888       888                                                                 888    
  888   o   888                                                                 888    
  888  d8b  888                                                                 888    
  888 d888b 888  .d88b.  88888b.  888  888  888  8888b.  888  888  888  .d88b.  888888 
  888d88888b888 d8P  Y8b 888 "88b 888  888  888     "88b 888  888  888 d8P  Y8b 888    
  88888P Y88888 88888888 888  888 888  888  888 .d888888 888  888  888 88888888 888    
  8888P   Y8888 Y8b.     888 d88P Y88b 888 d88P 888  888 Y88b 888 d88P Y8b.     Y88b.  
  888P     Y888  "Y8888  88888P"   "Y8888888P"  "Y888888  "Y8888888P"   "Y8888   "Y888 
                         888                                                           
                         888                                                           
                         888                                                           
  """)
  with open(path, encoding='utf-8') as f: lines = f.readlines()
  res = []

  for url in lines:
    ip = nslookup(url)
    shodan_infos = ask_shodan(ip)
    prop = {
      "url": url,
      "ip": ip
    }