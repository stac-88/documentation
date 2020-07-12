#!/bin/bash

echo Making a tar file of the contents of the folder: $1
tar -cvf $1.tar $1/*.yaml
