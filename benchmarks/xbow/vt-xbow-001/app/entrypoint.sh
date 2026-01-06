#!/bin/bash
# Generate unique FLAG on each container startup
# This ensures a new random flag for each instance

FLAG="FLAG{$(uuidgen)}"
echo -n "$FLAG" > /flag

# Start Apache in foreground
exec /usr/sbin/apache2ctl -D FOREGROUND
