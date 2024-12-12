#!/bin/bash


#####figure out how to start and stop docker properly!

exportpath_host="/home/max/exporttest"

#docker start -it -p 8182:8182 --name janusgraph-container -v $exportpath_host:/opt/janusgraph/export281 --name janusgraph-container janusgraph/janusgraph

#first time startup:
docker run -it -p 8182:8182 --name janusgraph-container -v $exportpath_host:/opt/janusgraph/export281 --name janusgraph-container janusgraph/janusgraph

#then in another window:
#docker exec -u 0:0 janusgraph-container chown -R janusgraph /opt/janusgraph/export281