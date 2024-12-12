# from gremlin_python.process.anonymous_traversal import traversal
# from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
# import gremlin_python.driver.serializer as serializer

db_url = 'ws://localhost:8182/gremlin'
# #db_url = 'ws://dc-max.local:8182/gremlin'
# connection = DriverRemoteConnection(db_url, 'g', message_serializer=serializer.GraphSONSerializersV3d0())
# g = traversal().with_remote(connection)
# g.V().drop().iterate()

# connection.submit('graph.io(graphml()).writeGraph("/tmp/graph.graphml")')


import datetime
from gremlin_python.driver.client import Client

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
client = Client(db_url, 'g')
client.submit(f'graph.io(IoCore.graphml()).writeGraph("export281/graph_{timestamp}.xml")')