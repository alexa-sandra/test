#!/bin/bash

python manage.py appmodelslist personalinfo --err-stderr > $(date '+%Y-%m-%d').dat
