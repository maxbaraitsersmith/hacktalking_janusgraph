# hacktalking_janusgraph

On first startup:

`$ sudo docker run -it -p 8182:8182 --name janusgraph-container -v ~:/opt/janusgraph/exports --name janusgraph-container janusgraph/janusgraph`

And then in another window:

`$ sudo docker exec -u 0:0 janusgraph-container chown -R janusgraph /opt/janusgraph/exports`
