service cron start
echo "0 * * * *  /usr/local/bin/python3 /app/statistics.py" >> crontab
cp crontab /etc/cron.d/crontab
chmod 777 /etc/cron.d/crontab
crontab /etc/cron.d/crontab
exec "$@"