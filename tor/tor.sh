#!/bin/bash
sudo vim /etc/tor/torrc
sudo systemctl restart tor@default.service 
journalctl -exft Tor
