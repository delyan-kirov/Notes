#!/usr/bin/env bash
source ./env/bin/activate
#flask --app ShareNotes.py --debug run
flask --app ShareNotes.py --debug run --host=0.0.0.0
