#!/bin/bash
echo "Starting server...."
echo "Env variables available are : $(env)"
python -m http.server ${PORT_HTTP}
