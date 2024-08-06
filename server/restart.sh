cd app/log
cat gunicorn.pid|xargs kill -9
rm -rf *.log
rm -rf *.pid
cd ../../
gunicorn --config=gunicorn_config.py praya_institue:app
