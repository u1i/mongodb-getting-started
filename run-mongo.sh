echo Cleanup...
docker kill mymongo 2>/dev/null
docker rm mymongo 2>/dev/null

echo Starting MongoDB
docker run --name mymongo -d mongo
echo Hang on for a moment...
sleep 10
echo Starting Mongo Shell
docker exec -it mymongo mongo

echo "MongoDB Shell stopped. Did you press Ctrl-C maybe? Anyway, simply run the $0 script again like previously."
