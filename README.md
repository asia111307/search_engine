# search_engine

Running project locally:
1. Start Solr engine on port 8983
search_engine/solr-8.0.0 $ bin/solr start -cloud 

2. Activate the project venv
search_engine $ . venv/bin/activate

3. Run Flask app on port 5000
search_engine $ . FLASK_APP=start.py FLASK_DEBUG=1 flask run

4. Open app at localhost:5000. Enjoy searching!



