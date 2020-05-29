#!/usr/bin/env bash

cd $HOME/exporter || exit 1

node ./export.js
./format.py
