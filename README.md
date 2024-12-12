# hacktalking_janusgraph

#first time startup:
docker run -it -p 8182:8182 --name janusgraph-container -v ~:/opt/janusgraph/exports --name janusgraph-container janusgraph/janusgraph

#then in another window:
#docker exec -u 0:0 janusgraph-container chown -R janusgraph /opt/janusgraph/exports