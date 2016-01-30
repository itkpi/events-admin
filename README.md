# EventsMonkey

Tool for making events digests.

## Suggest events

curl -X POST -H Content-Type:application/json http://127.0.0.1:5001/api/v1/suggested_events --data '{"title": "1", "submitter_email": "antigluk@gmail.com", "image_url": "http://example.com", "only_date": false, "social": "1", "registration_url": "http://example.com", "place": "1", "team": "default", "when_start": "01/31/2016", "when_end": "01/31/2016", "agenda": "1", "level": "NONE"}'
