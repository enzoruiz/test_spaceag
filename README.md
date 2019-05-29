# Test Space AG

## Run

```
docker-compose up -d --build
```

## Tests

### Inside docker container
```
docker exec -ti ID_CONTAINER bash
export DJANGO_SECRET_KEY=123
pytest
```

### Local
```
pytest
```
