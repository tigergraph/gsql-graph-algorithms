#!/bin/bash

ps -ef | grep "./run_free.sh" | grep -v grep | awk '{print $2}' | xargs kill;
