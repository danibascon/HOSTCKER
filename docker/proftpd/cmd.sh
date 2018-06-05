#!/bin/bash
set -e

USER=${USER:-""}
PASS=${PASS:-""}

if [[ $USER != "" ]] ;then
	python /usuario.py $USER $PASS
fi
exec proftpd --nodaemon
