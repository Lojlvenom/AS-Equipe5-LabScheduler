#!/bin/bash
./controller/run_controller.sh &
./notification_service/run_notification.sh &
./booking_service/run_booking.sh &
./lab_service/run_lab.sh &
./login_service/run_login.sh &