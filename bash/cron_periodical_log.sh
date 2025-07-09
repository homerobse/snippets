#!/bin/bash
logfile="log_file.txt"
echo "## DATE AND TIME NOW: $(date)" >> $logfile
echo "$(free -ht | awk 'FNR == 2 {print "RAM used: " $3 , "total: " $2}')"  >> $logfile



# Run
# `crontab -e`
# Add this line to the end
# `0 * * * * /path/to/cron_periodical_log.sh`  # run every hour
#
# For this to work, `cron` needs to be active. To check if it is active, run: `systemctl status cron`
# 
# On WSL, you may need to edit or create file `/etc/wsl.conf`
# 
# Add the following:
#     [boot]
#     systemd=true
# Then run `wsl --shutdown` on Powershell, then launch WSL again. Source: https://askubuntu.com/questions/1379425/system-has-not-been-booted-with-systemd-as-init-system-pid-1-cant-operate
# 
# 
# Use `sudo systemctl start cron.service` to start cron.
# And `sudo systemctl enable cron.service` to enable startup on boot
#