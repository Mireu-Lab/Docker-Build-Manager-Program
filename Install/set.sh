sudo cp Install/build_maneger.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable build_maneger
sudo systemctl start build_maneger