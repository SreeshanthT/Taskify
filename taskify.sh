#!/bin/bash
echo asd123. | sudo -S systemctl start mysql

source /home/reizend/Taskify/bin/activate
cd /home/reizend/Projects/test/Taskify
python manage.py runserver 0.0.0.0:8001
