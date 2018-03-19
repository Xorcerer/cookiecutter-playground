#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A redplus_interview.taskapp worker -l INFO
