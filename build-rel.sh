#!/bin/bash

cd src

source tools/compile-gui.sh
python3 tools/build.py

cd ..

\cp src/dist/* .

source gen-arc.sh
