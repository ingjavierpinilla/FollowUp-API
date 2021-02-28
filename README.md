# Video-Club-API-REST

The goal is to design a relational database that stores information on the loan of films from a video club. 
This information is managed in the following way:

When a loan is made, a card is filled in, in which the member who takes the film, the date and the number of the tape are noted. The date and the number of the tape being borrowed, which is unique (there are several copies of each film on different tapes), the office where the film is rented, the value per tape. This card is deposited in the borrowed films file cabinet. When the member returns the tape, the card is transferred to the of returned films.

# Entity–relationship model
![ds_structure](https://github.com/ingjavierpinilla/video-club-API-REST/blob/main/Entity–relationship_model.png)
# Characteristics
The API Rest provides the following information:
  - Consolidated monthly sales by store.
    - Receives the ID of the branch from which the information is desired, returns a json with the sum of the sales per month with the date in ISO 8601 format without including the hour, minutes and seconds.

    - URL: /api/sucursal/<id>

    - Method:

      - GET

    - URL Params

      - Required: id=[integer]

    - Success Response:

      - Code: 200
        Content:
        [
        {"month": "2021-01-01T00:00:00Z",
        "sale_value": 40.0 }
        { "month": "2021-02-01T00:00:00Z",
        "sale_value": 60.0 }
        ]
    - Error Response:

      - Code: 401 UNAUTHORIZED
      - Code: 400 BAD REQUEST
        Content: {'Invalid ID.'}
      - Code: 204 NO CONTENT
        Content: {'Tape <id> not found.'}

  - Daily sales detail, with office id, number of tapes rented and discriminated sales value.
    - Receives a date in ISO 8601 format without including the hour, minutes and seconds i.e. 2010-12-16. Returns a JSON with office_code, rented_tapes and sale_value. Sorted by office code.
    - URL: /api/venta/?fecha
    - Method:
      - GET
    - URL Params
      - Required: date=[string] date in ISO 8601 format i.e. 2010-12-16

    - Success Response:

      - Code: 200
      Content:
      [{ "office_id": 1, "rented_tapes": 2, "sales_value": 40.0 }, { "office_id": 2, "rented_tapes": 1, "sales_value": 20.0 }]
    - Error Response:

      - Code: 401 UNAUTHORIZED

      - Code: 400 NOT FOUND
      Content: {'Date not valid'}

      - Code: 204 NO CONTENT
      Content: {'No information for the requested date.'}
  - Films available for rental.
    - URL: /api/cinta/?disponible=true
    - Method:
      - GET
    - URL Params
      - None
    - Success Response:

      - Code: 200
      Content: [{ "id": 1, "title": "title1", "price": 10.0, "available": true }, { "id": 2, "title": "title2", "price": 20.0, "available": true }, { "id": 3, "title": "title3", "price": 30.0, "available": true }]
    - Error Response:

      - Code: 401 UNAUTHORIZED
      - Code: 400 BAD REQUEST

  - Determine which office has rented the most films among a range of dates. 
    - Receives two dates (from, to) in ISO 8601 format without including the hour, minutes and seconds i.e. 2010-12-16. Return a JSON with branch_code, branch_code__name and sale_value. Sorted by branch code
    - URL: /api/venta/?from&to
    - Method:
      - GET
    - URL Params
      - Required: from=[string] date in ISO 8601 format i.e. 2010-12-16, to=[string] date in ISO 8601 format i.e. 2010-12-16
    - Success Response:

      - Code: 200
      Content: [{ "office_id": 1, "office_id__name": "s1", "sales_value": 40.0 } ]
    - Error Response:

      Code: 401 UNAUTHORIZED


      Code: 400 BAD REQUEST
      Content: {'Date not valid'}

      Code: 400 BAD REQUEST
      Content: {'from' occurs before 'to'.}

      Code: 204 NO CONTENT
      Content: {'No information for the requested date.'}

### Technologies

The REST API was created using the following resources


* [Python] - 3.9
* [Django] - 3.1.7
* [Django REST framework] - 3.12


Licence
----

MIT



   [Python]: <https://www.python.org>
   [Django]: <https://pypi.org/project/Django/>
   [Django REST framework]: <https://pypi.org/project/djangorestframework/>
