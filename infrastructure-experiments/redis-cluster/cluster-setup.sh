rm -rf redis-cluster-nodes
mkdir redis-cluster-nodes
cd redis-cluster-nodes || exit
for i in {7000..7005}; do
  mkdir "node_$i"
  {
    echo "port $i"
    echo "cluster-enabled yes"
    echo "cluster-config-file nodes_$i.conf"
    echo "cluster-node-timeout 5000"
    echo "appendonly yes"
    echo "protected-mode no"
    echo "bind 0.0.0.0"
  } >> "node_$i/redis.conf"
done