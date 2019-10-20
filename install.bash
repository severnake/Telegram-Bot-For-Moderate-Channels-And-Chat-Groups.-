#!/usr/bin/env bash
echo -e "\u001b[32mInstallation Begining...\u001b[0m"
memory_free=`awk '/^Mem/ {print $4}' <(free -m)`

if [ "$memory_free" -le 60 ]; then
echo -e "\u001b[31m¦ ERROR:Your RAM size is less than 60MB\n¦ YOUR RAM FREE SIZE IS : ${memory_free}MB\u001b[0m"
exit ;
fi

sudo apt update

PKG_OK=`/usr/bin/dpkg-query --show --showformat='${db:Status-Status}\n' 'python3-minimal'`
if [ "${PKG_OK}" != "installed" ]; then
sudo apt install python3-minimal -y
fi

PKG_OK=`/usr/bin/dpkg-query --show --showformat='${db:Status-Status}\n' 'python3-pip'`
if [ "${PKG_OK}" != "installed" ]; then
sudo apt install python3-minimal -y
fi

python3 -m pip install -r requir.txt
python3 setup.py

echo -e '\u001b[32mRunning...\u001b[0m'
bash run.bash