

git clone https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git
mkdir firmware-backup
cp /lib/firmware/rtlwifi/* /home/ubuntu/firmware-backup
rm -rf /lib/firmware/rtlwifi/*
cd linux-firmware
cp -r * /lib/firmware/rtlwifi/
cd ..

# add lines to /etc/network/interfaces
auto wlan0
iface wlan0 inet dhcp
  wpa-ssid
  wpa-psk


