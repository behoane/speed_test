import speedtest

test = speedtest.Speedtest()
print("Đang tải danh sách máy chủ...")
test.get_servers()
print("Chọn máy chủ tốt nhất ...")
best = test.get_best_server()
vitri = best['country'].replace('Vietnam', 'Việt Nam')
print(f"Máy chủ: {best['host']} vị trí {vitri}")

print("Thực hiện kiểm tra tải xuống...")
download_result = test.download()
print("Thực hiện kiểm tra tải lên...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Tốc độ tải về: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Tốc độ tải về: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_result:.2f} ms")