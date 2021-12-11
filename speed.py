import speedtest

test = speedtest.Speedtest()
print("Loading server list...")
test.get_servers()
print("Choose the best server ...")
best = test.get_best_server()
vitri = best['country'].replace('Vietnam', 'Việt Nam')
print(f"Found: {best['host']} located in {vitri}")

print("Performance download test...")
download_result = test.download()
print("Performance upload test...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_result:.2f} ms")
