# VERIFY — api__replay__mock_server__minimal__v1.0

PASS if:
- Mock server starts and prints "READY"
- Visiting the clone shows populated lists/cards on:
  - home feed
  - one detail page
- Network panel shows calls hitting `localhost:<port>` with 200 responses
- 0 console errors related to API
